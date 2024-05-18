from tkinter import ttk
import tkinter as tk

from BondClasses import BondStat, BondInfo
from bond_invest_facade import BondInvestFacade

class BondsScreener():

    def __init__(self, parent_frame: ttk.Frame, token) -> None:
        self.parent_frame = parent_frame

        self.screener_frame = self.__init_frame_screener(parent_frame)
        self.bond_screener_table = self.__init_bond_screener(self.screener_frame)
        self.__place_frame_screener(self.screener_frame)
        self.progress_var= tk.IntVar(value=0)
        self.bond_facade= BondInvestFacade(token)



    def __init_frame_screener(self,parent_frame: ttk.Frame)-> ttk.Frame:
        frame_screener_table = ttk.Frame(parent_frame, borderwidth=1, relief=tk.SOLID, padding=[8, 10],width=1400,height=750)
        return frame_screener_table
    
    def __place_frame_screener(self, frame: ttk.Frame):
        frame.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)


    def __init_bond_screener(self, frame: ttk.Frame) -> ttk.Treeview:
        screener_tree = ttk.Treeview(frame, columns=("name","last_pay_year","price","months","percent","coupon","period","duration","amortization","static coupon","rating"), show="headings")
        screener_tree.bind("<<TreeviewSelect>>",self.bond_selected)
        screener_tree.place(width=1350,height=680,x=0, y=0)
        screener_tree.column("#1", stretch=tk.NO,width=230)
        screener_tree.column("#2", stretch=tk.NO,width=80)
        screener_tree.column("#3", stretch=tk.NO,width=70)
        screener_tree.column("#4", stretch=tk.NO,width=100)
        screener_tree.column("#5", stretch=tk.NO,width=110)
        screener_tree.column("#6", stretch=tk.NO,width=120)
        screener_tree.column("#7", stretch=tk.NO,width=120)
        screener_tree.column("#8", stretch=tk.NO,width=120)
        screener_tree.column("#9", stretch=tk.NO,width=80)
        screener_tree.column("#10", stretch=tk.NO,width=80)

        screener_tree.heading("name", text="Название", command=lambda: self.test_sort(0, False))
        screener_tree.heading("last_pay_year", text="погашение", command=lambda: self.test_sort(1, False))
        screener_tree.heading("price", text="Цена", command=lambda: self.test_sort(2, False))
        screener_tree.heading("months", text="Мес", command=lambda: self.test_sort(3, False))
        screener_tree.heading("percent", text="проценты", command=lambda: self.test_sort(4, False))
        screener_tree.heading("coupon", text="купон", command=lambda: self.test_sort(5, False))
        screener_tree.heading("period", text="период", command=lambda: self.test_sort(6, False))
        screener_tree.heading("duration", text="дюрация", command=lambda: self.test_sort(7, False))
        screener_tree.heading("amortization", text="амортизация", command=lambda: self.test_sort(8, False))
        screener_tree.heading("static coupon", text="фикс купон", command=lambda: self.test_sort(9, False))
        #bond_screener_progess = ttk.Progressbar(frame,orient="horizontal", length=300, variable=self.progress_var)
        #bond_screener_progess.place(width=800,height=10,x=320, y=720)
        bond_screener_button=ttk.Button(frame,text="load data", command=self.bond_screener_enable)
        bond_screener_button.place(width=100,height=30,x=670, y=685)
        
        return screener_tree
    
    def test_sort(self, col, reverse):
        # получаем все значения столбцов в виде отдельного списка
        l = [(self.bond_screener_table.set(k, col), k) for k in self.bond_screener_table.get_children("")]
        # сортируем список
        l.sort(reverse=reverse)
        # переупорядочиваем значения в отсортированном порядке
        for index,  (_, k) in enumerate(l):
            self.bond_screener_table.move(k, "", index)
        # в следующий раз выполняем сортировку в обратном порядке
        self.bond_screener_table.heading(col, command=lambda: self.test_sort(col, not reverse))


    def bonds_screener_table(self, bonds_list: list[BondInfo]):
        for bond in bonds_list:
            self.bond_screener_table.insert("", tk.END, values=(bond.bond_name,bond.bond_end_date,bond.bond_curr_price,bond.bond_month_payments, bond.percent,bond.bond_coupon))

    def bond_screener_enable(self):
        self.bonds_screener_table(self.bond_facade.get_all_bonds())

    def bond_selected(self):
        pass
    