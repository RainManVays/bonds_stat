from tkinter import ttk
import tkinter as tk

class BondsScreener():


    def init_frame_screener(self,parent_frame: ttk.Frame)-> ttk.Frame:
        frame_screener_table = ttk.Frame(parent_frame, borderwidth=1, relief=tk.SOLID, padding=[8, 10],width=1400,height=750)
        return frame_screener_table
    
    def place_frame_screener(self, frame: ttk.Frame):
        frame.pack(anchor=tk.NW, fill=tk.X, padx=5, pady=5)