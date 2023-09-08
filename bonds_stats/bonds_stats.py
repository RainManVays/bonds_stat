import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
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
        self.title('Bonds Payment Stat')
        self.geometry("1400x800")
        self.protocol("WM_DELETE_WINDOW",self.exit)

        self.load_button=ttk.Button(self,text="load statistic", command=self.plot_enable)
        self.initStatistic()
        self.initCoupons()
        self.initLabels()
        self.load_button.pack()
        

    def exit(self):
        if self.plot_widget:
            self.plot_widget.pack_forget()
            plt.close(self.plot_figure)
        self.destroy()

    def initStatistic(self):
        self.frame_table = ttk.Frame(self, borderwidth=1, relief=tk.SOLID, padding=[8, 10],width=1400,height=500)
        self.tree = ttk.Treeview(self.frame_table, columns=("name","count","price","pay","month"), show="headings")
        self.tree.bind("<<TreeviewSelect>>",self.bond_selected)
        self.tree.place(width=650,height=480,x=710, y=0)
        self.frame_table.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)

    def initCoupons(self):
        self.frame_coupons = ttk.Frame(self, borderwidth=1, relief=tk.SOLID, padding=[8, 10],width=1400,height=80)
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

    def initLabels(self):
        self.frame_labels = ttk.Frame(borderwidth=1, relief=tk.SOLID, padding=[8, 10])
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
        self.tree.column("#2", stretch=tk.NO,width=50)
        self.tree.column("#3", stretch=tk.NO,width=70)
        self.tree.column("#4", stretch=tk.NO,width=100)
        self.tree.column("#5", stretch=tk.NO,width=120)

        self.tree.heading("name", text="название")
        self.tree.heading("count", text="Кол-во")
        self.tree.heading("price", text="Цена")
        self.tree.heading("pay", text="Платеж")
        self.tree.heading("month", text="мес")
        
        
        # добавляем данные
        for bond in bonds_list:
            self.tree.insert("", tk.END, values=(bond.bond_name,bond.bonds_count,bond.bond_curr_price, bond.next_pay))

    def bond_selected(self,event):
        selected_bond=""
        for bond in self.tree.selection():
            item = self.tree.item(bond)
            print(item)
            temp = item["values"][1]
            print(temp)
            coupons= self.get_bond_coupons(item["values"][0])
            print(coupons)


            self.coupon_label_clean()
            total_pay=0.0
            for key,value in coupons.items():
                total_pay+=value*temp
                if key.month == 1:
                    self.jan["text"]=f"jan {value*temp}"
                    self.jan["foreground"]="green"
                elif key.month==2:
                    self.feb["text"]=f"feb {value*temp}"
                    self.feb["foreground"]="green"
                elif key.month==3:
                    self.mar["text"]=f"mar {value*temp}"
                    self.mar["foreground"]="green"
                elif key.month==4:
                    self.apr["text"]=f"apr {value*temp}"
                    self.apr["foreground"]="green"
                elif key.month==5:
                    self.may["text"]=f"may {value*temp}"
                    self.may["foreground"]="green"
                elif key.month==6:
                    self.jun["text"]=f"jun {value*temp}"
                    self.jun["foreground"]="green"
                elif key.month==7:
                    self.jul["text"]=f"jul {value*temp}"
                    self.jul["foreground"]="green"
                elif key.month==8:
                    self.aug["text"]=f"aug {value*temp}"
                    self.aug["foreground"]="green"
                elif key.month==9:
                    self.sep["text"]=f"sep {value*temp}"
                    self.sep["foreground"]="green"
                elif key.month==10:
                    self.oct["text"]=f"oct {value*temp}"
                    self.oct["foreground"]="green"
                elif key.month==11:
                    self.nov["text"]=f"nov {value*temp}"
                    self.nov["foreground"]="green"
                elif key.month==12:
                    self.dec["text"]=f"dec {value*temp}"
                    self.dec["foreground"]="green"
            self.coupon_total["text"]=f"TOTAL: {total_pay}"
            self.coupon_total["foreground"]="green"

    def coupon_label_clean(self):
        self.jan["text"]="jan"
        self.jan["foreground"]="black"
        self.feb["text"]="feb"
        self.feb["foreground"]="black"
        self.mar["text"]="mar"
        self.mar["foreground"]="black"
        self.apr["text"]="apr"
        self.apr["foreground"]="black"
        self.may["text"]="may"
        self.may["foreground"]="black"
        self.jun["text"]="jun"
        self.jun["foreground"]="black"
        self.jul["text"]="jul"
        self.jul["foreground"]="black"
        self.aug["text"]="aug"
        self.aug["foreground"]="black"
        self.sep["text"]="sep"
        self.sep["foreground"]="black"
        self.oct["text"]="oct"
        self.oct["foreground"]="black"
        self.nov["text"]="nov"
        self.nov["foreground"]="black"
        self.dec["text"]="dec"
        self.dec["foreground"]="black"
        self.coupon_total["text"]="TOTAL: "
        self.coupon_total["foreground"]="black"




    def plot_enable(self):
        self.plot_widget= self.bond_plot().get_tk_widget()
        self.plot_widget.place(width=700,x=0)
        
        self.total_payment["text"]=(self.bond_result.total_money)
        self.avg_roi["text"]=(self.bond_result.avg_roi)
        self.avg_month["text"]=(self.bond_result.avg_money_for_month)
        self.amount_bonds["text"]=f"total amount in bonds {(self.bond_result.total_amount_bonds)}"

        self.bonds_table(self.bond_result.bonds_stat)
        #self.btn.config(state="disabled")



    def get_pay_dates(self):
        bond_pay_dates={}
        total_year_payment=0.0
        start_date = date(datetime.now().year,1,1)
        end_date = date(datetime.now().year,12,31)
        start_date= datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.min.time())
        bonds_stat=[] 
        with Client(TOKEN) as client:
            accounts = client.users.get_accounts()
            print(accounts)
            portfolio = client.operations.get_portfolio(account_id=config['DEFAULT']["ACCOUNT_ID"])
            account_bonds = client.instruments.bonds().instruments
            for instrument in portfolio.positions:
                if instrument.instrument_type=='bond':
                    bond_name=""
                    for bond in account_bonds:
                        if bond.figi == instrument.figi:
                            bond_name=bond.name
                            print(bond_name)

                    print(f"bond {bond_name} type {instrument.instrument_type} count {instrument.quantity.units} price {instrument.current_price.units}.{instrument.current_price.nano}")
                    #print(client.instruments.bond_by(id_type= InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=str(instrument.figi)))
                    current_bond_coupons={}
                    next_pay=0.0
                    for coupon in client.instruments.get_bond_coupons(figi=instrument.figi,from_= start_date, to=end_date).events:
                        one_pay = float(f'{coupon.pay_one_bond.units}.{coupon.pay_one_bond.nano}')
                        if not next_pay:
                            next_pay=one_pay*instrument.quantity.units
                        print(f'pay date {coupon.coupon_date} pay for one bond {one_pay} all payment for date {one_pay*instrument.quantity.units}')
                        coupon_month=coupon.coupon_date.month#.strftime('%B')
                        if bond_pay_dates.get(coupon_month):
                            
                            bond_pay_dates[coupon_month]+=one_pay*instrument.quantity.units
                        else:
                            bond_pay_dates[coupon_month]=one_pay*instrument.quantity.units
                        total_year_payment+=one_pay*instrument.quantity.units
                        current_bond_coupons["coupon.coupon_date"]=one_pay
                    bonds_stat.append(BondStat(bond_name=bond_name,
                                                bonds_count=instrument.quantity.units,
                                                bond_curr_price=float(f"{instrument.current_price.units}.{instrument.current_price.nano}"),
                                                next_pay=next_pay,
                                                coupons=current_bond_coupons))
        bond_result = BondPayResults(total_amount_bonds=portfolio.total_amount_bonds.units,
                                    total_year_payment=total_year_payment,
                                    count_bonds=portfolio.total_amount_bonds.units,
                                    bond_pay_dates=bond_pay_dates,
                                    bonds_stat=bonds_stat)

        self.bond_result = bond_result
        return bond_result


    def get_bond_coupons(self, bond_name:str):
        start_date = date(datetime.now().year,1,1)
        end_date = date(datetime.now().year,12,31)
        start_date= datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.min.time())
        current_bond_coupons={}
        with Client(TOKEN) as client:
            account_bonds = client.instruments.bonds().instruments
            bond_figi=""
            print(bond_name)
            for bond in account_bonds:
                if bond.name in bond_name:
                    bond_figi=bond.figi
                    break
            portfolio = client.operations.get_portfolio(account_id=config['DEFAULT']["ACCOUNT_ID"])
            print(bond_figi)
            for instrument in portfolio.positions:
                if instrument.figi==bond_figi:
                    for coupon in client.instruments.get_bond_coupons(figi=bond_figi,from_= start_date, to=end_date).events:
                        one_pay = float(f'{coupon.pay_one_bond.units}.{coupon.pay_one_bond.nano}')
                        print(f'pay date {coupon.coupon_date} pay for one bond {one_pay} all payment for date {one_pay*instrument.quantity.units}')
                        coupon_month=coupon.coupon_date.month#.strftime('%B')
                        current_bond_coupons[coupon.coupon_date]=one_pay
                    break
                
            return current_bond_coupons 



    def bond_plot(self):
        payments_stat = self.get_pay_dates()
        lists = sorted(payments_stat.bond_pay_dates.items())
        month_name = lambda month:calendar.month_abbr[month]
        month, counts= zip(*lists)
        month = [month_name(x) for x in month]
        #month = ["jan", "feb", "march", "apr", "may", "jun","jul", "aug", "sep", "oct", "nov", "dec"]
        #counts = [5132, 2664, 2164, 727.29, 1716, 2174, 5118, 2664,2065, 1730, 647, 2016]
        bar_labels = ['red', 'blue', '_red', 'orange','red', 'blue', '_red', 'orange','red', 'blue', '_red', 'orange']
        #bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:red', 'tab:blue', 'tab:red', 'tab:orange','tab:red', 'tab:blue', 'tab:red', 'tab:orange']
        bar_colors=[]
        for count in counts:
            if count <=1500:
                bar_colors.append('tab:red')
            elif count <= 3000 and count > 1500:
                bar_colors.append('tab:orange')
            elif count >=5000:
                bar_colors.append('tab:green')
            else:
                bar_colors.append('tab:blue')

        self.plot_figure, ax = plt.subplots()

        figure_canvas= FigureCanvasTkAgg(self.plot_figure,self.frame_table)
        NavigationToolbar2Tk(figure_canvas,self)
        hbars = ax.bar(x=month, height= counts, label=counts,color=bar_colors)
        ax.bar_label(hbars, fmt='%.0f')

        ax.set_ylabel('rub')
        ax.set_xlabel(f'total: {sum(counts):.2f}')
        ax.set_title('bond payments')

        return figure_canvas


if __name__ == '__main__':
    app = App()
    app.mainloop()