from tkinter import ttk
import tkinter as tk

from BondClasses import BondStat, BondInfo
from bond_invest_facade import BondInvestFacade
from datetime import datetime
import calendar

from setup_logging import setup_logging
from share_methods import treeview_sort
log= setup_logging()

class BondsPayment():

    def __init__(self, parent_frame: ttk.Frame, token) -> None:
        self.parent_frame = parent_frame

        self.payment_frame = self.__init_frame_payment(parent_frame)
        self.bond_payment_table = self.__init_bond_payment(self.payment_frame)
        self.__place_frame_payment(self.payment_frame)
        self.progress_var= tk.IntVar(value=0)
        self.bond_facade= BondInvestFacade(token)



    def __init_frame_payment(self,parent_frame: ttk.Frame)-> ttk.Frame:
        frame_payment_table = ttk.Frame(parent_frame, borderwidth=1, relief=tk.SOLID, padding=[8, 10],width=1400,height=750)
        return frame_payment_table
    
    def __place_frame_payment(self, frame: ttk.Frame):
        frame.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)


    def __init_bond_payment(self, frame: ttk.Frame) -> ttk.Treeview:
        payment_tree = ttk.Treeview(frame, columns=("name","payment_date","pay_summ"), show="headings")
        payment_tree.bind("<<TreeviewSelect>>")#,self.bond_selected)
        payment_tree.place(width=1350,height=680,x=0, y=0)
        payment_tree.column("#1", stretch=tk.NO,width=230)
        payment_tree.column("#2", stretch=tk.NO,width=250)
        payment_tree.column("#3", stretch=tk.NO,width=150)

        payment_tree.heading("name", text="Название", command=lambda: treeview_sort(payment_tree,0, False))
        payment_tree.heading("payment_date", text="Дата выплаты", command=lambda: treeview_sort(payment_tree,1, False))
        payment_tree.heading("pay_summ", text="Сумма выплаты", command=lambda: treeview_sort(payment_tree,2, False))
        #bond_payment_progess = ttk.Progressbar(frame,orient="horizontal", length=300, variable=self.progress_var)
        #bond_payment_progess.place(width=800,height=10,x=320, y=720)
        bond_payment_button=ttk.Button(frame,text="load data", command=self.bond_payment_enable,style="Green.TButton")
        bond_payment_button.place(width=100,height=30,x=670, y=685)
        
        return payment_tree


    def bonds_payment_table_b(self, payment_list):
        payment_sum=0
        payment_month_sum=0
        payment_month_temp=1
        for payment in payment_list:

            if payment[1].month>payment_month_temp:
                self.bond_payment_table.insert("", tk.END, values=("",calendar.month_name[payment_month_temp],payment_month_sum))
                payment_month_temp=payment[1].month
                payment_month_sum=0
            else:
                log.debug(f"payment source: {payment}")
                payment_month_sum+=int(payment[2])
                log.debug(f"payment month sum: {payment_month_sum}")
            self.bond_payment_table.insert("", tk.END, values=(payment[0],payment[1],payment[2]))
            payment_sum+=int(payment[2])
        self.bond_payment_table.insert("", tk.END, values=("ВСЕГО: ","",payment_sum))
        
    def bonds_payment_table(self, payment_list):
            payment_sum = 0
            payment_month_sum = 0
            payment_month_temp = payment_list[0][1].month if payment_list else 1  # Начинаем с месяца первого платежа
            
            for payment in payment_list:
                current_month = payment[1].month
                
                if current_month > payment_month_temp:
                    # Добавляем сумму за предыдущий месяц перед переходом к следующему
                    self.bond_payment_table.insert("", tk.END, values=("", calendar.month_name[payment_month_temp], f"    {payment_month_sum}"))
                    
                    payment_month_temp = current_month
                    payment_month_sum = 0  # Обнуляем сумму для нового месяца
                
                payment_month_sum += int(payment[2])
                payment_sum += int(payment[2])

                self.bond_payment_table.insert("", tk.END, values=(payment[0], payment[1].strftime('%d-%m-%Y'), payment[2]))

            # Добавляем данные последнего месяца
            self.bond_payment_table.insert("", tk.END, values=("", calendar.month_name[payment_month_temp], payment_month_sum))
            
            # Добавляем итоговую сумму
            self.bond_payment_table.insert("", tk.END, values=("ВСЕГО: ", "", payment_sum))

            log.debug(f"Итоговая сумма выплат: {payment_sum}")



    def bond_payment_enable(self):
        self.bonds_payment_table(self.bond_facade.get_coupon_payments(self.bond_facade.get_current_account(),self.bond_facade.get_start_date(),self.bond_facade.get_end_date()))

    def bond_selected(self):
        pass
    