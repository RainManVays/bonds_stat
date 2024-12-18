import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from bond_invest_facade import BondInvestFacade
from bonds_screener_view import BondsScreener
from bond_payment_view import BondsPayment
from database import init_db
import crud
from share_methods import treeview_sort
matplotlib.use('TkAgg')
import calendar
from  BondClasses import *
from tkinter import ttk
from datetime import datetime, date
from webbrowser import get
from tinkoff.invest import Client, BondResponse, PortfolioResponse, PortfolioPosition, InstrumentIdType, GetBondCouponsResponse
import sys, os, configparser
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
config= configparser.ConfigParser()
config.read('config.ini')

from setup_logging import setup_logging
log= setup_logging()


os.environ["INVEST_TOKEN"]=config['DEFAULT']["TOKEN"]
from tinkoff.invest.token import TOKEN



class App(tk.Tk):
    btn = None
    clicks=0
    plot_widget=None
    bond_result=None
    plot_figure=None

    def __init__(self):
        super().__init__()
        self.title('Bonds Payment Statistic')
        self.geometry("1400x800")
        self.protocol("WM_DELETE_WINDOW",self.exit)
        self.bond_invest_facade = BondInvestFacade(TOKEN)
        self.init_style()

        self.notebook = ttk.Notebook(style="Green.TNotebook")
        self.notebook.pack(expand=True, fill=tk.BOTH)


        self.my_bond_frame = ttk.Frame(self.notebook)
        self.bond_payment = ttk.Frame(self.notebook)
        self.bond_screener = ttk.Frame(self.notebook)
        
        self.my_bond_frame.pack(fill=tk.BOTH, expand=True)
        self.bond_payment.pack(fill=tk.BOTH, expand=True)
        self.bond_screener.pack(fill=tk.BOTH, expand=True)
        
        # добавляем фреймы в качестве вкладок
        self.notebook.add(self.my_bond_frame, text="MyBond")
        self.notebook.add(self.bond_payment, text="MyBondPayments")
        self.notebook.add(self.bond_screener, text="Bond Screener")

       
        self.load_button=ttk.Button(self.my_bond_frame,text="load statistic", command=self.plot_enable,style="Green.TButton")
        
        self.init_accounts_combobox()
        
        self.initStatistic()
        self.initCoupons()
        self.initLabels()
        

        bs = BondsScreener(self.bond_screener, TOKEN)
        bp = BondsPayment(self.bond_payment, TOKEN)
        
        self.load_button.pack()
        
    def init_style(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Используем тему "clam" для лучшей кастомизации
        self.style.configure("Green.TButton", background="#4CAF50", foreground="white", font=("Arial", 12))
        

        # Настраиваем стиль для таблицы
        self.style.configure("Treeview",
                             background="#f0f0f0",  # Цвет фона
                             foreground="black",    # Цвет текста
                             rowheight=25,          # Высота строки
                             fieldbackground="#e0e0e0",  # Фон ячеек
                             font=("Arial", 12))    # Шрифт

        # Настраиваем стиль заголовков
        self.style.configure("Treeview.Heading",
                             background="#4CAF50",  # Цвет фона заголовка
                             foreground="white",    # Цвет текста заголовка
                             font=("Arial", 13, "bold"))  # Жирный шрифт

        # Настраиваем цвет выделения строки
        self.style.map("Treeview",
                       background=[("selected", "#90EE90")],  # Цвет выделенной строки
                       foreground=[("selected", "black")])
        # Стиль для Notebook (вкладки)
        self.style.configure("Green.TNotebook",
                             background="#4CAF50",
                             foreground="white",
                             padding=[10, 5],
                             font=("Arial", 12, "bold"))

        self.style.map("Green.TNotebook",
                       background=[("selected", "#388E3C")],  # Цвет активной вкладки
                       foreground=[("selected", "white")])
        # Стиль для Combobox
        self.style.configure("Combobox",
                             fieldbackground="#e0e0e0",  # Цвет фона поля
                             background="#ffffff",       # Цвет кнопки
                             foreground="#333333",       # Цвет текста
                             font=("Arial", 12))



    def exit(self):
        if self.plot_widget:
            self.plot_widget.pack_forget()
            plt.close(self.plot_figure)
        self.destroy()

    def init_accounts_combobox(self):
        accounts = self.bond_invest_facade.get_all_accounts()
        self.account_list_combobox = ttk.Combobox(self.notebook, values=list(accounts.keys()))
        self.account_list_combobox.pack(expand=False,padx=600)
        self.account_list_combobox.bind("<<ComboboxSelected>>", self.account_selected)
        #self.progress = ttk.Progressbar(self.my_bond_frame, orient="horizontal", mode="indeterminate", length=300)
        #self.progress.pack(padx=5, side="right")
        
    def account_selected(self, event):
        selection = self.account_list_combobox.get()
        account_id =self.bond_invest_facade.get_account_id_on_name(selection)
        self.current_account=account_id
        self.bond_invest_facade.set_current_account(account_id)

    def initStatistic(self):
        self.frame_table = ttk.Frame(self.my_bond_frame, borderwidth=1, relief=tk.SOLID, padding=[8, 10],width=1400,height=500)
        self.tree = ttk.Treeview(self.frame_table, columns=("name","count","price","pay","month","percent","end_date"), show="headings")
        self.tree.bind("<<TreeviewSelect>>",self.bond_selected)
        self.tree.place(width=730,height=480,x=640, y=0)
        self.frame_table.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)

    def initCoupons(self):
        self.frame_coupons = ttk.Frame(self.my_bond_frame, borderwidth=1, relief=tk.SOLID, padding=[8, 10],width=1400,height=80)
        self.jan = ttk.Label(self.frame_coupons,text="jan", font=("Arial",13))
        self.feb = ttk.Label(self.frame_coupons,text="feb", font=("Arial",13))
        self.mar = ttk.Label(self.frame_coupons,text="mar", font=("Arial",13))
        self.apr = ttk.Label(self.frame_coupons,text="apr", font=("Arial",13))
        self.may = ttk.Label(self.frame_coupons,text="may", font=("Arial",13))
        self.jun = ttk.Label(self.frame_coupons,text="jun", font=("Arial",13))
        self.jul = ttk.Label(self.frame_coupons,text="jul", font=("Arial",13))
        self.aug = ttk.Label(self.frame_coupons,text="aug", font=("Arial",13))
        self.sep = ttk.Label(self.frame_coupons,text="sep", font=("Arial",13))
        self.oct = ttk.Label(self.frame_coupons,text="oct", font=("Arial",13))
        self.nov = ttk.Label(self.frame_coupons,text="nov", font=("Arial",13))
        self.dec = ttk.Label(self.frame_coupons,text="dec", font=("Arial",13))
        self.coupon_total = ttk.Label(self.frame_coupons,text="Total: ", font=("Arial",14))
        self.jan.place(width=150,height=30,x=0,y=5)
        self.feb.place(width=150,height=30,x=200,y=5)
        self.mar.place(width=150,height=30,x=400,y=5)
        self.apr.place(width=150,height=30,x=600,y=5)
        self.may.place(width=150,height=30,x=800,y=5)
        self.jun.place(width=150,height=30,x=1000,y=5)
        self.coupon_total.place(width=150,height=30,x=1200,y=5)
        self.jul.place(width=150,height=30,x=0,y=30)
        self.aug.place(width=150,height=30,x=200,y=30)
        self.sep.place(width=150,height=30,x=400,y=30)
        self.oct.place(width=150,height=30,x=600,y=30)
        self.nov.place(width=150,height=30,x=800,y=30)
        self.dec.place(width=150,height=30,x=1000,y=30)
        self.frame_coupons.pack(anchor=tk.S, fill=tk.X, padx=5, pady=5)



    def initCoupons_new(self):
        self.frame_coupons = ttk.Frame(
                self.my_bond_frame,
                borderwidth=1,
                relief=tk.SOLID,
                padding=[8, 10],
                width=1400,
                height=80
            )

        # Список месяцев и их позиции
        months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
        label_width = 150
        label_height = 30
        x_offset = 200
        y_positions = [5, 30]

        # Создаем и размещаем метки для месяцев
        self.month_labels = {}
        for i, month in enumerate(months):
            x = (i % 6) * x_offset
            y = y_positions[i // 6]
            label = ttk.Label(self.frame_coupons, text=month, font=("Arial", 13))
            label.place(width=label_width, height=label_height, x=x, y=y)
            self.month_labels[month] = label

        # Метка для общей суммы
        self.coupon_total = ttk.Label(self.frame_coupons, text="Total: ", font=("Arial", 14))
        self.coupon_total.place(width=label_width, height=label_height, x=1200, y=5)

        # Размещение фрейма
        self.frame_coupons.pack(anchor=tk.S, fill=tk.X, padx=5, pady=5)

    def initLabels(self):
        self.frame_labels = ttk.Frame(self.my_bond_frame,borderwidth=1, relief=tk.SOLID, padding=[8, 10])
        self.total_payment = ttk.Label(self.frame_labels,text="total_payment")
        self.avg_roi = ttk.Label(self.frame_labels,text="avg_roi")
        self.avg_month= ttk.Label(self.frame_labels,text="avg_month")
        self.amount_bonds= ttk.Label(self.frame_labels,text="amount_bonds")
        self.total_payment.pack()
        self.avg_roi.pack()
        self.avg_month.pack()
        self.amount_bonds.pack()
        self.frame_labels.pack(anchor=tk.S, fill=tk.X, padx=5, pady=5)
        

    def bonds_table(self, bonds_list: [BondStat]):
        # определяем заголовки
        self.tree.column("#1", stretch=tk.NO,width=230)
        self.tree.column("#2", stretch=tk.NO,width=60)
        self.tree.column("#3", stretch=tk.NO,width=70)
        self.tree.column("#4", stretch=tk.NO,width=100)
        self.tree.column("#5", stretch=tk.NO,width=140)
        self.tree.column("#6", stretch=tk.NO,width=50)
        self.tree.column("#7", stretch=tk.NO,width=70)

        self.tree.heading("name", text="Название", command=lambda: treeview_sort(self.tree,0, False))
        self.tree.heading("count", text="Кол-во", command=lambda: treeview_sort(self.tree,1, False))
        self.tree.heading("price", text="Цена", command=lambda: treeview_sort(self.tree,2, False))
        self.tree.heading("pay", text="Платеж", command=lambda: treeview_sort(self.tree,3, False))
        self.tree.heading("month", text="Мес", command=lambda: treeview_sort(self.tree,4, False))
        self.tree.heading("percent", text="%", command=lambda: treeview_sort(self.tree,5, False))
        self.tree.heading("end_date", text="end_date", command=lambda: treeview_sort(self.tree,6, False))

        # добавляем данные
        self.tree.delete(*self.tree.get_children())
        for bond in bonds_list:
            month_cnt= 12 if "All" in bond.months else len(bond.months)
            percent = f"{(bond.next_pay/bond.bonds_count*(month_cnt)/bond.bond_curr_price*100):.2f}"
            self.tree.insert("", tk.END, values=(bond.bond_name,bond.bonds_count,bond.bond_curr_price, bond.next_pay, bond.months,percent,bond.bond_end_date))


    def bond_selected(self, event):
        for bond in self.tree.selection():
            log.debug(f"selected bond {bond}")
            item = self.tree.item(bond)
            bond_name = item["values"][0]
            coupon_count = item["values"][1]
            log.debug(f'bond_name {bond_name}')
            coupons =self.get_figi_bond_coupons(crud.get_bond_figi_on_name(bond_name))
            log.debug(f"bond coupons {coupons}")
            self.coupon_label_clean()
            fg_color = "green"
            total_pay = 0.0
            self.bond_result
            month_labels = {
                1: self.jan,
                2: self.feb,
                3: self.mar,
                4: self.apr,
                5: self.may,
                6: self.jun,
                7: self.jul,
                8: self.aug,
                9: self.sep,
                10: self.oct,
                11: self.nov,
                12: self.dec,
            }

            for month, value in coupons.items():
                log.debug(f"month {month} value {value}")
                payment = value * coupon_count
                total_pay += payment

                label = month_labels.get(month.month)
                if label:
                    label["text"] = f"{calendar.month_abbr[month.month]} {payment}"
                    label["foreground"] = fg_color

            self.coupon_total["text"] = f"TOTAL: {total_pay}"
            self.coupon_total["foreground"] = fg_color
        
        
    def coupon_label_clean(self):
        self.jan["text"]="jan"
        self.feb["text"]="feb"
        self.mar["text"]="mar"
        self.apr["text"]="apr"
        self.may["text"]="may"
        self.jun["text"]="jun"
        self.jul["text"]="jul"
        self.aug["text"]="aug"
        self.sep["text"]="sep"
        self.oct["text"]="oct"
        self.nov["text"]="nov"
        self.dec["text"]="dec"
        self.coupon_total["text"]="TOTAL: "
        for item in self.frame_coupons.winfo_children():
            item["foreground"]="black"


    def plot_enable(self):
        if self.plot_widget:
            self.plot_widget.delete(self.plot_widget.children)
        
        self.plot_widget= self.bond_plot().get_tk_widget()
        self.plot_widget.place(width=630,x=0)
        
        self.total_payment["text"]=(self.bond_result.total_money)
        self.avg_roi["text"]=(self.bond_result.avg_roi)
        self.avg_month["text"]=(self.bond_result.avg_money_for_month)
        self.amount_bonds["text"]=f"total amount in bonds {(self.bond_result.total_amount_bonds)}"
        
        self.bonds_table(self.bond_result.bonds_stat)


    def get_start_date(self):
        start_date = date(datetime.now().year,1,1)
        return datetime.combine(start_date, datetime.min.time())
    
    def get_end_date(self):
        end_date = date(datetime.now().year,12,31)
        return datetime.combine(end_date, datetime.min.time())

    def get_pay_dates(self):
        bond_pay_dates={}
        total_year_payment=0.0
        
        bond_facade = BondInvestFacade(TOKEN)
        bonds_stat=[] 
        with Client(TOKEN) as client:
            portfolio = client.operations.get_portfolio(account_id=self.bond_invest_facade.get_current_account())
            for instrument in portfolio.positions:
                if instrument.instrument_type=='bond':
                    bond_name= bond_facade.get_bond_name(instrument.figi)
                    bonds_count = instrument.quantity.units
                    bond_actual_price=float(f"{instrument.current_price.units}.{instrument.current_price.nano}")
                    log.debug(f"bond {bond_name} type {instrument.instrument_type} count {bonds_count} price {bond_actual_price:.2f}")
                    current_bond_coupons={}
                    total_month_pay=0.0
                    bond_payment_months=[]
                    for coupon in client.instruments.get_bond_coupons(figi=instrument.figi,from_= self.get_start_date(), to=self.get_end_date()).events:
                        one_pay = float(f'{coupon.pay_one_bond.units}.{coupon.pay_one_bond.nano}')
                        if not total_month_pay:
                            total_month_pay=float(f"{one_pay*bonds_count:.2f}")
                        log.debug(f'pay date {coupon.coupon_date} pay for one bond {one_pay} all payment for date {total_month_pay}')
                        coupon_month=coupon.coupon_date.month#.strftime('%B')
                        bond_payment_months.append(calendar.month_abbr[coupon_month])
                        if bond_pay_dates.get(coupon_month):
                            bond_pay_dates[coupon_month]+=total_month_pay
                        else:
                            bond_pay_dates[coupon_month]=total_month_pay
                        total_year_payment+=total_month_pay
                        current_bond_coupons["coupon.coupon_date"]=one_pay
                    bonds_stat.append(BondStat(bond_figi=instrument.figi,bond_name=bond_name,
                                                bonds_count=bonds_count,
                                                bond_curr_price=float(f"{instrument.current_price.units}.{instrument.current_price.nano}"),
                                                next_pay=total_month_pay,
                                                coupons=current_bond_coupons,
                                                months=bond_payment_months,
                                                end_date=bond_facade.get_bond_maturity_date(instrument.figi).strftime("%Y-%m")))
        bond_result = BondPayResults(total_amount_bonds=portfolio.total_amount_bonds.units,
                                    total_year_payment=total_year_payment,
                                    count_bonds=portfolio.total_amount_bonds.units,
                                    bond_pay_dates=bond_pay_dates,
                                    bonds_stat=bonds_stat)

        self.bond_result = bond_result
        return bond_result


    def get_figi_bond_coupons(self, bond_figi:str):
        current_bond_coupons={}
        with Client(TOKEN) as client:
            for coupon in client.instruments.get_bond_coupons(figi=bond_figi,from_= self.get_start_date(), to=self.get_end_date()).events:
                log.debug(f"found bound coupon {coupon}")
                one_pay = float(f'{coupon.pay_one_bond.units}.{coupon.pay_one_bond.nano}')
                current_bond_coupons[coupon.coupon_date]=one_pay

            return current_bond_coupons 

    def bond_plot(self):
        red=int(config['Graph']["red_color_limit"])
        orange=int(config['Graph']["orange_color_limit"])
        green=int(config['Graph']["green_color_limit"])
        payments_stat = self.get_pay_dates()
        lists = sorted(payments_stat.bond_pay_dates.items())
        month_name = lambda month:calendar.month_abbr[month]
        month, counts= zip(*lists)
        month = [month_name(x) for x in month]
        bar_colors=[]
        for count in counts:
            if count <=red:
                bar_colors.append('tab:red')
            elif count <= orange and count > red:
                bar_colors.append('tab:orange')
            elif count >=green:
                bar_colors.append('tab:green')
            else:
                bar_colors.append('tab:blue')
        if self.plot_figure:
            self.plot_figure.clear()
        self.plot_figure, ax = plt.subplots()
        figure_canvas= FigureCanvasTkAgg(self.plot_figure,self.frame_table)
        NavigationToolbar2Tk(figure_canvas,self, pack_toolbar=False)

        hbars = ax.bar(x=month, height= counts, label=counts,color=bar_colors)
        ax.bar_label(hbars, fmt='%.0f')
        ax.set_ylabel('rub')
        ax.set_xlabel(f'total: {sum(counts):.2f}')
        ax.set_title('bond payments')

        return figure_canvas


if __name__ == '__main__':
    app = App()
    log.info("Application Started.")
    init_db()
    app.mainloop()