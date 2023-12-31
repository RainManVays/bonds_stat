from tkinter import ttk
import tkinter as tk

from BondClasses import BondStat, BondInfo
from bond_invest_facade import BondInvestFacade

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
        payment_tree.bind("<<TreeviewSelect>>",self.bond_selected)
        payment_tree.place(width=1350,height=680,x=0, y=0)
        payment_tree.column("#1", stretch=tk.NO,width=230)
        payment_tree.column("#2", stretch=tk.NO,width=250)
        payment_tree.column("#3", stretch=tk.NO,width=150)

        payment_tree.heading("name", text="Название", command=lambda: self.test_sort(0, False))
        payment_tree.heading("payment_date", text="Дата выплаты", command=lambda: self.test_sort(1, False))
        payment_tree.heading("pay_summ", text="Сумма выплаты", command=lambda: self.test_sort(2, False))
        #bond_payment_progess = ttk.Progressbar(frame,orient="horizontal", length=300, variable=self.progress_var)
        #bond_payment_progess.place(width=800,height=10,x=320, y=720)
        bond_payment_button=ttk.Button(frame,text="load data", command=self.bond_payment_enable)
        bond_payment_button.place(width=100,height=30,x=670, y=685)
        
        return payment_tree
    
    def test_sort(self, col, reverse):
        # получаем все значения столбцов в виде отдельного списка
        l = [(self.bond_payment_table.set(k, col), k) for k in self.bond_payment_table.get_children("")]
        # сортируем список
        l.sort(reverse=reverse)
        # переупорядочиваем значения в отсортированном порядке
        for index,  (_, k) in enumerate(l):
            self.bond_payment_table.move(k, "", index)
        # в следующий раз выполняем сортировку в обратном порядке
        self.bond_payment_table.heading(col, command=lambda: self.test_sort(col, not reverse))


    def bonds_payment_table(self, payment_list):
        for payment in payment_list:
            self.bond_payment_table.insert("", tk.END, values=(payment[0],payment[1],payment[2]))

    def bond_payment_enable(self):
        self.bonds_payment_table(self.bond_facade.get_coupon_payments())

    def bond_selected(self):
        pass
    