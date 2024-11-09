from tkinter import ttk
import tkinter as tk

from BondClasses import BondStat, BondInfo
from bond_invest_facade import BondInvestFacade
from models import BondSqlData
from setup_logging import setup_logging
from share_methods import treeview_sort
log= setup_logging()

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
        screener_tree.column("#2", stretch=tk.NO,width=70)
        screener_tree.column("#3", stretch=tk.NO,width=70)
        screener_tree.column("#4", stretch=tk.NO,width=100)
        screener_tree.column("#5", stretch=tk.NO,width=110)
        screener_tree.column("#6", stretch=tk.NO,width=120)
        screener_tree.column("#7", stretch=tk.NO,width=120)
        screener_tree.column("#8", stretch=tk.NO,width=120)
        screener_tree.column("#9", stretch=tk.NO,width=80)
        screener_tree.column("#10", stretch=tk.NO,width=80)

        screener_tree.heading("name", text="Название", command=lambda: treeview_sort(screener_tree,0, False))
        screener_tree.heading("last_pay_year", text="погашение", command=lambda: treeview_sort(screener_tree,1, False))
        screener_tree.heading("price", text="Цена", command=lambda: treeview_sort(screener_tree,2, False))
        screener_tree.heading("months", text="Мес", command=lambda: treeview_sort(screener_tree,3, False))
        screener_tree.heading("percent", text="проценты", command=lambda: treeview_sort(screener_tree,4, False))
        screener_tree.heading("coupon", text="купон", command=lambda: treeview_sort(screener_tree,5, False))
        screener_tree.heading("period", text="период", command=lambda: treeview_sort(screener_tree,6, False))
        screener_tree.heading("duration", text="дюрация", command=lambda: treeview_sort(screener_tree,7, False))
        screener_tree.heading("amortization", text="аморт", command=lambda: treeview_sort(screener_tree,8, False))
        screener_tree.heading("static coupon", text="фикс купн", command=lambda: treeview_sort(screener_tree,9, False))
        #bond_screener_progess = ttk.Progressbar(frame,orient="horizontal", length=300, variable=self.progress_var)
        #bond_screener_progess.place(width=800,height=10,x=320, y=720)
        bond_screener_button=ttk.Button(frame,text="load data", command=self.bond_screener_enable,style="Green.TButton")
        bond_screener_button.place(width=100,height=30,x=670, y=685)
        
        return screener_tree


    def bonds_screener_table(self, bonds_list: list[BondSqlData]):
        for bond in bonds_list:
            self.bond_screener_table.insert("", tk.END, values=(bond.name,bond.maturity_date, bond.currency))#,bond.bond_curr_price,bond.bond_month_payments, bond.percent,bond.bond_coupon,bond.pay_period,"дюр",bond.amortization,bond.fix_coupon)) .strftime("%Y-%m")

    def bond_screener_enable(self):
        self.bonds_screener_table(self.bond_facade.get_all_bonds())

    def bond_selected(self):
        pass
    