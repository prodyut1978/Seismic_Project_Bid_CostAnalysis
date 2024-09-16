#Front End
import os
from tkinter import*
import tkinter.messagebox
import Eagle_Bid_Database_BackEnd
import Eagle_Bid_Trucking_REPORT
import tkinter.ttk as ttk
import tkinter as tk
import sqlite3
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import pandas as pd
import openpyxl
import csv
import time
import datetime

Default_Date_today   = datetime.date.today()

class BidEagle_Trucking_Equipment_Expense:
    
    def __init__(self,root):

        ## Define Global Variables       
        Province            = StringVar()
        ProvinceTax         = DoubleVar()
        Currency            = StringVar()

        ## Define Trucking Variables
        TotalSP             = IntVar()
        TotalRP             = IntVar()
        TotalKM             = DoubleVar()
        
        TruckingEQ          = StringVar()
        Quantity            = IntVar()
        ShiftHours          = DoubleVar()
        RateHours           = DoubleVar()
        CountTrucking_Entry = IntVar()

        
        self.root =root
        self.root.title ("Eagle Bid Equipment Trucking Expenses")
        self.root.geometry("1222x450+0+0")
        self.root.config(bg="cadet blue")
        self.root.resizable(0, 0)
        
        # Entry For Equipment Trucking Expenses
        Label_DataFrameLEFT = Label(self.root, text = "TRUCKING VARIABLES :", font=("arial", 10,'bold'),bg = "cadet blue", fg="blue").place(x=2,y=2)
        DataFrameLEFT = LabelFrame(self.root, bd = 1, width = 520, height = 450, padx= 1, pady= 1, relief = RIDGE,
                                   bg = "cadet blue",font=('aerial', 15, 'bold'))
        DataFrameLEFT.place(x=2,y=25)
        
        
        self.lblTotalSP = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "1. Total Planned Shot Points :    ", padx =1, pady= 2, bg = "cadet blue")
        self.lblTotalSP.grid(row =0, column = 0, sticky =W)
        self.txtTotalSP = Entry(DataFrameLEFT, font=('aerial', 9, 'bold'), textvariable = TotalSP, width = 14, bd=1)
        self.txtTotalSP.grid(row =0, column = 1)

        self.lblTotalRP = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "3. Total Planned Receiver Points:    ", padx =1, pady= 2, bg = "cadet blue")
        self.lblTotalRP.grid(row =1, column = 0, sticky =W)
        self.txtTotalRP= Entry(DataFrameLEFT, font=('aerial', 9, 'bold'), textvariable = TotalRP, width = 14, bd=1)
        self.txtTotalRP.grid(row =1, column = 1)
        
        self.lblTotalKM = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "3. Total Linear Kilometers  (km):    ", padx =1, pady= 2, bg = "cadet blue")
        self.lblTotalKM.grid(row =2, column = 0, sticky =W)
        self.txtTotalKM = Entry(DataFrameLEFT, font=('aerial', 9, 'bold'), textvariable = TotalKM, width = 14, bd=1)
        self.txtTotalKM.grid(row =2, column = 1)


        # Equipment Trucking Profile 
        Label_TableMargin_Trucking = Label(self.root, text = "TRUCKING PROFILE :", font=("arial", 10,'bold'),bg = "cadet blue", fg="blue").place(x=2,y=107)
        TableMargin_Trucking = Frame(self.root)
        TableMargin_Trucking.place(x=2,y=129)         
        scrollbary = Scrollbar(TableMargin_Trucking, orient=VERTICAL)
        tree_Trucking = ttk.Treeview(TableMargin_Trucking, column=("column1", "column2", "column3", "column4"),
                            height=12, show='headings')
        scrollbary.config(command=tree_Trucking.yview)
        scrollbary.pack(side=RIGHT, fill=Y)   
        tree_Trucking.heading("#1", text="Trucking Equipment", anchor=W)
        tree_Trucking.heading("#2", text="Quantity", anchor=W)
        tree_Trucking.heading("#3", text="Shift Hours", anchor=W)
        tree_Trucking.heading("#4", text="Rate/Hour", anchor=W)
                        
        tree_Trucking.column('#1', stretch=NO, minwidth=0, width=140)            
        tree_Trucking.column('#2', stretch=NO, minwidth=0, width=70)
        tree_Trucking.column('#3', stretch=NO, minwidth=0, width=80)
        tree_Trucking.column('#4', stretch=NO, minwidth=0, width=80)
        
        tree_Trucking.pack()

        txtEditTruckingEQ_List = ["Equipment Trailers", "Vibe Trucking", "Dozers","Drills", "Cats & Drills", "Camp Trucking",
                                 "Cat Chasers", "New Cut/Cats", "Snow Plowing", "Trucks & Quads"]
        self.txtEditTruckingEQ = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = TruckingEQ, width = 19)
        self.txtEditTruckingEQ.place(x=2,y=398)
        self.txtEditTruckingEQ['values'] = sorted(list(txtEditTruckingEQ_List))

        txtEditQuantity_List = [1,2,3,4,5]
        self.txtEditQuantity = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = Quantity, width = 6)
        self.txtEditQuantity.place(x=159,y=398)
        self.txtEditQuantity['values'] = sorted(list(txtEditQuantity_List))

        txtEditShiftHours_List = [12.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00, 20.00]
        self.txtEditShiftHours = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = ShiftHours, width = 8)
        self.txtEditShiftHours.place(x=224,y=398)
        self.txtEditShiftHours['values'] = sorted(list(txtEditShiftHours_List))

        txtEditRateHours_List = [800.00, 650.00, 600.00, 500.00, 450.00, 400.00, 375.00, 100.00]
        self.txtEditRateHours = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = RateHours, width = 10)
        self.txtEditRateHours.place(x=303,y=398)
        self.txtEditRateHours['values'] = sorted(list(txtEditRateHours_List))

        Label_Count_Trucking     = Label(self.root, text = "Entries :", font=("arial", 10,'bold'),bg = "cadet blue").place(x=300,y=105)
        self.txtTruckingEntries  = Entry(self.root, font=('aerial', 10, 'bold'),textvariable = CountTrucking_Entry, width = 4)
        self.txtTruckingEntries.place(x=360,y=105)

        # Equipment Trucking Generated Report Tree View
        DataFrameRIGHT = LabelFrame(self.root, bd = 1, width = 810, height = 420, padx= 1, pady= 1, relief = RIDGE,
                                   bg = "ghost white",font=('aerial', 15, 'bold'))
        DataFrameRIGHT.place(x=410,y=1)

        TruckingREPORT = Frame(DataFrameRIGHT)
        TruckingREPORT.place(x=2,y=30)         
        scrollbary = Scrollbar(TruckingREPORT, orient=VERTICAL)
        tree_TruckingREPORT = ttk.Treeview(TruckingREPORT, column=("column1", "column2", "column3", "column4", "column5",
                                                                     "column6", "column7", "column8"),height=8, show='headings')
        scrollbary.config(command=tree_TruckingREPORT.yview)
        scrollbary.pack(side=RIGHT, fill=Y)   
        tree_TruckingREPORT.heading("#1", text="Trucking Equipment", anchor=W)
        tree_TruckingREPORT.heading("#2", text="Quantity", anchor=W)
        tree_TruckingREPORT.heading("#3", text="Hours", anchor=W)
        tree_TruckingREPORT.heading("#4", text="Rate/Hour", anchor=W)        
        tree_TruckingREPORT.heading("#5", text="Total Cost", anchor=W)
        tree_TruckingREPORT.heading("#6", text="Cost/ShotPoint", anchor=W)
        tree_TruckingREPORT.heading("#7", text="Cost/RecPoint", anchor=W)
        tree_TruckingREPORT.heading("#8", text="Cost/Kilometer", anchor=W)                       

        tree_TruckingREPORT.column('#1', stretch=NO, minwidth=0, width=140)            
        tree_TruckingREPORT.column('#2', stretch=NO, minwidth=0, width=60)
        tree_TruckingREPORT.column('#3', stretch=NO, minwidth=0, width=60)
        tree_TruckingREPORT.column('#4', stretch=NO, minwidth=0, width=70)
        tree_TruckingREPORT.column('#5',stretch=NO, minwidth=0, width=100)
        tree_TruckingREPORT.column('#6',stretch=NO, minwidth=0, width=100)            
        tree_TruckingREPORT.column('#7',stretch=NO, minwidth=0, width=100)
        tree_TruckingREPORT.column('#8',stretch=NO, minwidth=0, width=100)  
        tree_TruckingREPORT.pack()

        self.lblTotalSP_Report = Label(DataFrameRIGHT, text = "Total Planned SP :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=2,y=2)
        self.txtTotalSP_Report= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), state='normal', width = 8, bd=1)
        self.txtTotalSP_Report.place(x=118,y=0)

        self.lblTotalRP_Report = Label(DataFrameRIGHT, text = "Total Planned RP :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=220,y=2)
        self.txtTotalRP_Report= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), state='normal', width = 8, bd=1)
        self.txtTotalRP_Report.place(x=336,y=0)

        self.lblTotalKM_Report = Label(DataFrameRIGHT, text = "Total Linear Kilometers  (km) :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=560,y=2)
        self.txtTotalKM_Report= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), state='normal', width = 7, bd=1)
        self.txtTotalKM_Report.place(x=742,y=0)
        
        self.txtTruckingQuantity= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 6, bd=3)
        self.txtTruckingQuantity.place(x=70,y=220)
        TruckingQuantity = Label(DataFrameRIGHT, text = "Total Qty :", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=0,y=220)

        TruckingSummary = Label(DataFrameRIGHT, text = "Sum Trucking Cost :", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=160,y=220)
        self.txtTotalTruckingCost= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 12, bd=3)
        self.txtTotalTruckingCost.place(x=305,y=220)
        TruckingCost = Label(DataFrameRIGHT, text = "Total Cost", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=320,y=248)

        self.txtTotalTruckingCost_SP= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 12, bd=3)
        self.txtTotalTruckingCost_SP.place(x=415,y=220)
        TruckingCost_SP = Label(DataFrameRIGHT, text = "Total Cost/SP", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=415,y=248)

        self.txtTotalTruckingCost_RP= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 12, bd=3)
        self.txtTotalTruckingCost_RP.place(x=525,y=220)
        TruckingCost_RP = Label(DataFrameRIGHT, text = "Total Cost/RP", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=525,y=248)

        self.txtTotalTruckingCost_KM= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 12, bd=3)
        self.txtTotalTruckingCost_KM.place(x=635,y=220)
        TruckingCost_KM = Label(DataFrameRIGHT, text = "Total Cost/Km", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=635,y=248)

        Label_Currency = Label(DataFrameRIGHT, text = "Currency", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=747,y=248)
        Currency_List = ["CAD", "USD"]
        self.txtCurrency = ttk.Combobox(DataFrameRIGHT, font=('aerial', 10, 'bold'), width = 5)
        self.txtCurrency.place(x=747,y=222)
        self.txtCurrency['values'] = sorted(list(Currency_List))
        self.txtCurrency.current(0)

        Label_Deduct_Add_Percent = Label(self.root, text = "User Add/Deduction Percent (%) :", font=("arial", 9,'bold'),bg = "cadet blue", fg="black").place(x=720,y=423)
        Deduct_Add_List = [0, 10, 15, 20, 25, 30, 35, 40, -10, -15, -20, -25, -30, -35, -40]
        self.txtDeduct_Add = ttk.Combobox(self.root, font=('aerial', 10, 'bold'), width = 5)
        self.txtDeduct_Add.place(x=915,y=423)
        self.txtDeduct_Add['values'] = sorted(list(Deduct_Add_List))
        self.txtDeduct_Add.current(7)


        ## Trucking Generated Report Summary
        Label_TruckingReport_SUMMARY = Label(DataFrameRIGHT, text = "TRUCKING EXPENSE TOTAL SUMMARY :", font=("arial", 10,'bold'),bg = "ghost white", fg="blue").place(x=0,y=284)
        TruckingReport_SUMMARY = Frame(DataFrameRIGHT)
        TruckingReport_SUMMARY.place(x=2,y=307)         
        scrollbary = Scrollbar(TruckingReport_SUMMARY, orient=VERTICAL)
        tree_TruckingReport_SUMMARY = ttk.Treeview(TruckingReport_SUMMARY, column=("column1", "column2", "column3", "column4", "column5",
                                                   "column6"),height=4, show='headings')
        scrollbary.config(command=tree_TruckingReport_SUMMARY.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        tree_TruckingReport_SUMMARY.heading("#1", text="Index", anchor=W)
        tree_TruckingReport_SUMMARY.heading("#2", text="Item Name And Description", anchor=W)
        tree_TruckingReport_SUMMARY.heading("#3", text="Total Trucking Cost", anchor=W)
        tree_TruckingReport_SUMMARY.heading("#4", text="Trucking Cost/SP", anchor=W)        
        tree_TruckingReport_SUMMARY.heading("#5", text="Trucking Cost/RP", anchor=W)
        tree_TruckingReport_SUMMARY.heading("#6", text="Trucking Cost/Km", anchor=W)                
        tree_TruckingReport_SUMMARY.column('#1', stretch=NO, minwidth=0, width=60)            
        tree_TruckingReport_SUMMARY.column('#2', stretch=NO, minwidth=0, width=220)
        tree_TruckingReport_SUMMARY.column('#3', stretch=NO, minwidth=0, width=140)
        tree_TruckingReport_SUMMARY.column('#4', stretch=NO, minwidth=0, width=140)
        tree_TruckingReport_SUMMARY.column('#5',stretch=NO, minwidth=0, width=120)
        tree_TruckingReport_SUMMARY.column('#6',stretch=NO, minwidth=0, width=120)                   
        tree_TruckingReport_SUMMARY.pack()

        ## Tree View Event and Selection And Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", font=('aerial', 9), foreground="black")
        style.configure("Treeview", foreground='black')
        style.configure("Treeview.Heading",font=('aerial', 8,'bold'), background='ghost white', foreground='black',fieldbackground='Ghost White')
        
        def tree_TruckingRec(event):
            for nm in tree_Trucking.selection():
                sd = tree_Trucking.item(nm, 'values')
                self.txtEditTruckingEQ.delete(0,END)
                self.txtEditTruckingEQ.insert(tk.END,sd[0])                
                self.txtEditQuantity.delete(0,END)
                self.txtEditQuantity.insert(tk.END,sd[1])
                self.txtEditShiftHours.delete(0,END)
                self.txtEditShiftHours.insert(tk.END,sd[2])
                self.txtEditRateHours.delete(0,END)
                self.txtEditRateHours.insert(tk.END,sd[3])                              
        tree_Trucking.bind('<<TreeviewSelect>>',tree_TruckingRec)

        ## Connect to Trucking Database        
        conn = sqlite3.connect("EagleBidWidget.db")
        TruckingDF = pd.read_sql_query("SELECT * FROM EagleBidWidget_Trucking_Log ORDER BY `RatePerHour` DESC ;", conn)
        User_Entry  = pd.read_sql_query("SELECT * FROM EagleBidWidget_Trucking_Entry ;", conn)
        TruckingDF = pd.DataFrame(TruckingDF)
        TruckingDF = TruckingDF.reset_index(drop=True)
        User_EntryDF = pd.DataFrame(User_Entry)
        User_EntryDF = User_EntryDF.reset_index(drop=True)
        Length_TruckingDF = len(TruckingDF)
        Length_User_EntryDF = len(User_EntryDF)
        conn.commit()
        conn.close()
        conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
        TruckingDF_Master = pd.read_sql_query("select * from EagleBidWidget_Trucking_Log_Master ;", conn)
        TruckingDF_Master = pd.DataFrame(TruckingDF_Master)
        TruckingDF_Master = TruckingDF_Master.reset_index(drop=True)
        Length_TruckingDF_Master = len(TruckingDF_Master)
        conn.commit()
        conn.close()

        if Length_TruckingDF >0:
            self.txtTruckingEntries.delete(0,END)
            tree_Trucking.delete(*tree_Trucking.get_children())
            for each_rec in range(len(TruckingDF)):
                tree_Trucking.insert("", tk.END, values=list(TruckingDF.loc[each_rec]))
            self.txtTruckingEntries.insert(tk.END,Length_TruckingDF)

        elif Length_TruckingDF_Master >0:
            self.txtTruckingEntries.delete(0,END)
            tree_Trucking.delete(*tree_Trucking.get_children())
            for each_rec in range(len(TruckingDF_Master)):
                tree_Trucking.insert("", tk.END, values=list(TruckingDF_Master.loc[each_rec]))
            self.txtTruckingEntries.insert(tk.END,Length_TruckingDF_Master)
            conn = sqlite3.connect("EagleBidWidget.db")
            TruckingDF_Master.to_sql('EagleBidWidget_Trucking_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

        else:
            MakeTruckingDF = {'TruckingEquipment': ["Equipment Trailers", "Vibe Trucking"],
                              'Quantity': [1,2],
                              'ShiftHour': [16.00,16.00],
                              'RatePerHour': [185.00,200.00]}
            MakeTruckingDF = pd.DataFrame(MakeTruckingDF, columns = ['TruckingEquipment', 'Quantity', 'ShiftHour', 'RatePerHour'])
            MakeTruckingDF = MakeTruckingDF.reset_index(drop=True)
            MakeTruckingDF_Length = len(MakeTruckingDF)
            
            conn = sqlite3.connect("EagleBidWidget.db")
            MakeTruckingDF.to_sql('EagleBidWidget_Trucking_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

            conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
            MakeTruckingDF.to_sql('EagleBidWidget_Trucking_Log_Master',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            
            self.txtTruckingEntries.delete(0,END)
            tree_Trucking.delete(*tree_Trucking.get_children())

            for each_rec in range(len(MakeTruckingDF)):
                tree_Trucking.insert("", tk.END, values=list(MakeTruckingDF.loc[each_rec]))
            
            self.txtTruckingEntries.insert(tk.END,MakeTruckingDF_Length)


        if Length_User_EntryDF >0:
            self.txtTotalSP.delete(0,END)
            self.txtTotalRP.delete(0,END)
            self.txtTotalKM.delete(0,END)
            
            TotalSP_COLUMN = (User_EntryDF['TotalPlannedSP'])
            TotalRP_COLUMN = (User_EntryDF['TotalPlannedRP'])
            TotalKM_COLUMN = (User_EntryDF['TotalLinearKMS'])
                        
            TotalSP_VALUE      = TotalSP_COLUMN[0]
            TotalRP_VALUE      = TotalRP_COLUMN[0]
            TotalKM_VALUE      = TotalKM_COLUMN[0]
            
            self.txtTotalSP.insert(tk.END,TotalSP_VALUE)
            self.txtTotalRP.insert(tk.END,TotalRP_VALUE)
            self.txtTotalKM.insert(tk.END,TotalKM_VALUE)
            
            
        else:
            self.txtTotalSP.delete(0,END)
            self.txtTotalRP.delete(0,END)
            self.txtTotalKM.delete(0,END)     
            self.txtTotalSP.insert(tk.END,0)
            self.txtTotalRP.insert(tk.END,0)
            self.txtTotalKM.insert(tk.END,0.0)
            
        self.txtEditTruckingEQ.delete(0,END)                          
        self.txtEditQuantity.delete(0,END)            
        self.txtEditShiftHours.delete(0,END)            
        self.txtEditRateHours.delete(0,END)


        ## Functions For Trucking Expense Calculation
        def Add_Trucking_LOG():
            TruckingEQ_Length       = (len(self.txtEditTruckingEQ.get()))
            TruckingQuantity_Get    = ((self.txtEditQuantity.get()))
            TruckingShiftHours_Get  = ((self.txtEditShiftHours.get()))
            TruckingRateHours_Get   = ((self.txtEditRateHours.get()))
            if((TruckingEQ_Length)!=0) & ((TruckingQuantity_Get)!=0) & ((TruckingShiftHours_Get)!=0) & ((TruckingRateHours_Get)!=0):
                try:
                    TruckingEQ  = ((self.txtEditTruckingEQ.get()))
                    Quantity    = ((self.txtEditQuantity.get()))
                    ShiftHours  = ((self.txtEditShiftHours.get()))
                    RateHours   = ((self.txtEditRateHours.get()))
                    Eagle_Bid_Database_BackEnd.addRec_Trucking_Log(TruckingEQ, Quantity, ShiftHours, RateHours)
                    DB_UpdateNew_Trucking()
                    tree_Trucking.delete(*tree_Trucking.get_children())
                    for row in Eagle_Bid_Database_BackEnd.viewTrucking_LogData():
                        tree_Trucking.insert("", tk.END, values=row)
                    LB_TruckingEntries()
                except:
                    tkinter.messagebox.showinfo("Add Error","Duplicate Trucking Entry")
            else:
                    tkinter.messagebox.showinfo("Add Error","Entries can not be empty")

        def DB_UpdateNew_Trucking():
            conn = sqlite3.connect("EagleBidWidget.db")
            Complete_df = pd.read_sql_query("SELECT * FROM EagleBidWidget_Trucking_Log ORDER BY `RatePerHour` DESC ;", conn)
            data = pd.DataFrame(Complete_df)
            data ['DuplicatedEntries']=data.sort_values(by =['RatePerHour']).duplicated(['TruckingEquipment'],keep='last')
            data = data.loc[data.DuplicatedEntries == False, 'TruckingEquipment': 'RatePerHour']
            data = data.reset_index(drop=True)
            data.to_sql('EagleBidWidget_Trucking_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
        
        def update_Trucking_LOG():
            TruckingEQ_Length       = (len(self.txtEditTruckingEQ.get()))
            TruckingQuantity_Get    = ((self.txtEditQuantity.get()))
            TruckingShiftHours_Get  = ((self.txtEditShiftHours.get()))
            TruckingRateHours_Get   = ((self.txtEditRateHours.get()))
            if((TruckingEQ_Length)!=0) & ((TruckingQuantity_Get)!=0) & ((TruckingShiftHours_Get)!=0) & ((TruckingRateHours_Get)!=0):
                conn = sqlite3.connect("EagleBidWidget.db")
                cur = conn.cursor()
                for selected_item in tree_Trucking.selection():
                    cur.execute("DELETE FROM EagleBidWidget_Trucking_Log WHERE TruckingEquipment =? AND Quantity =? AND \
                                 ShiftHour =? AND RatePerHour =? ",\
                                (tree_Trucking.set(selected_item, '#1'), tree_Trucking.set(selected_item, '#2'),tree_Trucking.set(selected_item, '#3'),\
                                 tree_Trucking.set(selected_item, '#4'),))
                    conn.commit()
                    tree_Trucking.delete(*tree_Trucking.get_children())
                    conn.close()

            TruckingEQ_Length       = (len(self.txtEditTruckingEQ.get()))
            TruckingQuantity_Get    = ((self.txtEditQuantity.get()))
            TruckingShiftHours_Get  = ((self.txtEditShiftHours.get()))
            TruckingRateHours_Get   = ((self.txtEditRateHours.get()))
            if((TruckingEQ_Length)!=0) & ((TruckingQuantity_Get)!=0) & ((TruckingShiftHours_Get)!=0) & ((TruckingRateHours_Get)!=0):
                TruckingEQ  = ((self.txtEditTruckingEQ.get()))
                Quantity    = ((self.txtEditQuantity.get()))
                ShiftHours  = ((self.txtEditShiftHours.get()))
                RateHours   = ((self.txtEditRateHours.get()))
                Eagle_Bid_Database_BackEnd.addRec_Trucking_Log(TruckingEQ, Quantity, ShiftHours, RateHours)
                tree_Trucking.delete(*tree_Trucking.get_children())
                for row in Eagle_Bid_Database_BackEnd.viewTrucking_LogData():
                    tree_Trucking.insert("", tk.END, values=row)
                LB_TruckingEntries()
            else:
                tkinter.messagebox.showinfo("Update Error","Entries can not be empty")

        def LB_TruckingEntries():
            self.txtTruckingEntries.delete(0,END)
            Total_count = len(tree_Trucking.get_children())
            self.txtTruckingEntries.insert(tk.END,Total_count)

        def Delete_Trucking_LOG():
            SelectionTree = tree_Trucking.selection()
            if len(SelectionTree)>0:
                iDelete = tkinter.messagebox.askyesno("Delete Entry From Trucking Database", "Confirm if you want to Delete From Trucking DataBase")
                if iDelete >0:
                    conn = sqlite3.connect("EagleBidWidget.db")
                    cur = conn.cursor()
                    TruckingEQ_Length       = (len(self.txtEditTruckingEQ.get()))
                    TruckingQuantity_Get    = ((self.txtEditQuantity.get()))
                    TruckingShiftHours_Get  = ((self.txtEditShiftHours.get()))
                    TruckingRateHours_Get   = ((self.txtEditRateHours.get()))
                    if((TruckingEQ_Length)!=0) & ((TruckingQuantity_Get)!=0) & ((TruckingShiftHours_Get)!=0) & ((TruckingRateHours_Get)!=0):
                        for selected_item in tree_Trucking.selection():
                            cur.execute("DELETE FROM EagleBidWidget_Trucking_Log WHERE TruckingEquipment =? AND Quantity =? AND \
                                 ShiftHour =? AND RatePerHour =? ",\
                                (tree_Trucking.set(selected_item, '#1'), tree_Trucking.set(selected_item, '#2'),tree_Trucking.set(selected_item, '#3'),\
                                 tree_Trucking.set(selected_item, '#4'),))
                            conn.commit()
                            tree_Trucking.delete(*tree_Trucking.get_children())
                        conn.commit()
                        conn.close()
                    tree_Trucking.delete(*tree_Trucking.get_children())
                    for row in Eagle_Bid_Database_BackEnd.viewTrucking_LogData():
                        tree_Trucking.insert("", tk.END, values=row)
                    LB_TruckingEntries()
                    return
            else:
                tkinter.messagebox.showinfo("Delete Error","Please Select Entries To Delete From Trucking DB")

        def Load_Trucking_New_Profile():
            tree_Trucking.delete(*tree_Trucking.get_children())
            self.txtTruckingEntries.delete(0,END)
            time.sleep(2)
            self.txtTotalSP.delete(0,END)
            self.txtTotalRP.delete(0,END)
            self.txtTotalKM.delete(0,END)
            
            TotalSP_Default  = int(0)
            TotalKM_Default  = float(0)
            
            User_Entry = {'TotalPlannedSP': [TotalSP_Default], 'TotalLinearKMS': [TotalKM_Default]}

            User_EntryDF = pd.DataFrame(User_Entry, columns = ['TotalPlannedSP', 'TotalLinearKMS'])
            User_EntryDF = User_EntryDF.reset_index(drop=True)
            
            conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
            TruckingDF_Master = pd.read_sql_query("select * from EagleBidWidget_Trucking_Log_Master ORDER BY `RatePerHour` DESC ;", conn)
            TruckingDF_Master = pd.DataFrame(TruckingDF_Master)
            TruckingDF_Master = TruckingDF_Master.reset_index(drop=True)
            Length_TruckingDF_Master = len(TruckingDF_Master)
            conn.commit()
            conn.close()
            
            for each_rec in range(len(TruckingDF_Master)):
                tree_Trucking.insert("", tk.END, values=list(TruckingDF_Master.loc[each_rec]))
            self.txtTruckingEntries.insert(tk.END,Length_TruckingDF_Master)
            conn = sqlite3.connect("EagleBidWidget.db")
            TruckingDF_Master.to_sql('EagleBidWidget_Trucking_Log',conn, if_exists="replace", index=False)
            User_EntryDF.to_sql('EagleBidWidget_Trucking_Entry',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.txtEditTruckingEQ.delete(0,END)                          
            self.txtEditQuantity.delete(0,END)            
            self.txtEditShiftHours.delete(0,END)            
            self.txtEditRateHours.delete(0,END)
            self.txtTotalSP.insert(tk.END,0)
            self.txtTotalRP.insert(tk.END,0)
            self.txtTotalKM.insert(tk.END,0.0)

        def GenTrucking_Clear_Report():
            tree_TruckingREPORT.delete(*tree_TruckingREPORT.get_children())
            tree_TruckingReport_SUMMARY.delete(*tree_TruckingReport_SUMMARY.get_children())
            self.txtTotalSP_Report.delete(0,END)
            self.txtTotalRP_Report.delete(0,END)
            self.txtTotalKM_Report.delete(0,END)
            self.txtTruckingQuantity.delete(0,END)
            self.txtTotalTruckingCost.delete(0,END)
            self.txtTotalTruckingCost_SP.delete(0,END)
            self.txtTotalTruckingCost_RP.delete(0,END)
            self.txtTotalTruckingCost_KM.delete(0,END)


        def Generate_Trucking_Expense():
            GenTrucking_Clear_Report()
            TotalSP_Cal  = int(self.txtTotalSP.get())
            TotalRP_Cal  = int(self.txtTotalRP.get())
            TotalKM_Cal  = float(self.txtTotalKM.get())
            if((TotalSP_Cal)!=0) & ((TotalRP_Cal)!=0) & ((TotalKM_Cal)!=0):
                TotalSP_Cal  = int(self.txtTotalSP.get())
                TotalRP_Cal  = int(self.txtTotalRP.get())
                TotalKM_Cal  = float(self.txtTotalKM.get())
                Currency_Cal = self.txtCurrency.get()
                self.txtTotalSP_Report.insert(tk.END,TotalSP_Cal)
                self.txtTotalRP_Report.insert(tk.END,TotalRP_Cal)
                self.txtTotalKM_Report.insert(tk.END,TotalKM_Cal)

                conn = sqlite3.connect("EagleBidWidget.db")
                TruckingDF_Cal = pd.read_sql_query("SELECT * FROM EagleBidWidget_Trucking_Log ORDER BY `RatePerHour` DESC ;", conn)
                TruckingDF_Cal = pd.DataFrame(TruckingDF_Cal)
                TruckingDF_Cal = TruckingDF_Cal.reset_index(drop=True)

            ## Trucking Expense Report Generating Here
                TruckingDF_Gen = pd.DataFrame(TruckingDF_Cal)
                TruckingDF_Gen = TruckingDF_Gen.reset_index(drop=True)                
                TruckingDF_Gen['TotalCost']      = round((TruckingDF_Gen['Quantity']).mul(TruckingDF_Gen['ShiftHour']).mul(TruckingDF_Gen['RatePerHour']),2)
                TruckingDF_Gen['TotalCostPerSP'] = round((TruckingDF_Gen['TotalCost']).mul(1/TotalSP_Cal),2)
                TruckingDF_Gen['TotalCostPerRP'] = round((TruckingDF_Gen['TotalCost']).mul(1/TotalRP_Cal),2)
                TruckingDF_Gen['TotalCostPerKM'] = round((TruckingDF_Gen['TotalCost']).mul(1/TotalKM_Cal),2)
                TruckingDF_Gen['TotalPlannedSP'] = TruckingDF_Gen.shape[0]*[TotalSP_Cal]
                TruckingDF_Gen['TotalPlannedRP'] = TruckingDF_Gen.shape[0]*[TotalRP_Cal]
                TruckingDF_Gen['TotalLinearKMS'] = TruckingDF_Gen.shape[0]*[TotalKM_Cal]
                TruckingDF_Gen['Currency']       = TruckingDF_Gen.shape[0]*[Currency_Cal]


                TruckingDF_Gen  = TruckingDF_Gen.loc[:,['TruckingEquipment','Quantity','ShiftHour','RatePerHour',
                                                          'TotalCost','TotalCostPerSP', 'TotalCostPerRP', 'TotalCostPerKM',
                                                          'TotalPlannedSP','TotalPlannedRP','TotalLinearKMS','Currency']]
                TruckingDF_Gen = pd.DataFrame(TruckingDF_Gen)
                TruckingDF_Gen = TruckingDF_Gen.reset_index(drop=True)

                TruckingDF_Gen_TreeView  = TruckingDF_Gen.loc[:,['TruckingEquipment','Quantity','ShiftHour','RatePerHour',
                                                                 'TotalCost','TotalCostPerSP', 'TotalCostPerRP', 'TotalCostPerKM']]
                TruckingDF_Gen_TreeView  = pd.DataFrame(TruckingDF_Gen_TreeView)
                TruckingDF_Gen_TreeView  = TruckingDF_Gen_TreeView.reset_index(drop=True)

                for each_rec in range(len(TruckingDF_Gen_TreeView)):
                    tree_TruckingREPORT.insert("", tk.END, values=list(TruckingDF_Gen_TreeView.loc[each_rec]))

                SUM_TruckingDF_Quantity       = round((TruckingDF_Gen_TreeView['Quantity'].sum(axis = 0, skipna = True)),2)
                SUM_TruckingDF_TotalCost      = round((TruckingDF_Gen_TreeView['TotalCost'].sum(axis = 0, skipna = True)),2)
                SUM_TruckingDF_TotalCostPerSP = round((TruckingDF_Gen_TreeView['TotalCostPerSP'].sum(axis = 0, skipna = True)),2)
                SUM_TruckingDF_TotalCostPerRP = round((TruckingDF_Gen_TreeView['TotalCostPerRP'].sum(axis = 0, skipna = True)),2)
                SUM_TruckingDF_TotalCostPerKM = round((TruckingDF_Gen_TreeView['TotalCostPerKM'].sum(axis = 0, skipna = True)),2)
            
                self.txtTruckingQuantity.insert(tk.END,SUM_TruckingDF_Quantity)
                self.txtTotalTruckingCost.insert(tk.END,SUM_TruckingDF_TotalCost)
                self.txtTotalTruckingCost_SP.insert(tk.END,SUM_TruckingDF_TotalCostPerSP)
                self.txtTotalTruckingCost_RP.insert(tk.END,SUM_TruckingDF_TotalCostPerRP)
                self.txtTotalTruckingCost_KM.insert(tk.END,SUM_TruckingDF_TotalCostPerKM)
                
                TruckingDF_Gen['SUMTotalQuantity']  = TruckingDF_Gen.shape[0]*[SUM_TruckingDF_Quantity]
                TruckingDF_Gen['SUMTotalCost']      = TruckingDF_Gen.shape[0]*[SUM_TruckingDF_TotalCost]
                TruckingDF_Gen['SUMTotalCostPerSP'] = TruckingDF_Gen.shape[0]*[SUM_TruckingDF_TotalCostPerSP]
                TruckingDF_Gen['SUMTotalCostPerRP'] = TruckingDF_Gen.shape[0]*[SUM_TruckingDF_TotalCostPerRP]
                TruckingDF_Gen['SUMTotalCostPerKM'] = TruckingDF_Gen.shape[0]*[SUM_TruckingDF_TotalCostPerKM]
                
                TruckingDF_Gen = pd.DataFrame(TruckingDF_Gen)
                TruckingDF_Gen = TruckingDF_Gen.reset_index(drop=True)

                AddDeductPercent_Cal    = float(self.txtDeduct_Add.get())

                Global_Trucking_Summary =    {'ItemIndex'              : [1],
                                              'AddDeductionPercent'    : [AddDeductPercent_Cal],
                                              'TruckingItem'           : ["Total Trucking Equipments Cost"],
                                              'TotalCost'              : [SUM_TruckingDF_TotalCost],
                                              'CostPerSP'              : [SUM_TruckingDF_TotalCostPerSP],
                                              'CostPerRP'              : [SUM_TruckingDF_TotalCostPerRP],
                                              'CostPerKM'              : [SUM_TruckingDF_TotalCostPerKM]}

                Global_Trucking_SummaryDF = pd.DataFrame(Global_Trucking_Summary, columns = ['ItemIndex', 'AddDeductionPercent', 'TruckingItem', 'TotalCost', 'CostPerSP', 'CostPerRP', 'CostPerKM'])
                Global_Trucking_SummaryDF = Global_Trucking_SummaryDF.reset_index(drop=True)               
                conn = sqlite3.connect("EagleBidWidget.db")
                Global_Trucking_SummaryDF.to_sql('EagleBidWidget_Trucking_GLOBAL', conn, if_exists="replace", index=False)

                Global_Trucking_TreeView = Global_Trucking_SummaryDF.loc[:,['ItemIndex','TruckingItem','TotalCost', 'CostPerSP', 'CostPerRP', 'CostPerKM']]
                Global_Trucking_TreeView = pd.DataFrame(Global_Trucking_TreeView)
                Global_Trucking_TreeView = Global_Trucking_TreeView.reset_index(drop=True)
                for each_rec in range(len(Global_Trucking_TreeView)):
                    tree_TruckingReport_SUMMARY.insert("", tk.END, values=list(Global_Trucking_TreeView.loc[each_rec]))

                ## Updating Trucking DB After Finish Calculation
                User_Entry_Cal = {'TotalPlannedSP': [TotalSP_Cal], 'TotalPlannedRP': [TotalRP_Cal], 'TotalLinearKMS': [TotalKM_Cal]}
                User_EntryDF_Cal = pd.DataFrame(User_Entry_Cal, columns = ['TotalPlannedSP', 'TotalPlannedRP', 'TotalLinearKMS'])
                User_EntryDF_Cal = User_EntryDF_Cal.reset_index(drop=True)
                conn = sqlite3.connect("EagleBidWidget.db")
                TruckingDF_Cal.to_sql('EagleBidWidget_Trucking_Log', conn, if_exists="replace", index=False)
                User_EntryDF_Cal.to_sql('EagleBidWidget_Trucking_Entry',conn, if_exists="replace", index=False)
                TruckingDF_Gen.to_sql('EagleBidWidget_Trucking_Expense',conn, if_exists="replace", index=False)
                conn.commit()
                conn.close()
            else:
                tkinter.messagebox.showinfo("Eagle Trucking Equipment Bid Summary Report Message","Please Total SP, RP And KM Entry Can Not Be Empty")

        def Export_Trucking_REPORT():
            Eagle_Bid_Trucking_REPORT.Export_Trucking_Report()


        def Apply_Add_Deduct_Percent():
            AddDeductPercent_Cal    = float(self.txtDeduct_Add.get())
            if((AddDeductPercent_Cal)!=0):
                tree_TruckingReport_SUMMARY.delete(*tree_TruckingReport_SUMMARY.get_children())
                conn = sqlite3.connect("EagleBidWidget.db")
                Global_Trucking_DF = pd.read_sql_query("SELECT * FROM EagleBidWidget_Trucking_GLOBAL ORDER BY `ItemIndex` ASC ;", conn)      
                Global_Trucking_DF = pd.DataFrame(Global_Trucking_DF)
                Global_Trucking_DF = Global_Trucking_DF.reset_index(drop=True)
                AddDeductPercent_Cal    = float(self.txtDeduct_Add.get())
                Global_Trucking_DF['AddDeductionPercent'] = Global_Trucking_DF.shape[0]*[AddDeductPercent_Cal]
                Global_Trucking_DF['TotalCost'] = round(  (Global_Trucking_DF['TotalCost']) + (Global_Trucking_DF['TotalCost']).mul(AddDeductPercent_Cal/100),2)
                Global_Trucking_DF['CostPerSP'] = round(  (Global_Trucking_DF['CostPerSP']) + (Global_Trucking_DF['CostPerSP']).mul(AddDeductPercent_Cal/100),2)
                Global_Trucking_DF['CostPerRP'] = round(  (Global_Trucking_DF['CostPerRP']) + (Global_Trucking_DF['CostPerRP']).mul(AddDeductPercent_Cal/100),2)
                Global_Trucking_DF['CostPerKM'] = round(  (Global_Trucking_DF['CostPerKM']) + (Global_Trucking_DF['CostPerKM']).mul(AddDeductPercent_Cal/100),2)
                Global_Trucking_DF = pd.DataFrame(Global_Trucking_DF)
                Global_Trucking_DF = Global_Trucking_DF.reset_index(drop=True)
                Global_Trucking_DF.to_sql('EagleBidWidget_Trucking_GLOBAL', conn, if_exists="replace", index=False)
                conn.commit()
                conn.close()

                Global_Trucking_TreeView = Global_Trucking_DF.loc[:,['ItemIndex','TruckingItem','TotalCost', 'CostPerSP', 'CostPerRP', 'CostPerKM']]
                Global_Trucking_TreeView = pd.DataFrame(Global_Trucking_TreeView)
                Global_Trucking_TreeView = Global_Trucking_TreeView.reset_index(drop=True)
                for each_rec in range(len(Global_Trucking_TreeView)):
                    tree_TruckingReport_SUMMARY.insert("", tk.END, values=list(Global_Trucking_TreeView.loc[each_rec]))            

        def I_exit():
            self.root.destroy()
            

        ## Command Buttons For Trucking Expense Only
        btnModifyUpdateTrucking_LOG = Button(self.root, text="Update", font=('aerial', 10, 'bold'), height =1, width=6, bd=1, command = update_Trucking_LOG)
        btnModifyUpdateTrucking_LOG.place(x=2,y=422)
        btnDeleteTrucking_LOG = Button(self.root, text="Delete", font=('aerial', 10, 'bold'), height =1, width=6, bd=1, command = Delete_Trucking_LOG)
        btnDeleteTrucking_LOG.place(x=62,y=422)
        btnAdd_Trucking_LOG = Button(self.root, text="Add", font=('aerial', 10, 'bold'), height =1, width=4, bd=1, command = Add_Trucking_LOG)
        btnAdd_Trucking_LOG.place(x=122,y=422)        
        btnLoad_New_Trucking_Profile = Button(self.root, text="Load Deafult", font=('aerial', 10, 'bold'), height =1, width=12, bd=1, command = Load_Trucking_New_Profile)
        btnLoad_New_Trucking_Profile.place(x=168,y=422)        
        btnGenTrucking_Exp_Report = Button(self.root, text="Generate Report", font=('aerial', 10, 'bold'),  height =1, width=13, bd=1, command =Generate_Trucking_Expense)
        btnGenTrucking_Exp_Report.place(x=280,y=422)
        btnTrucking_Clear_Report = Button(self.root, text="Clear Output", font=('aerial', 9, 'bold'),  height =1, width=10, bd=1, command = GenTrucking_Clear_Report)
        btnTrucking_Clear_Report.place(x=323,y=0)
        btnExportReport = Button(self.root, text="Export Report", font=('aerial', 9, 'bold'),  bg='yellow', height =1, width=12, bd=1, command = Export_Trucking_REPORT)
        btnExportReport.place(x=410,y=423)
        btnApply_Percent = Button(self.root, text="Apply Percent", font=('aerial', 9, 'bold'), height =1, width=14, bd=1, command = Apply_Add_Deduct_Percent)
        btnApply_Percent.place(x=976,y=423)        
        btnExit = Button(self.root, text="Exit", font=('aerial', 9, 'bold'), height =1, width=4, bd=1, command = I_exit)
        btnExit.place(x=1184,y=423)



if __name__ == '__main__':
    root = Tk()
    application  = BidEagle_Trucking_Equipment_Expense (root)
    root.mainloop()

