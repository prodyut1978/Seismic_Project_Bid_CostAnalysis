#Front End
import os
from tkinter import*
import tkinter.messagebox
import Eagle_Bid_Database_BackEnd
import Eagle_Bid_Personnel_Equipment_BID_ENTRY
import Eagle_Bid_Personnel_Equipment_REPORT
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

class BidEagle_Personnel_Equipment_Expense:
    
    def __init__(self,root):
        self.root =root
        self.root.title ("Eagle Bid Personnel and Equipment Expenses")
        self.root.geometry("1350x940+0+0")
        self.root.config(bg="cadet blue")
        self.root.resizable(0, 0)

        ## Define Global Variables       
        ShiftHour           = DoubleVar()
        WeatherStandby      = DoubleVar()
        WeatherRate         = DoubleVar()
        StatdayRate         = DoubleVar()
        Crew                = StringVar()
        Province            = StringVar()
        ProvinceTax         = DoubleVar()
        Currency            = StringVar()

        ## Define Personnel Variables  
        Mobilization        = StringVar()
        Weather             = StringVar()
        Personnel           = StringVar()
        CountPerson_Entry   = IntVar()
        Quantity            = IntVar()
        Rate                = DoubleVar()

        ## Define Personnel Variables  
        EQMobilization        = StringVar()
        EQWeather             = StringVar()
        EQEquipment           = StringVar()
        EQCountEquipment_Entry= IntVar()
        EQQuantity            = IntVar()
        EQRate                = DoubleVar()

        ## Global Frame For Personnel And Equipment

        DataFrameGLOBAL = LabelFrame(self.root, bd = 1, width = 1350, height = 68, padx= 1, pady= 1, relief = RIDGE,
                                   bg = "lightgreen",font=('aerial', 15, 'bold'))
        DataFrameGLOBAL.place(x=0,y=864)
        LabelGlobalPersonnel_Equip = Label(DataFrameGLOBAL, text = "COST CALCULATION - PERSONNEL AND EQUIPMENT : ", font=("arial", 11,'bold'), bg = "lightgreen", fg="black").place(x=0,y=0)


        TotalDailyCostPerDay = Label(DataFrameGLOBAL, text = "Total Cost/Day", font=("arial", 11,'bold'),bg = "lightgreen", fg="black").place(x=455,y=0)
        self.txtTotalDailyCostPerDay= Entry(DataFrameGLOBAL, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtTotalDailyCostPerDay.place(x=455,y=27)

        TotalDailyCostPerHour = Label(DataFrameGLOBAL, text = "Total Cost/Hour", font=("arial", 11,'bold'),bg = "lightgreen", fg="black").place(x=595,y=0)
        self.txtTotalDailyCostPerHour= Entry(DataFrameGLOBAL, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtTotalDailyCostPerHour.place(x=595,y=27)

        TotalMobCostPerDay = Label(DataFrameGLOBAL, text = "Total Mob/Day", font=("arial", 11,'bold'),bg = "lightgreen", fg="black").place(x=735,y=0)
        self.txtTotalMobCostPerDay= Entry(DataFrameGLOBAL, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtTotalMobCostPerDay.place(x=735,y=27)

        TotalMobCostPerHour = Label(DataFrameGLOBAL, text = "Total Mob/Hour", font=("arial", 11,'bold'),bg = "lightgreen", fg="black").place(x=875,y=0)
        self.txtTotalMobCostPerHour= Entry(DataFrameGLOBAL, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtTotalMobCostPerHour.place(x=875,y=27)

        TotalWeatherCostPerHour = Label(DataFrameGLOBAL, text = "Total Weather/Hour", font=("arial", 11,'bold'),bg = "lightgreen", fg="black").place(x=1030,y=0)
        self.txtTotalWeatherCostPerHour= Entry(DataFrameGLOBAL, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtTotalWeatherCostPerHour.place(x=1040,y=27)

        TotalStatCostPerHour = Label(DataFrameGLOBAL, text = "Total StatDay/Hour", font=("arial", 11,'bold'),bg = "lightgreen", fg="black").place(x=1203,y=0)
        self.txtTotalStatCostPerHour= Entry(DataFrameGLOBAL, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtTotalStatCostPerHour.place(x=1213,y=27)

        
        # ENTRY FOR PERSONNEL BID EXPENSE CALCULATION
        Label_DataFrameLEFT = Label(self.root, text = "PERSONNEL VARIABLES :", font=("arial", 10,'bold'),bg = "cadet blue", fg="blue").place(x=2,y=2)
        DataFrameLEFT = LabelFrame(self.root, bd = 1, width = 520, height = 450, padx= 1, pady= 1, relief = RIDGE,
                                   bg = "cadet blue",font=('aerial', 15, 'bold'))
        DataFrameLEFT.place(x=2,y=25)

        ShiftHour_List = [12.0,13.0,14.0,11.0,10.0,24.0,22.0,20.0]
        self.lblShiftHour = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "1. Shift Hours :    ", padx =1, pady= 2, bg = "cadet blue")
        self.lblShiftHour.grid(row =0, column = 0, sticky =W)
        self.txtShiftHour = ttk.Combobox(DataFrameLEFT, font=('aerial', 9, 'bold'), width = 6)
        self.txtShiftHour.grid(row =0, column = 1)
        self.txtShiftHour['values'] = sorted(list(ShiftHour_List))
        #self.txtShiftHour.current(3)

        WeatherStandby_List = [12.0,13.0,14.0,11.0,10.0]
        self.lblWeatherStandby = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "2. Weather Hours :    ", padx =1, pady= 4, bg = "cadet blue")
        self.lblWeatherStandby.grid(row =1, column = 0, sticky =W)
        self.txtWeatherStandby = ttk.Combobox(DataFrameLEFT, font=('aerial', 9, 'bold'), width = 6)
        self.txtWeatherStandby.grid(row =1, column = 1)
        self.txtWeatherStandby['values'] = sorted(list(WeatherStandby_List))
        #self.txtWeatherStandby.current(2)
        
        WeatherRate_List = [100.0,95.0,90.0,85.0,80.0,75.0,70.0]
        self.lblWeatherRate = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "3. Weather Rate (%) :", padx =19, pady= 2, bg = "cadet blue")
        self.lblWeatherRate.grid(row =0, column = 3, sticky =W)
        self.txtWeatherRate = ttk.Combobox(DataFrameLEFT, font=('aerial', 9, 'bold'), width = 6)
        self.txtWeatherRate.grid(row =0, column = 4)
        self.txtWeatherRate['values'] = sorted(list(WeatherRate_List))
        #self.txtWeatherRate.current(6)

        StatdayRate_List = [100.0,95.0,90.0,85.0,80.0,75.0,70.0]
        self.lblStatdayRate = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "4. Stat Rate (%) :", padx =19, pady= 4, bg = "cadet blue")
        self.lblStatdayRate.grid(row =1, column = 3, sticky =W)
        self.txtStatdayRate = ttk.Combobox(DataFrameLEFT, font=('aerial', 9, 'bold'), width = 6)
        self.txtStatdayRate.grid(row =1, column = 4)
        self.txtStatdayRate['values'] = sorted(list(StatdayRate_List))
        #self.txtStatdayRate.current(2)

        # ######################################## END OF ENTRY FOR PERSONNEL BID EXPENSE CALCULATION  ##################################

        # ######################################## PERSONNEL BID EXPENSE CALCULATION  ################################## 

        DataFrameRIGHT = LabelFrame(self.root, bd = 1, width = 889, height = 460, padx= 1, pady= 1, relief = RIDGE,
                                   bg = "ghost white",font=('aerial', 15, 'bold'))
        DataFrameRIGHT.place(x=460,y=1)
        
        PersonnelShiftHOUR = Label(DataFrameRIGHT, text = "Shift Hour :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=2,y=0)
        self.txtPersonnelShiftHOUR= Entry(DataFrameRIGHT, font=('aerial', 9, 'bold'), state='normal', width = 4, bd=1)
        self.txtPersonnelShiftHOUR.place(x=73,y=0)

        PersonnelWeatherHOUR = Label(DataFrameRIGHT, text = "Weather Hour:", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=150,y=0)
        self.txtPersonnelWeatherHOUR= Entry(DataFrameRIGHT, font=('aerial', 9, 'bold'), width = 4, bd=1)
        self.txtPersonnelWeatherHOUR.place(x=240,y=0)
        PersonnelWeatherRATE = Label(DataFrameRIGHT, text = "-  Rate (%) :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=276,y=0)
        self.txtPersonnelWeatherRATE= Entry(DataFrameRIGHT, font=('aerial', 9, 'bold'), width = 6, bd=1)
        self.txtPersonnelWeatherRATE.place(x=348,y=0)


        PersonnelMobRate_List = [100.0,95.0,90.0,85.0,80.0,75.0,70.0]
        PersonnelMobRate = Label(DataFrameRIGHT, text = "Mob Rate (%) :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=440,y=0)
        self.txtPersonnelMobRATE= ttk.Combobox(DataFrameRIGHT, font=('aerial', 9, 'bold'), width = 6)
        self.txtPersonnelMobRATE.place(x=532,y=0)
        self.txtPersonnelMobRATE['values'] = sorted(list(PersonnelMobRate_List))
        self.txtPersonnelMobRATE.current(6)

        PersonnelStatRate = Label(DataFrameRIGHT, text = "Stat Rate (%) :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=730,y=0)
        self.txtPersonnelStatRATE= Entry(DataFrameRIGHT, font=('aerial', 9, 'bold'), width = 6, bd=1)
        self.txtPersonnelStatRATE.place(x=820,y=0)


        PersonnelQuantity = Label(DataFrameRIGHT, text = "Qty", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=4,y=408)
        self.txtPersonnelQuantity= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 4, bd=3)
        self.txtPersonnelQuantity.place(x=0,y=429)

        PersonnelCostPerDay = Label(DataFrameRIGHT, text = "Personnel Cost/Day", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=70,y=408)
        self.txtPersonnelCostPerDay= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtPersonnelCostPerDay.place(x=75,y=429)

        PersonnelCostPerHour = Label(DataFrameRIGHT, text = "Personnel Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=195,y=408)
        self.txtPersonnelCostPerHour= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtPersonnelCostPerHour.place(x=200,y=429)

        MobCostPerDay = Label(DataFrameRIGHT, text = "Mob Cost/Day", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=335,y=408)
        self.txtMobCostPerDay= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtMobCostPerDay.place(x=325,y=429)

        MobCostPerHour = Label(DataFrameRIGHT, text = "Mob Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=461,y=408)
        self.txtMobCostPerHour= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtMobCostPerHour.place(x=451,y=429)

        WeatherCostPerHour = Label(DataFrameRIGHT, text = "Weather Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=581,y=408)
        self.txtWeatherCostPerHour= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtWeatherCostPerHour.place(x=575,y=429)

        StatCostPerHour = Label(DataFrameRIGHT, text = "StatDay Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=705,y=408)
        self.txtStatCostPerHour= Entry(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtStatCostPerHour.place(x=698,y=429)

        Label_Currency = Label(DataFrameRIGHT, text = "Currency", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=823,y=408)
        Currency_List = ["CAD", "USD"]
        self.txtCurrency = ttk.Combobox(DataFrameRIGHT, font=('aerial', 11, 'bold'), width = 4)
        self.txtCurrency.place(x=828,y=429)
        self.txtCurrency['values'] = sorted(list(Currency_List))
        self.txtCurrency.current(0)

        PersonnelREPORT = Frame(DataFrameRIGHT)
        PersonnelREPORT.place(x=2,y=22)         
        scrollbary = Scrollbar(PersonnelREPORT, orient=VERTICAL)
        tree_PersonnelREPORT = ttk.Treeview(PersonnelREPORT, column=("column1", "column2", "column3", "column4", "column5",
                                                                     "column6", "column7", "column8", "column9", "column10", "column11"),height=18, show='headings')
        scrollbary.config(command=tree_PersonnelREPORT.yview)
        scrollbary.pack(side=RIGHT, fill=Y)   
        tree_PersonnelREPORT.heading("#1", text="Mob", anchor=W)
        tree_PersonnelREPORT.heading("#2", text="Weather", anchor=W)
        tree_PersonnelREPORT.heading("#3", text="Personnel", anchor=W)
        tree_PersonnelREPORT.heading("#4", text="Qty", anchor=W)
        tree_PersonnelREPORT.heading("#5", text="Rate/Person", anchor=W)
        tree_PersonnelREPORT.heading("#6", text="Cost/Day", anchor=W)
        tree_PersonnelREPORT.heading("#7", text="Cost/Hour", anchor=W)
        tree_PersonnelREPORT.heading("#8", text="Mob/Day", anchor=W)
        tree_PersonnelREPORT.heading("#9", text="Mob/Hour", anchor=W)
        tree_PersonnelREPORT.heading("#10", text="Weather/Hour", anchor=W)
        tree_PersonnelREPORT.heading("#11", text="Stat/Hour", anchor=W)                    
        tree_PersonnelREPORT.column('#1', stretch=NO, minwidth=0, width=40)            
        tree_PersonnelREPORT.column('#2', stretch=NO, minwidth=0, width=60)
        tree_PersonnelREPORT.column('#3', stretch=NO, minwidth=0, width=150)
        tree_PersonnelREPORT.column('#4', stretch=NO, minwidth=0, width=45)
        tree_PersonnelREPORT.column('#5', stretch=NO, minwidth=0, width=90)
        tree_PersonnelREPORT.column('#6', stretch=NO, minwidth=0, width=80)            
        tree_PersonnelREPORT.column('#7', stretch=NO, minwidth=0, width=85)
        tree_PersonnelREPORT.column('#8', stretch=NO, minwidth=0, width=70)
        tree_PersonnelREPORT.column('#9', stretch=NO, minwidth=0, width=70)
        tree_PersonnelREPORT.column('#10', stretch=NO, minwidth=0, width=95)
        tree_PersonnelREPORT.column('#11', stretch=NO, minwidth=0, width=75)
        tree_PersonnelREPORT.pack()

        # Tree View Personnel Expense Frames-------------
        Label_TableMargin_Personnel = Label(self.root, text = "PERSONNEL PROFILE :", font=("arial", 10,'bold'),bg = "cadet blue", fg="blue").place(x=2,y=82)
        TableMargin_Personnel = Frame(self.root)
        TableMargin_Personnel.place(x=2,y=104)         
        scrollbary = Scrollbar(TableMargin_Personnel, orient=VERTICAL)
        tree_Personnel = ttk.Treeview(TableMargin_Personnel, column=("column1", "column2", "column3", "column4", "column5"),
                            height=14, show='headings')
        scrollbary.config(command=tree_Personnel.yview)
        scrollbary.pack(side=RIGHT, fill=Y)   
        tree_Personnel.heading("#1", text="Mobilization", anchor=W)
        tree_Personnel.heading("#2", text="Weather", anchor=W)
        tree_Personnel.heading("#3", text="Crew Personnel", anchor=W)
        tree_Personnel.heading("#4", text="Quantity", anchor=W)
        tree_Personnel.heading("#5", text="Rate/Day", anchor=W)                    
        tree_Personnel.column('#1', stretch=NO, minwidth=0, width=75)            
        tree_Personnel.column('#2', stretch=NO, minwidth=0, width=60)
        tree_Personnel.column('#3', stretch=NO, minwidth=0, width=140)
        tree_Personnel.column('#4', stretch=NO, minwidth=0, width=65)
        tree_Personnel.column('#5', stretch=NO, minwidth=0, width=80)

        txtEditMob_List = ["Y", "N"]
        self.txtEditMob = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = Mobilization, width = 6)
        self.txtEditMob.place(x=2,y=413)
        self.txtEditMob['values'] = sorted(list(txtEditMob_List))

        txtEditWx_List = ["Y", "N"]
        self.txtEditWx = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = Weather, width = 6)
        self.txtEditWx.place(x=68,y=413)
        self.txtEditWx['values'] = sorted(list(txtEditWx_List))

        txtEditPersonnel_List = ["Party Manager","Assist.Party Manager","Field Service Tech","Merge Operator","FMC Operator","Mechanic","HSE Advisor","Administrator","Co-ordinator",
                                 "Shooters","Shooter's Helpers","Vibrator Technician","Vibrator Operators","Fuel Driver","Trouble Shooters/Viewers","Line Boss","Recorder Helpers",
                                 "Staging Helpers","Night Watchman","Rotation"]
        self.txtEditPersonnel = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = Personnel, width = 18)
        self.txtEditPersonnel.place(x=134,y=413)
        self.txtEditPersonnel['values'] = sorted(list(txtEditPersonnel_List))

        txtEditQuantity_List = [1,2,3,4,5]
        self.txtEditQuantity = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = Quantity, width = 6)
        self.txtEditQuantity.place(x=285,y=413)
        self.txtEditQuantity['values'] = sorted(list(txtEditQuantity_List))

        txtEditRate_List = [800.00, 650.00, 600.00, 500.00, 450.00, 400.00, 375.00, 100.00]
        self.txtEditRate = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = Rate, width = 10)
        self.txtEditRate.place(x=352,y=413)
        self.txtEditRate['values'] = sorted(list(txtEditRate_List))

        Label_Count_Personnel     = Label(self.root, text = "Entries :", font=("arial", 10,'bold'),bg = "cadet blue").place(x=353,y=82)
        self.txtPersonnelEntries  = Entry(self.root, font=('aerial', 10, 'bold'),textvariable = CountPerson_Entry, width = 4)
        self.txtPersonnelEntries.place(x=410,y=82)

        # Tree View Personnel Event and Selection
        def tree_PersonnelRec(event):
            for nm in tree_Personnel.selection():
                sd = tree_Personnel.item(nm, 'values')
                self.txtEditMob.delete(0,END)
                self.txtEditMob.insert(tk.END,sd[0])                
                self.txtEditWx.delete(0,END)
                self.txtEditWx.insert(tk.END,sd[1])
                self.txtEditPersonnel.delete(0,END)
                self.txtEditPersonnel.insert(tk.END,sd[2])
                self.txtEditQuantity.delete(0,END)
                self.txtEditQuantity.insert(tk.END,sd[3])
                self.txtEditRate.delete(0,END)
                self.txtEditRate.insert(tk.END,sd[4])                
        tree_Personnel.pack()
        tree_Personnel.bind('<<TreeviewSelect>>',tree_PersonnelRec)

        ## Connect to crew personnel Database        
        conn = sqlite3.connect("EagleBidWidget.db")
        PersonnalDF = pd.read_sql_query("SELECT * FROM EagleBidWidget_Personnal_Log ORDER BY `Rate` DESC ;", conn)
        User_Entry  = pd.read_sql_query("SELECT * FROM EagleBidWidget_Personnal_Entry ;", conn)
        PersonnalDF = pd.DataFrame(PersonnalDF)
        PersonnalDF = PersonnalDF.reset_index(drop=True)
        User_EntryDF = pd.DataFrame(User_Entry)
        User_EntryDF = User_EntryDF.reset_index(drop=True)
        Length_PersonnalDF = len(PersonnalDF)
        Length_User_EntryDF = len(User_EntryDF)
        conn.commit()
        conn.close()
        conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
        PersonnalDF_Master = pd.read_sql_query("select * from EagleBidWidget_Personnal_Log_Master ORDER BY `Rate` DESC ;", conn)
        PersonnalDF_Master = pd.DataFrame(PersonnalDF_Master)
        PersonnalDF_Master = PersonnalDF_Master.reset_index(drop=True)
        Length_PersonnalDF_Master = len(PersonnalDF_Master)
        conn.commit()
        conn.close()

        if Length_PersonnalDF >0:
            self.txtPersonnelEntries.delete(0,END)
            tree_Personnel.delete(*tree_Personnel.get_children())
            for each_rec in range(len(PersonnalDF)):
                tree_Personnel.insert("", tk.END, values=list(PersonnalDF.loc[each_rec]))
            self.txtPersonnelEntries.insert(tk.END,Length_PersonnalDF)

        elif Length_PersonnalDF_Master >0:
            self.txtPersonnelEntries.delete(0,END)
            tree_Personnel.delete(*tree_Personnel.get_children())
            for each_rec in range(len(PersonnalDF_Master)):
                tree_Personnel.insert("", tk.END, values=list(PersonnalDF_Master.loc[each_rec]))
            self.txtPersonnelEntries.insert(tk.END,Length_PersonnalDF_Master)
            conn = sqlite3.connect("EagleBidWidget.db")
            PersonnalDF_Master.to_sql('EagleBidWidget_Personnal_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

        else:
            MakePersonnelDF = {'Mobilization': ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                           'Weather': ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                           'Personnel': ["Party Manager","Assist.Party Manager","Field Service Tech","Merge Operator","FMC Operator","Mechanic","HSE Advisor","Administrator","Co-ordinator",
                                         "Shooters","Shooter's Helpers","Vibrator Technician","Vibrator Operators","Fuel Driver","Trouble Shooters/Viewers","Line Boss","Recorder Helpers",
                                         "Staging Helpers","Night Watchman","Rotation"],
                           'Quantity': [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
                           'Rate': [800.00,650.00,650.00,650.00,600.00,600.00,600.00,450.00,500.00,450.00,400.00,600.00,450.00,450.00,450.00,450.00,375.00,375.00,400.00,100.00]}
            MakePersonnelDF = pd.DataFrame(MakePersonnelDF, columns = ['Mobilization', 'Weather', 'Personnel', 'Quantity','Rate'])
            MakePersonnelDF = MakePersonnelDF.reset_index(drop=True)
            MakePersonnelDF_Length = len(MakePersonnelDF)
            
            conn = sqlite3.connect("EagleBidWidget.db")
            MakePersonnelDF.to_sql('EagleBidWidget_Personnal_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

            conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
            MakePersonnelDF.to_sql('EagleBidWidget_Personnal_Log_Master',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            
            self.txtPersonnelEntries.delete(0,END)
            tree_Personnel.delete(*tree_Personnel.get_children())

            for row in Eagle_Bid_Database_BackEnd.viewPersonnal_LogData():
                tree_Personnel.insert("", tk.END, values=row)
            
            self.txtPersonnelEntries.insert(tk.END,MakePersonnelDF_Length)


        if Length_User_EntryDF >0:
            self.txtShiftHour.delete(0,END)
            self.txtWeatherStandby.delete(0,END)
            self.txtWeatherRate.delete(0,END)
            self.txtStatdayRate.delete(0,END)
            ShiftHour_COLUMN = (User_EntryDF['ShiftHour'])
            WeatherStandby_COLUMN = (User_EntryDF['WeatherStandby'])
            WeatherRate_COLUMN = (User_EntryDF['WeatherRate'])
            StatdayRate_COLUMN = (User_EntryDF['StatdayRate'])
            
            ShiftHour_VALUE      = ShiftHour_COLUMN[0]
            WeatherStandby_VALUE = WeatherStandby_COLUMN[0]
            WeatherRate_VALUE    = WeatherRate_COLUMN[0]
            StatdayRate_VALUE    = StatdayRate_COLUMN[0]

            self.txtShiftHour.insert(tk.END,ShiftHour_VALUE)
            self.txtWeatherStandby.insert(tk.END,WeatherStandby_VALUE)
            self.txtWeatherRate.insert(tk.END,WeatherRate_VALUE)
            self.txtStatdayRate.insert(tk.END,StatdayRate_VALUE)
            
        else:
            self.txtShiftHour.delete(0,END)
            self.txtWeatherStandby.delete(0,END)
            self.txtWeatherRate.delete(0,END)
            self.txtStatdayRate.delete(0,END)
            self.txtShiftHour.current(3)
            self.txtWeatherStandby.current(2)
            self.txtWeatherRate.current(6)
            self.txtStatdayRate.current(2)

        self.txtEditMob.delete(0,END)                          
        self.txtEditWx.delete(0,END)            
        self.txtEditPersonnel.delete(0,END)            
        self.txtEditQuantity.delete(0,END)            
        self.txtEditRate.delete(0,END)

### --------------------------------------------------------------#####------------------------------------------------------------------------------------------------------------------


        # ENTRY FOR EQUIPMENT BID EXPENSE CALCULATION
        Label_DataFrameBOTTOM = Label(self.root, text = "EQUIPMENT VARIABLES :", font=("arial", 10,'bold'),bg = "cadet blue", fg="blue").place(x=2,y=473)
        Label_DataFrameBOTTOM = LabelFrame(self.root, bd = 1, width = 520, height = 450, padx= 1, pady= 1, relief = RIDGE,
                                   bg = "cadet blue",font=('aerial', 15, 'bold'))
        Label_DataFrameBOTTOM.place(x=2,y=496)

        EQShiftHour_List = [12.0,13.0,14.0,11.0,10.0,24.0,22.0,20.0]
        self.lblShiftHourEQ = Label(Label_DataFrameBOTTOM, font=('aerial', 10, 'bold'), text = "1. Shift Hours :    ", padx =1, pady= 2, bg = "cadet blue")
        self.lblShiftHourEQ.grid(row =0, column = 0, sticky =W)
        self.txtShiftHourEQ = ttk.Combobox(Label_DataFrameBOTTOM, font=('aerial', 9, 'bold'), width = 6)
        self.txtShiftHourEQ.grid(row =0, column = 1)
        self.txtShiftHourEQ['values'] = sorted(list(EQShiftHour_List))
        #self.txtShiftHour.current(3)

        EQWeatherStandby_List = [12.0,13.0,14.0,11.0,10.0]
        self.lblWeatherStandbyEQ = Label(Label_DataFrameBOTTOM, font=('aerial', 10, 'bold'), text = "2. Weather Hours :    ", padx =1, pady= 4, bg = "cadet blue")
        self.lblWeatherStandbyEQ.grid(row =1, column = 0, sticky =W)
        self.txtWeatherStandbyEQ = ttk.Combobox(Label_DataFrameBOTTOM, font=('aerial', 9, 'bold'), width = 6)
        self.txtWeatherStandbyEQ.grid(row =1, column = 1)
        self.txtWeatherStandbyEQ['values'] = sorted(list(EQWeatherStandby_List))
        #self.txtWeatherStandby.current(2)
        
        EQWeatherRate_List = [100.0,95.0,90.0,85.0,80.0,75.0,70.0]
        self.lblWeatherRateEQ = Label(Label_DataFrameBOTTOM, font=('aerial', 10, 'bold'), text = "3. Weather Rate (%) :", padx =19, pady= 2, bg = "cadet blue")
        self.lblWeatherRateEQ.grid(row =0, column = 3, sticky =W)
        self.txtWeatherRateEQ = ttk.Combobox(Label_DataFrameBOTTOM, font=('aerial', 9, 'bold'), width = 6)
        self.txtWeatherRateEQ.grid(row =0, column = 4)
        self.txtWeatherRateEQ['values'] = sorted(list(EQWeatherRate_List))
        #self.txtWeatherRate.current(6)

        EQStatdayRate_List = [100.0,95.0,90.0,85.0,80.0,75.0,70.0]
        self.lblStatdayRateEQ = Label(Label_DataFrameBOTTOM, font=('aerial', 10, 'bold'), text = "4. Stat Rate (%) :", padx =19, pady= 4, bg = "cadet blue")
        self.lblStatdayRateEQ.grid(row =1, column = 3, sticky =W)
        self.txtStatdayRateEQ = ttk.Combobox(Label_DataFrameBOTTOM, font=('aerial', 9, 'bold'), width = 6)
        self.txtStatdayRateEQ.grid(row =1, column = 4)
        self.txtStatdayRateEQ['values'] = sorted(list(EQStatdayRate_List))
        #self.txtStatdayRate.current(2)



        # ########################################  EQUIPMENT BID EXPENSE CALCULATION  ################################## 

        DataFrameRIGHTBOTTOM = LabelFrame(self.root, bd = 4, width = 889, height = 390, padx= 1, pady= 1, relief = RIDGE,
                                   bg = "ghost white",font=('aerial', 15, 'bold'))
        DataFrameRIGHTBOTTOM.place(x=460,y=470)
        
        EquipmentShiftHOUR = Label(DataFrameRIGHTBOTTOM, text = "Shift Hour :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=2,y=0)
        self.txtEquipmentShiftHOUR= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 9, 'bold'), width = 4, bd=1)
        self.txtEquipmentShiftHOUR.place(x=73,y=0)

        EquipmentWeatherHOUR = Label(DataFrameRIGHTBOTTOM, text = "Weather Hour:", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=150,y=0)
        self.txtEquipmentWeatherHOUR= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 9, 'bold'), width = 4, bd=1)
        self.txtEquipmentWeatherHOUR.place(x=240,y=0)
        EquipmentWeatherRATE = Label(DataFrameRIGHTBOTTOM, text = "-  Rate (%) :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=276,y=0)
        self.txtEquipmentWeatherRATE= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 9, 'bold'), width = 6, bd=1)
        self.txtEquipmentWeatherRATE.place(x=348,y=0)

        EquipmentMobRate_List = [100.0,95.0,90.0,85.0,80.0,75.0,70.0]
        EquipmentMobRate = Label(DataFrameRIGHTBOTTOM, text = "Mob Rate (%) :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=440,y=0)
        self.txtEquipmentMobRATE= ttk.Combobox(DataFrameRIGHTBOTTOM, font=('aerial', 9, 'bold'), width = 6)
        self.txtEquipmentMobRATE.place(x=532,y=0)
        self.txtEquipmentMobRATE['values'] = sorted(list(EquipmentMobRate_List))
        self.txtEquipmentMobRATE.current(6)

        EquipmentStatRate = Label(DataFrameRIGHTBOTTOM, text = "Stat Rate (%) :", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=730,y=0)
        self.txtEquipmentStatRATE= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 9, 'bold'), width = 6, bd=1)
        self.txtEquipmentStatRATE.place(x=820,y=0)

        EquipmentQuantity = Label(DataFrameRIGHTBOTTOM, text = "Item", font=("arial", 10,'bold'),bg = "ghost white", fg="black").place(x=4,y=332)
        self.txtEquipmentQuantity= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 4, bd=3)
        self.txtEquipmentQuantity.place(x=0,y=354)

        EquipmentCostPerDay = Label(DataFrameRIGHTBOTTOM, text = "Equipment Cost/Day", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=70,y=332)
        self.txtEquipmentCostPerDay= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtEquipmentCostPerDay.place(x=75,y=354)

        EquipmentCostPerHour = Label(DataFrameRIGHTBOTTOM, text = "Equipment Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=195,y=332)
        self.txtEquipmentCostPerHour= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtEquipmentCostPerHour.place(x=200,y=354)

        EquipmentMobCostPerDay = Label(DataFrameRIGHTBOTTOM, text = "Mob Cost/Day", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=335,y=332)
        self.txtEquipmentMobCostPerDay= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtEquipmentMobCostPerDay.place(x=325,y=354)

        EquipmentMobCostPerHour = Label(DataFrameRIGHTBOTTOM, text = "Mob Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=461,y=332)
        self.txtEquipmentMobCostPerHour= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtEquipmentMobCostPerHour.place(x=451,y=354)

        EquipmentWeatherCostPerHour = Label(DataFrameRIGHTBOTTOM, text = "Weather Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=581,y=332)
        self.txtEquipmentWeatherCostPerHour= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtEquipmentWeatherCostPerHour.place(x=575,y=354)

        EquipmentStatCostPerHour = Label(DataFrameRIGHTBOTTOM, text = "StatDay Cost/Hour", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=705,y=332)
        self.txtEquipmentStatCostPerHour= Entry(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 14, bd=3)
        self.txtEquipmentStatCostPerHour.place(x=698,y=354)

        EquipmentLabel_Currency = Label(DataFrameRIGHTBOTTOM, text = "Currency", font=("arial", 9,'bold'),bg = "ghost white", fg="black").place(x=823,y=332)
        EquipmentCurrency_List = ["CAD", "USD"]
        self.txtEquipmentCurrency = ttk.Combobox(DataFrameRIGHTBOTTOM, font=('aerial', 11, 'bold'), width = 4)
        self.txtEquipmentCurrency.place(x=828,y=354)
        self.txtEquipmentCurrency['values'] = sorted(list(EquipmentCurrency_List))
        self.txtEquipmentCurrency.current(0)

        EquipmentREPORT = Frame(DataFrameRIGHTBOTTOM)
        EquipmentREPORT.place(x=2,y=22)         
        scrollbary = Scrollbar(EquipmentREPORT, orient=VERTICAL)
        tree_EquipmentREPORT = ttk.Treeview(EquipmentREPORT, column=("column1", "column2", "column3", "column4", "column5",
                                                                     "column6", "column7", "column8", "column9", "column10", "column11"),height=14, show='headings')
        scrollbary.config(command=tree_EquipmentREPORT.yview)
        scrollbary.pack(side=RIGHT, fill=Y)   
        tree_EquipmentREPORT.heading("#1", text="Mob", anchor=W)
        tree_EquipmentREPORT.heading("#2", text="Weather", anchor=W)
        tree_EquipmentREPORT.heading("#3", text="Equipment", anchor=W)
        tree_EquipmentREPORT.heading("#4", text="Qty", anchor=W)
        tree_EquipmentREPORT.heading("#5", text="Rate/Unit", anchor=W)
        tree_EquipmentREPORT.heading("#6", text="Cost/Day", anchor=W)
        tree_EquipmentREPORT.heading("#7", text="Cost/Hour", anchor=W)
        tree_EquipmentREPORT.heading("#8", text="Mob/Day", anchor=W)
        tree_EquipmentREPORT.heading("#9", text="Mob/Hour", anchor=W)
        tree_EquipmentREPORT.heading("#10", text="Weather/Hour", anchor=W)
        tree_EquipmentREPORT.heading("#11", text="Stat/Hour", anchor=W)                    
        tree_EquipmentREPORT.column('#1', stretch=NO, minwidth=0, width=40)            
        tree_EquipmentREPORT.column('#2', stretch=NO, minwidth=0, width=60)
        tree_EquipmentREPORT.column('#3', stretch=NO, minwidth=0, width=150)
        tree_EquipmentREPORT.column('#4', stretch=NO, minwidth=0, width=45)
        tree_EquipmentREPORT.column('#5', stretch=NO, minwidth=0, width=90)
        tree_EquipmentREPORT.column('#6', stretch=NO, minwidth=0, width=80)            
        tree_EquipmentREPORT.column('#7', stretch=NO, minwidth=0, width=85)
        tree_EquipmentREPORT.column('#8', stretch=NO, minwidth=0, width=70)
        tree_EquipmentREPORT.column('#9', stretch=NO, minwidth=0, width=70)
        tree_EquipmentREPORT.column('#10', stretch=NO, minwidth=0, width=95)
        tree_EquipmentREPORT.column('#11', stretch=NO, minwidth=0, width=75)
        tree_EquipmentREPORT.pack()

        # Tree View Equipment Expense Frames-------------
        Label_TableMargin_Equipment = Label(self.root, text = "EQUIPMENT PROFILE :", font=("arial", 10,'bold'),bg = "cadet blue", fg="blue").place(x=2,y=555)
        TableMargin_Equipment = Frame(self.root)
        TableMargin_Equipment.place(x=2,y=578) 
        scrollbary = Scrollbar(TableMargin_Equipment, orient=VERTICAL)
        tree_Equipment = ttk.Treeview(TableMargin_Equipment, column=("column1", "column2", "column3", "column4", "column5"),
                            height=10, show='headings')
        scrollbary.config(command=tree_Equipment.yview)
        scrollbary.pack(side=RIGHT, fill=Y)   
        tree_Equipment.heading("#1", text="Mobilization", anchor=W)
        tree_Equipment.heading("#2", text="Weather", anchor=W)
        tree_Equipment.heading("#3", text="Equipment/Subsistance", anchor=W)
        tree_Equipment.heading("#4", text="Quantity", anchor=W)
        tree_Equipment.heading("#5", text="Rate/Unit", anchor=W)            
        tree_Equipment.column('#1', stretch=NO, minwidth=0, width=75)            
        tree_Equipment.column('#2', stretch=NO, minwidth=0, width=60)
        tree_Equipment.column('#3', stretch=NO, minwidth=0, width=140)
        tree_Equipment.column('#4', stretch=NO, minwidth=0, width=65)
        tree_Equipment.column('#5', stretch=NO, minwidth=0, width=80)
        

        txtEquipmentEditMob_List = ["Y", "N"]
        self.txtEquipmentEditMob = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = EQMobilization, width = 6)
        self.txtEquipmentEditMob.place(x=2,y=807)
        self.txtEquipmentEditMob['values'] = sorted(list(txtEquipmentEditMob_List))

        txtEquipmentEditWx_List = ["Y", "N"]
        self.txtEquipmentEditWx = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = EQWeather, width = 6)
        self.txtEquipmentEditWx.place(x=68,y=807)
        self.txtEquipmentEditWx['values'] = sorted(list(txtEquipmentEditWx_List))

        txtEQEquipment_List = ["Rental Recording System","Rental Geophone","Personal Trucks","Tapes\Supplies","Equipment R&M","Fleet R&M","Fuel - Recording","Fuel - Vibes","One Time Cost",
                                 "Subsistence","Motel-Crew Office","Motel - Single Rooms","Motel - Double Rooms"]
        self.txtEQEquipment = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = EQEquipment, width = 18)
        self.txtEQEquipment.place(x=134,y=807)
        self.txtEQEquipment['values'] = sorted(list(txtEQEquipment_List))

        txtEQQuantity_List = [1,2,3,4,5]
        self.txtEQQuantity = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = EQQuantity, width = 6)
        self.txtEQQuantity.place(x=285,y=807)
        self.txtEQQuantity['values'] = sorted(list(txtEQQuantity_List))

        txtEQRate_List = [800.00, 650.00, 600.00, 500.00, 450.00, 400.00, 375.00, 100.00]
        self.txtEQRate = ttk.Combobox(self.root, font=('aerial', 9, 'bold'), state = "normal", textvariable = EQRate, width = 10)
        self.txtEQRate.place(x=352,y=807)
        self.txtEQRate['values'] = sorted(list(txtEQRate_List))

        Label_Count_EQ     = Label(self.root, text = "Entries :", font=("arial", 10,'bold'),bg = "cadet blue").place(x=353,y=555)
        self.txtEquipmentEntries  = Entry(self.root, font=('aerial', 10, 'bold'),textvariable = EQCountEquipment_Entry, width = 4)
        self.txtEquipmentEntries.place(x=410,y=555)


        # Tree View Equipment Event and Selection
        def tree_EquipmentRec(event):
            for nm in tree_Equipment.selection():
                sd = tree_Equipment.item(nm, 'values')
                self.txtEquipmentEditMob.delete(0,END)
                self.txtEquipmentEditMob.insert(tk.END,sd[0])                
                self.txtEquipmentEditWx.delete(0,END)
                self.txtEquipmentEditWx.insert(tk.END,sd[1])
                self.txtEQEquipment.delete(0,END)
                self.txtEQEquipment.insert(tk.END,sd[2])
                self.txtEQQuantity.delete(0,END)
                self.txtEQQuantity.insert(tk.END,sd[3])
                self.txtEQRate.delete(0,END)
                self.txtEQRate.insert(tk.END,sd[4])                
        tree_Equipment.pack()
        tree_Equipment.bind('<<TreeviewSelect>>',tree_EquipmentRec)


        ## Connect to crew Equipment Database        
        conn = sqlite3.connect("EagleBidWidget.db")
        EquipmentDF = pd.read_sql_query("SELECT * FROM EagleBidWidget_Equipment_Log ORDER BY `Rate` DESC ;", conn)
        EquipmentUser_Entry  = pd.read_sql_query("SELECT * FROM EagleBidWidget_Equipment_Entry ;", conn)
        EquipmentDF = pd.DataFrame(EquipmentDF)
        EquipmentDF = EquipmentDF.reset_index(drop=True)
        EquipmentUser_EntryDF = pd.DataFrame(EquipmentUser_Entry)
        EquipmentUser_EntryDF = EquipmentUser_EntryDF.reset_index(drop=True)
        Length_EquipmentDF = len(EquipmentDF)
        Length_EquipmentUser_EntryDF = len(EquipmentUser_EntryDF)
        conn.commit()
        conn.close()
        conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
        EquipmentDF_Master = pd.read_sql_query("select * from EagleBidWidget_Equipment_Log_Master ORDER BY `Rate` DESC ;", conn)
        EquipmentDF_Master = pd.DataFrame(EquipmentDF_Master)
        EquipmentDF_Master = EquipmentDF_Master.reset_index(drop=True)
        Length_EquipmentDF_Master = len(EquipmentDF_Master)
        conn.commit()
        conn.close()

        if Length_EquipmentDF >0:
            self.txtEquipmentEntries.delete(0,END)
            tree_Equipment.delete(*tree_Equipment.get_children())
            for each_rec in range(len(EquipmentDF)):
                tree_Equipment.insert("", tk.END, values=list(EquipmentDF.loc[each_rec]))
            self.txtEquipmentEntries.insert(tk.END,Length_EquipmentDF)

        elif Length_EquipmentDF_Master >0:
            self.txtEquipmentEntries.delete(0,END)
            tree_Equipment.delete(*tree_Equipment.get_children())
            for each_rec in range(len(EquipmentDF_Master)):
                tree_Equipment.insert("", tk.END, values=list(EquipmentDF_Master.loc[each_rec]))
            self.txtEquipmentEntries.insert(tk.END,Length_EquipmentDF_Master)
            conn = sqlite3.connect("EagleBidWidget.db")
            EquipmentDF_Master.to_sql('EagleBidWidget_Equipment_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

        else:
            MakeEquipmentDF = {'Mobilization':    ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                               'Weather':         ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                               'Equipment': ["Rental Recording System", "Rental Geophone", "Rental Box Unit (3C)", "Rental Box Unit (1C)", "Rental Box Battery", "Rental Blaster",
                                         "Personal Trucks", "Tapes\Supplies", "Equipment R&M", "Fleet R&M", "Fuel - Recording", "Fuel - Vibes",
                                         "One Time Cost", "Subsistence", "Motel-Crew Office", "Motel - Single Rooms", "Motel - Double Rooms"],
                               'Quantity': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               'Rate':     [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 110.0, 500.0, 1000.0, 1000.0, 150.0, 400.0, 1.0, 50.0, 125.0, 125.0, 125.0]}
            MakeEquipmentDF = pd.DataFrame(MakeEquipmentDF, columns = ['Mobilization', 'Weather', 'Equipment', 'Quantity','Rate'])
            MakeEquipmentDF = MakeEquipmentDF.reset_index(drop=True)
            MakeEquipmentDF_Length = len(MakeEquipmentDF)
            
            conn = sqlite3.connect("EagleBidWidget.db")
            MakeEquipmentDF.to_sql('EagleBidWidget_Equipment_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

            conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
            MakeEquipmentDF.to_sql('EagleBidWidget_Equipment_Log_Master',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            
            self.txtEquipmentEntries.delete(0,END)
            tree_Equipment.delete(*tree_Equipment.get_children())

            for row in Eagle_Bid_Database_BackEnd.viewEquipment_LogData():
                tree_Equipment.insert("", tk.END, values=row)
            
            self.txtEquipmentEntries.insert(tk.END,MakeEquipmentDF_Length)


        if Length_EquipmentUser_EntryDF >0:
            self.txtShiftHourEQ.delete(0,END)
            self.txtWeatherStandbyEQ.delete(0,END)
            self.txtWeatherRateEQ.delete(0,END)
            self.txtStatdayRateEQ.delete(0,END)
            EQShiftHour_COLUMN      = (EquipmentUser_EntryDF['ShiftHour'])
            EQWeatherStandby_COLUMN = (EquipmentUser_EntryDF['WeatherStandby'])
            EQWeatherRate_COLUMN    = (EquipmentUser_EntryDF['WeatherRate'])
            EQStatdayRate_COLUMN    = (EquipmentUser_EntryDF['StatdayRate'])
            
            EQShiftHour_VALUE      = EQShiftHour_COLUMN[0]
            EQWeatherStandby_VALUE = EQWeatherStandby_COLUMN[0]
            EQWeatherRate_VALUE    = EQWeatherRate_COLUMN[0]
            EQStatdayRate_VALUE    = EQStatdayRate_COLUMN[0]

            self.txtShiftHourEQ.insert(tk.END,EQShiftHour_VALUE)
            self.txtWeatherStandbyEQ.insert(tk.END,EQWeatherStandby_VALUE)
            self.txtWeatherRateEQ.insert(tk.END,EQWeatherRate_VALUE)
            self.txtStatdayRateEQ.insert(tk.END,EQStatdayRate_VALUE)
            
        else:
            self.txtShiftHourEQ.delete(0,END)
            self.txtWeatherStandbyEQ.delete(0,END)
            self.txtWeatherRateEQ.delete(0,END)
            self.txtStatdayRateEQ.delete(0,END)
            self.txtShiftHourEQ.current(3)
            self.txtWeatherStandbyEQ.current(2)
            self.txtWeatherRateEQ.current(6)
            self.txtStatdayRateEQ.current(2)

        self.txtEquipmentEditMob.delete(0,END)                          
        self.txtEquipmentEditWx.delete(0,END)            
        self.txtEQEquipment.delete(0,END)            
        self.txtEQQuantity.delete(0,END)            
        self.txtEQRate.delete(0,END)


        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", font=('aerial', 9), foreground="black")
        style.configure("Treeview", foreground='black')
        style.configure("Treeview.Heading",font=('aerial', 8,'bold'), background='ghost white', foreground='black',fieldbackground='Ghost White')



        ############################################## FUNCTIONS DEFINE FOR EQUIPMENT AND EXPENSE CALCULATION  #######################
      ## Functions For Personnel And Expense Calculation

        def Add_Personnel_LOG():
            Len_Mob       = (len(self.txtEditMob.get()))
            Len_Weather   = (len(self.txtEditWx.get()))
            Len_Personnel = (len(self.txtEditPersonnel.get()))
            QuantityGet   = ((self.txtEditQuantity.get()))
            RateGet       = ((self.txtEditRate.get()))
            if((Len_Mob)!=0) & ((Len_Weather)!=0) & ((Len_Personnel)!=0) & ((QuantityGet)!=0) & ((RateGet)!=0):
                try:
                    Mobilization       = ((self.txtEditMob.get()))
                    Weather            = ((self.txtEditWx.get()))
                    Personnel          = ((self.txtEditPersonnel.get()))
                    Quantity           = ((self.txtEditQuantity.get()))
                    Rate               = ((self.txtEditRate.get()))
                    Eagle_Bid_Database_BackEnd.addRec_Personnal_Log(Mobilization, Weather, Personnel, Quantity, Rate)
                    DB_UpdateNew_Personnel()
                    tree_Personnel.delete(*tree_Personnel.get_children())
                    for row in Eagle_Bid_Database_BackEnd.viewPersonnal_LogData():
                        tree_Personnel.insert("", tk.END, values=row)
                    LB_PersonnelEntries()
                except:
                    tkinter.messagebox.showinfo("Add Error","Duplicate Personnel Entry")
            else:
                    tkinter.messagebox.showinfo("Add Error","Mobilization, Weather, Personnel, Quantity, Rate entry can not be empty")



        def Add_Equipment_LOG():
            Len_EQMobilization = (len(self.txtEquipmentEditMob.get()))
            Len_EQWeather      = (len(self.txtEquipmentEditWx.get()))
            Len_EQEquipment    = (len(self.txtEQEquipment.get()))
            EQQuantityGet      = ((self.txtEQQuantity.get()))
            EQRateGet          = ((self.txtEQRate.get()))            
            if((Len_EQMobilization)!=0) & ((Len_EQWeather)!=0) & ((Len_EQEquipment)!=0) & ((EQQuantityGet) !=0) & ((EQRateGet)!=0):
                try:
                    EQMobilization  = ((self.txtEquipmentEditMob.get()))
                    EQWeather       = ((self.txtEquipmentEditWx.get()))
                    EQEquipment     = ((self.txtEQEquipment.get()))
                    EQQuantity      = ((self.txtEQQuantity.get()))
                    EQRate          = ((self.txtEQRate.get()))
                    Eagle_Bid_Database_BackEnd.addRec_Equipment_Log(EQMobilization, EQWeather, EQEquipment, EQQuantity, EQRate)
                    DB_UpdateNew_Equipment()
                    tree_Equipment.delete(*tree_Equipment.get_children())
                    for row in Eagle_Bid_Database_BackEnd.viewEquipment_LogData():
                        tree_Equipment.insert("", tk.END, values=row)
                    LB_EquipmentEntries()
                except:
                    tkinter.messagebox.showinfo("Add Error","Duplicate Equipment Entry")
            else:
                    tkinter.messagebox.showinfo("Add Error","Mobilization, Weather, Equipment, Quantity, Rate entry can not be empty")


        def DB_UpdateNew_Personnel():
            conn = sqlite3.connect("EagleBidWidget.db")
            Complete_df = pd.read_sql_query("SELECT * FROM EagleBidWidget_Personnal_Log ORDER BY `Rate` DESC ;", conn)
            data = pd.DataFrame(Complete_df)
            data ['DuplicatedEntries']=data.sort_values(by =['Rate']).duplicated(['Personnel'],keep='last')
            data = data.loc[data.DuplicatedEntries == False, 'Mobilization': 'Rate']
            data = data.reset_index(drop=True)
            data.to_sql('EagleBidWidget_Personnal_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

        def DB_UpdateNew_Equipment():
            conn = sqlite3.connect("EagleBidWidget.db")
            Complete_df = pd.read_sql_query("SELECT * FROM EagleBidWidget_Equipment_Log ORDER BY `Rate` DESC ;", conn)
            data = pd.DataFrame(Complete_df)
            data ['DuplicatedEntries']=data.sort_values(by =['Rate']).duplicated(['Equipment'],keep='last')
            data = data.loc[data.DuplicatedEntries == False, 'Mobilization': 'Rate']
            data = data.reset_index(drop=True)
            data.to_sql('EagleBidWidget_Equipment_Log',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
        
        def update_Personnel_LOG():
            Len_Mob       = (len(self.txtEditMob.get()))
            Len_Weather   = (len(self.txtEditWx.get()))
            Len_Personnel = (len(self.txtEditPersonnel.get()))
            QuantityGet   = ((self.txtEditQuantity.get()))
            RateGet       = ((self.txtEditRate.get()))
            if((Len_Mob)!=0) & ((Len_Weather)!=0) & ((Len_Personnel)!=0) & ((QuantityGet)!=0) & ((RateGet)!=0):
                conn = sqlite3.connect("EagleBidWidget.db")
                cur = conn.cursor()
                for selected_item in tree_Personnel.selection():
                    cur.execute("DELETE FROM EagleBidWidget_Personnal_Log WHERE Mobilization =? AND Weather =? AND \
                                 Personnel =? AND Quantity =? AND Rate =? ",\
                                (tree_Personnel.set(selected_item, '#1'), tree_Personnel.set(selected_item, '#2'),tree_Personnel.set(selected_item, '#3'),\
                                 tree_Personnel.set(selected_item, '#4'),tree_Personnel.set(selected_item, '#5'),))
                    conn.commit()
                    tree_Personnel.delete(selected_item)
                    conn.close()


            Len_Mob       = (len(self.txtEditMob.get()))
            Len_Weather   = (len(self.txtEditWx.get()))
            Len_Personnel = (len(self.txtEditPersonnel.get()))
            QuantityGet   = ((self.txtEditQuantity.get()))
            RateGet       = ((self.txtEditRate.get()))
            if((Len_Mob)!=0) & ((Len_Weather)!=0) & ((Len_Personnel)!=0) & ((QuantityGet)!=0) & ((RateGet)!=0):
                Mobilization       = ((self.txtEditMob.get()))
                Weather            = ((self.txtEditWx.get()))
                Personnel          = ((self.txtEditPersonnel.get()))
                Quantity           = ((self.txtEditQuantity.get()))
                Rate               = ((self.txtEditRate.get()))
                Eagle_Bid_Database_BackEnd.addRec_Personnal_Log(Mobilization, Weather, Personnel, Quantity, Rate)
                tree_Personnel.delete(*tree_Personnel.get_children())
                for row in Eagle_Bid_Database_BackEnd.viewPersonnal_LogData():
                    tree_Personnel.insert("", tk.END, values=row)
                LB_PersonnelEntries()
            else:
                tkinter.messagebox.showinfo("Update Error","Mobilization, Weather, Personnel, Quantity, Rate entry can not be empty")


        def update_Equipment_LOG():
            Len_EQMobilization = (len(self.txtEquipmentEditMob.get()))
            Len_EQWeather      = (len(self.txtEquipmentEditWx.get()))
            Len_EQEquipment    = (len(self.txtEQEquipment.get()))
            EQQuantityGet      = ((self.txtEQQuantity.get()))
            EQRateGet          = ((self.txtEQRate.get()))            
            if((Len_EQMobilization)!=0) & ((Len_EQWeather)!=0) & ((Len_EQEquipment)!=0) & ((EQQuantityGet) !=0) & ((EQRateGet)!=0):
                conn = sqlite3.connect("EagleBidWidget.db")
                cur = conn.cursor()
                for selected_item in tree_Equipment.selection():
                    cur.execute("DELETE FROM EagleBidWidget_Equipment_Log WHERE Mobilization =? AND Weather =? AND \
                                 Equipment =? AND Quantity =? AND Rate =? ",\
                                (tree_Equipment.set(selected_item, '#1'), tree_Equipment.set(selected_item, '#2'),tree_Equipment.set(selected_item, '#3'),\
                                 tree_Equipment.set(selected_item, '#4'),tree_Equipment.set(selected_item, '#5'),))
                    conn.commit()
                    tree_Equipment.delete(selected_item)
                    conn.close()

            Len_EQMobilization = (len(self.txtEquipmentEditMob.get()))
            Len_EQWeather      = (len(self.txtEquipmentEditWx.get()))
            Len_EQEquipment    = (len(self.txtEQEquipment.get()))
            EQQuantityGet      = ((self.txtEQQuantity.get()))
            EQRateGet          = ((self.txtEQRate.get()))            
            if((Len_EQMobilization)!=0) & ((Len_EQWeather)!=0) & ((Len_EQEquipment)!=0) & ((EQQuantityGet) !=0) & ((EQRateGet)!=0):
                EQMobilization  = ((self.txtEquipmentEditMob.get()))
                EQWeather       = ((self.txtEquipmentEditWx.get()))
                EQEquipment     = ((self.txtEQEquipment.get()))
                EQQuantity      = ((self.txtEQQuantity.get()))
                EQRate          = ((self.txtEQRate.get()))
                Eagle_Bid_Database_BackEnd.addRec_Equipment_Log(EQMobilization, EQWeather, EQEquipment, EQQuantity, EQRate)
                tree_Equipment.delete(*tree_Equipment.get_children())
                for row in Eagle_Bid_Database_BackEnd.viewEquipment_LogData():
                    tree_Equipment.insert("", tk.END, values=row)
                LB_EquipmentEntries()
            else:
                tkinter.messagebox.showinfo("Update Error","Mobilization, Weather, Equipment, Quantity, Rate entry can not be empty")

        def Delete_Personnel_LOG():
            SelectionTree = tree_Personnel.selection()
            if len(SelectionTree)>0:
                iDelete = tkinter.messagebox.askyesno("Delete Entry From Personnel Database", "Confirm if you want to Delete From Personnel DataBase")
                if iDelete >0:
                    conn = sqlite3.connect("EagleBidWidget.db")
                    cur = conn.cursor()
                    Len_Mob       = (len(self.txtEditMob.get()))
                    Len_Weather   = (len(self.txtEditWx.get()))
                    Len_Personnel = (len(self.txtEditPersonnel.get()))
                    QuantityGet   = ((self.txtEditQuantity.get()))
                    RateGet       = ((self.txtEditRate.get()))
                    if((Len_Mob)!=0) & ((Len_Weather)!=0) & ((Len_Personnel)!=0) & ((QuantityGet)!=0) & ((RateGet)!=0):
                        for selected_item in tree_Personnel.selection():
                            cur.execute("DELETE FROM EagleBidWidget_Personnal_Log WHERE Mobilization =? AND Weather =? AND \
                                         Personnel =? AND Quantity =? AND Rate =? ",\
                                        (tree_Personnel.set(selected_item, '#1'), tree_Personnel.set(selected_item, '#2'),tree_Personnel.set(selected_item, '#3'),\
                                         tree_Personnel.set(selected_item, '#4'),tree_Personnel.set(selected_item, '#5'),))
                            conn.commit()
                            tree_Personnel.delete(selected_item)
                        conn.commit()
                        conn.close()
                    tree_Personnel.delete(*tree_Personnel.get_children())
                    for row in Eagle_Bid_Database_BackEnd.viewPersonnal_LogData():
                        tree_Personnel.insert("", tk.END, values=row)
                    LB_PersonnelEntries()
                    return
            else:
                tkinter.messagebox.showinfo("Delete Error","Please Select Entries To Delete From Personnel DB")

        def Delete_Equipment_LOG():
            SelectionTree = tree_Equipment.selection()
            if len(SelectionTree)>0:
                iDelete = tkinter.messagebox.askyesno("Delete Entry From Equipment Database", "Confirm if you want to Delete From Equipment DataBase")
                if iDelete >0:
                    conn = sqlite3.connect("EagleBidWidget.db")
                    cur = conn.cursor()
                    Len_EQMobilization = (len(self.txtEquipmentEditMob.get()))
                    Len_EQWeather      = (len(self.txtEquipmentEditWx.get()))
                    Len_EQEquipment    = (len(self.txtEQEquipment.get()))
                    EQQuantityGet      = ((self.txtEQQuantity.get()))
                    EQRateGet          = ((self.txtEQRate.get()))
                    if((Len_EQMobilization)!=0) & ((Len_EQWeather)!=0) & ((Len_EQEquipment)!=0) & ((EQQuantityGet) !=0) & ((EQRateGet)!=0):
                        for selected_item in tree_Equipment.selection():
                            cur.execute("DELETE FROM EagleBidWidget_Equipment_Log WHERE Mobilization =? AND Weather =? AND \
                                         Equipment =? AND Quantity =? AND Rate =? ",\
                                        (tree_Equipment.set(selected_item, '#1'), tree_Equipment.set(selected_item, '#2'),tree_Equipment.set(selected_item, '#3'),\
                                         tree_Equipment.set(selected_item, '#4'),tree_Equipment.set(selected_item, '#5'),))
                            conn.commit()
                            tree_Equipment.delete(selected_item)
                        conn.commit()
                        conn.close()
                    tree_Equipment.delete(*tree_Equipment.get_children())
                    for row in Eagle_Bid_Database_BackEnd.viewEquipment_LogData():
                        tree_Equipment.insert("", tk.END, values=row)
                    LB_EquipmentEntries()
                    return
            else:
                tkinter.messagebox.showinfo("Delete Error","Please Select Entries To Delete From Equipment DB")
        
        def LB_PersonnelEntries():
            self.txtPersonnelEntries.delete(0,END)
            Total_count = len(tree_Personnel.get_children())
            self.txtPersonnelEntries.insert(tk.END,Total_count)


        def LB_EquipmentEntries():
            self.txtEquipmentEntries.delete(0,END)
            Total_count = len(tree_Equipment.get_children())
            self.txtEquipmentEntries.insert(tk.END,Total_count)


        def Load_Personnel_New_Profile():
            tree_Personnel.delete(*tree_Personnel.get_children())
            self.txtPersonnelEntries.delete(0,END)
            time.sleep(2)
            self.txtShiftHour.delete(0,END)
            self.txtWeatherStandby.delete(0,END)
            self.txtWeatherRate.delete(0,END)
            self.txtStatdayRate.delete(0,END)
            self.txtShiftHour.current(3)
            self.txtWeatherStandby.current(2)
            self.txtWeatherRate.current(6)
            self.txtStatdayRate.current(2)
            
            ShiftHour_Default      = float(self.txtShiftHour.get())
            WeatherStandby_Default = float(self.txtWeatherStandby.get())
            WeatherRate_Default    = float(self.txtWeatherRate.get())
            StatdayRate_Default    = float(self.txtStatdayRate.get())
            User_Entry = {'ShiftHour': [ShiftHour_Default], 'WeatherStandby': [WeatherStandby_Default],
                          'WeatherRate': [WeatherRate_Default], 'StatdayRate': [StatdayRate_Default]}

            User_EntryDF = pd.DataFrame(User_Entry, columns = ['ShiftHour', 'WeatherStandby', 'WeatherRate', 'StatdayRate'])
            User_EntryDF = User_EntryDF.reset_index(drop=True)
            
            conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
            PersonnalDF_Master = pd.read_sql_query("select * from EagleBidWidget_Personnal_Log_Master ORDER BY `Rate` DESC ;", conn)
            PersonnalDF_Master = pd.DataFrame(PersonnalDF_Master)
            PersonnalDF_Master = PersonnalDF_Master.reset_index(drop=True)
            Length_PersonnalDF_Master = len(PersonnalDF_Master)
            conn.commit()
            conn.close()
            
            for each_rec in range(len(PersonnalDF_Master)):
                tree_Personnel.insert("", tk.END, values=list(PersonnalDF_Master.loc[each_rec]))
            self.txtPersonnelEntries.insert(tk.END,Length_PersonnalDF_Master)
            conn = sqlite3.connect("EagleBidWidget.db")
            PersonnalDF_Master.to_sql('EagleBidWidget_Personnal_Log',conn, if_exists="replace", index=False)
            User_EntryDF.to_sql('EagleBidWidget_Personnal_Entry',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            self.txtEditMob.delete(0,END)                          
            self.txtEditWx.delete(0,END)            
            self.txtEditPersonnel.delete(0,END)            
            self.txtEditQuantity.delete(0,END)            
            self.txtEditRate.delete(0,END)


        def Load_Equipment_New_Profile():
            tree_Equipment.delete(*tree_Equipment.get_children())
            self.txtEquipmentEntries.delete(0,END)
            time.sleep(2)
            
            self.txtShiftHourEQ.delete(0,END)
            self.txtWeatherStandbyEQ.delete(0,END)
            self.txtWeatherRateEQ.delete(0,END)
            self.txtStatdayRateEQ.delete(0,END)
            
            self.txtShiftHourEQ.current(3)
            self.txtWeatherStandbyEQ.current(2)
            self.txtWeatherRateEQ.current(6)
            self.txtStatdayRateEQ.current(2)
            
            ShiftHour_Default      = float(self.txtShiftHourEQ.get())
            WeatherStandby_Default = float(self.txtWeatherStandbyEQ.get())
            WeatherRate_Default    = float(self.txtWeatherRateEQ.get())
            StatdayRate_Default    = float(self.txtStatdayRateEQ.get())
            User_Entry = {'ShiftHour': [ShiftHour_Default], 'WeatherStandby': [WeatherStandby_Default],
                          'WeatherRate': [WeatherRate_Default], 'StatdayRate': [StatdayRate_Default]}

            User_EntryDF = pd.DataFrame(User_Entry, columns = ['ShiftHour', 'WeatherStandby', 'WeatherRate', 'StatdayRate'])
            User_EntryDF = User_EntryDF.reset_index(drop=True)
            
            conn = sqlite3.connect("EagleBidWidgetMasterBackup.db")
            EquipmentDF_Master = pd.read_sql_query("select * from EagleBidWidget_Equipment_Log_Master ORDER BY `Rate` DESC ;", conn)
            EquipmentDF_Master = pd.DataFrame(EquipmentDF_Master)
            EquipmentDF_Master = EquipmentDF_Master.reset_index(drop=True)
            Length_EquipmentDF_Master = len(EquipmentDF_Master)
            conn.commit()
            conn.close()
            
            for each_rec in range(len(EquipmentDF_Master)):
                tree_Equipment.insert("", tk.END, values=list(EquipmentDF_Master.loc[each_rec]))
            self.txtEquipmentEntries.insert(tk.END,Length_EquipmentDF_Master)
            conn = sqlite3.connect("EagleBidWidget.db")
            EquipmentDF_Master.to_sql('EagleBidWidget_Equipment_Log',conn, if_exists="replace", index=False)
            User_EntryDF.to_sql('EagleBidWidget_Equipment_Entry',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
            
            self.txtEquipmentEditMob.delete(0,END)                          
            self.txtEquipmentEditWx.delete(0,END)            
            self.txtEQEquipment.delete(0,END)            
            self.txtEQQuantity.delete(0,END)            
            self.txtEQRate.delete(0,END)

        def Generate_Personnel_Expense():
            tree_PersonnelREPORT.delete(*tree_PersonnelREPORT.get_children())
            self.txtPersonnelShiftHOUR.delete(0,END)
            self.txtPersonnelWeatherHOUR.delete(0,END)
            self.txtPersonnelWeatherRATE.delete(0,END)
            self.txtPersonnelStatRATE.delete(0,END)
            self.txtPersonnelQuantity.delete(0,END)
            self.txtPersonnelCostPerDay.delete(0,END)
            self.txtPersonnelCostPerHour.delete(0,END)
            self.txtMobCostPerDay.delete(0,END)
            self.txtMobCostPerHour.delete(0,END)
            self.txtWeatherCostPerHour.delete(0,END)
            self.txtStatCostPerHour.delete(0,END)

            ShiftHour_Cal          = float(self.txtShiftHour.get())
            WeatherStandby_Cal     = float(self.txtWeatherStandby.get())
            WeatherRate_Cal        = float(self.txtWeatherRate.get())
            StatdayRate_Cal        = float(self.txtStatdayRate.get())
            PersonnelMobRATE_Cal   = float(self.txtPersonnelMobRATE.get())
            PersonnelCurrency_Cal  = (self.txtCurrency.get())

            self.txtPersonnelShiftHOUR.insert(tk.END,ShiftHour_Cal)
            self.txtPersonnelWeatherHOUR.insert(tk.END,WeatherStandby_Cal)
            self.txtPersonnelWeatherRATE.insert(tk.END,WeatherRate_Cal)
            self.txtPersonnelStatRATE.insert(tk.END,StatdayRate_Cal)
            
            conn = sqlite3.connect("EagleBidWidget.db")
            PersonnalDF_Cal = pd.read_sql_query("SELECT * FROM EagleBidWidget_Personnal_Log ORDER BY `Rate` DESC ;", conn)
            PersonnalDF_Cal = pd.DataFrame(PersonnalDF_Cal)
            PersonnalDF_Cal = PersonnalDF_Cal.reset_index(drop=True)

            ## Personnel Expense Report Generating Here
            PersonnalDF_Gen = pd.DataFrame(PersonnalDF_Cal)
            PersonnalDF_Gen = PersonnalDF_Gen.reset_index(drop=True)

            PersonnalDF_Gen['PersonnelCostPerDay']  = PersonnalDF_Gen['Rate'].mul(PersonnalDF_Gen['Quantity'])
            PersonnalDF_Gen['PersonnelCostPerHour'] = round(PersonnalDF_Gen['PersonnelCostPerDay'].mul(1/ShiftHour_Cal),2)


            def trans_Mobilization_PerDay(y):
                if y == "Y":
                    return (PersonnelMobRATE_Cal/100)

                elif y == "Yes":
                    return (PersonnelMobRATE_Cal/100)

                elif y == "y":
                    return (PersonnelMobRATE_Cal/100)

                elif y == "yes":
                    return (PersonnelMobRATE_Cal/100)

                elif y == "YES":
                    return (PersonnelMobRATE_Cal/100)

                elif y == "N":
                    return 0.0

                elif y == "No":
                    return 0.0

                elif y == "NO":
                    return 0.0

                elif y == "no":
                    return 0.0

                else:
                    return (float(y)*(PersonnelMobRATE_Cal/100))

            PersonnalDF_Gen['MobCostPerDay_X'] = PersonnalDF_Gen['Mobilization'].apply(trans_Mobilization_PerDay)
            PersonnalDF_Gen['MobCostPerDay']   = round(PersonnalDF_Gen['PersonnelCostPerDay'].mul(PersonnalDF_Gen['MobCostPerDay_X']),2)
            
        

            def trans_Mobilization_PerHour(y):
                if y == "Y":
                    return (1/ShiftHour_Cal)

                elif y == "Yes":
                    return (1/ShiftHour_Cal)

                elif y == "y":
                    return (1/ShiftHour_Cal)

                elif y == "yes":
                    return (1/ShiftHour_Cal)

                elif y == "YES":
                    return (1/ShiftHour_Cal)

                elif y == "N":
                    return 0.0

                elif y == "No":
                    return 0.0

                elif y == "NO":
                    return 0.0

                elif y == "no":
                    return 0.0

                else:
                    return (float(y)*(1/ShiftHour_Cal))

            PersonnalDF_Gen['MobCostPerHour_X'] = PersonnalDF_Gen['Mobilization'].apply(trans_Mobilization_PerHour)
            PersonnalDF_Gen['MobCostPerHour']   = round(PersonnalDF_Gen['PersonnelCostPerDay'].mul(PersonnalDF_Gen['MobCostPerHour_X']),2)
            PersonnalDF_Gen['MobCostPerHour']   = round(PersonnalDF_Gen['MobCostPerHour'].mul((PersonnelMobRATE_Cal)/100),2)

            def trans_Weather(y):
                if y == "Y":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "Yes":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "y":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "yes":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "YES":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "N":
                    return 0.0

                elif y == "No":
                    return 0.0

                elif y == "NO":
                    return 0.0

                elif y == "no":
                    return 0.0

                else:
                    return (float(y)*((1/WeatherStandby_Cal)*(WeatherRate_Cal/100)))

            PersonnalDF_Gen['WeatherCostPerHour_X'] = PersonnalDF_Gen['Weather'].apply(trans_Weather)
            PersonnalDF_Gen['WeatherCostPerHour']   = round(PersonnalDF_Gen['PersonnelCostPerDay'].mul(PersonnalDF_Gen['WeatherCostPerHour_X']),2)
            PersonnalDF_Gen['StatdayCostPerHour']   = round(PersonnalDF_Gen['PersonnelCostPerHour'].mul(StatdayRate_Cal/100),2)

            PersonnalDF_Gen['ShiftHour']            = PersonnalDF_Gen.shape[0]*[ShiftHour_Cal]
            PersonnalDF_Gen['WeatherStandby']       = PersonnalDF_Gen.shape[0]*[WeatherStandby_Cal]
            PersonnalDF_Gen['WeatherRate']          = PersonnalDF_Gen.shape[0]*[WeatherRate_Cal]
            PersonnalDF_Gen['StatdayRate']          = PersonnalDF_Gen.shape[0]*[StatdayRate_Cal]
            PersonnalDF_Gen['MobRate']              = PersonnalDF_Gen.shape[0]*[PersonnelMobRATE_Cal]
            PersonnalDF_Gen['Currency']             = PersonnalDF_Gen.shape[0]*[PersonnelCurrency_Cal]

            PersonnalDF_Gen  = PersonnalDF_Gen.loc[:,['Mobilization','Weather','Personnel','Quantity','Rate',
                                                      'PersonnelCostPerDay','PersonnelCostPerHour', 'MobCostPerDay',
                                                      'MobCostPerHour','WeatherCostPerHour','StatdayCostPerHour',
                                                      'ShiftHour','WeatherStandby','WeatherRate','StatdayRate','MobRate','Currency']]
            PersonnalDF_Gen = pd.DataFrame(PersonnalDF_Gen)
            PersonnalDF_Gen = PersonnalDF_Gen.reset_index(drop=True)

            PersonnalDF_Gen_TreeView  = PersonnalDF_Gen.loc[:,['Mobilization','Weather','Personnel','Quantity','Rate',
                                                      'PersonnelCostPerDay','PersonnelCostPerHour', 'MobCostPerDay',
                                                      'MobCostPerHour','WeatherCostPerHour','StatdayCostPerHour']]
            PersonnalDF_Gen_TreeView = pd.DataFrame(PersonnalDF_Gen_TreeView)
            PersonnalDF_Gen_TreeView = PersonnalDF_Gen_TreeView.reset_index(drop=True)
            for each_rec in range(len(PersonnalDF_Gen_TreeView)):
                tree_PersonnelREPORT.insert("", tk.END, values=list(PersonnalDF_Gen_TreeView.loc[each_rec]))

            SUM_PersonnalDF_Quantity             = round((PersonnalDF_Gen_TreeView['Quantity'].sum(axis = 0, skipna = True)),2)
            SUM_PersonnalDF_PersonnelCostPerDay  = round((PersonnalDF_Gen_TreeView['PersonnelCostPerDay'].sum(axis = 0, skipna = True)),2)
            SUM_PersonnalDF_PersonnelCostPerHour = round((PersonnalDF_Gen_TreeView['PersonnelCostPerHour'].sum(axis = 0, skipna = True)),2)
            SUM_PersonnalDF_MobCostPerDay        = round((PersonnalDF_Gen_TreeView['MobCostPerDay'].sum(axis = 0, skipna = True)),2)
            SUM_PersonnalDF_MobCostPerHour       = round((PersonnalDF_Gen_TreeView['MobCostPerHour'].sum(axis = 0, skipna = True)),2)
            SUM_PersonnalDF_WeatherCostPerHour   = round((PersonnalDF_Gen_TreeView['WeatherCostPerHour'].sum(axis = 0, skipna = True)),2)
            SUM_PersonnalDF_StatdayCostPerHour   = round((PersonnalDF_Gen_TreeView['StatdayCostPerHour'].sum(axis = 0, skipna = True)),2)            
            self.txtPersonnelQuantity.insert(tk.END,SUM_PersonnalDF_Quantity)
            self.txtPersonnelCostPerDay.insert(tk.END,SUM_PersonnalDF_PersonnelCostPerDay)
            self.txtPersonnelCostPerHour.insert(tk.END,SUM_PersonnalDF_PersonnelCostPerHour)
            self.txtMobCostPerDay.insert(tk.END,SUM_PersonnalDF_MobCostPerDay)
            self.txtMobCostPerHour.insert(tk.END,SUM_PersonnalDF_MobCostPerHour)
            self.txtWeatherCostPerHour.insert(tk.END,SUM_PersonnalDF_WeatherCostPerHour)
            self.txtStatCostPerHour.insert(tk.END,SUM_PersonnalDF_StatdayCostPerHour)

            PersonnalDF_Gen['TotalPersonnal_Quantity']             = PersonnalDF_Gen.shape[0]*[SUM_PersonnalDF_Quantity]
            PersonnalDF_Gen['TotalPersonnal_CostPerDay']           = PersonnalDF_Gen.shape[0]*[SUM_PersonnalDF_PersonnelCostPerDay]
            PersonnalDF_Gen['TotalPersonnal_CostPerHour']          = PersonnalDF_Gen.shape[0]*[SUM_PersonnalDF_PersonnelCostPerHour]
            PersonnalDF_Gen['TotalPersonnal_MobCostPerDay']        = PersonnalDF_Gen.shape[0]*[SUM_PersonnalDF_MobCostPerDay]
            PersonnalDF_Gen['TotalPersonnal_MobCostPerHour']       = PersonnalDF_Gen.shape[0]*[SUM_PersonnalDF_MobCostPerHour]
            PersonnalDF_Gen['TotalPersonnal_WeatherCostPerHour']   = PersonnalDF_Gen.shape[0]*[SUM_PersonnalDF_WeatherCostPerHour]
            PersonnalDF_Gen['TotalPersonnal_StatdayCostPerHour']   = PersonnalDF_Gen.shape[0]*[SUM_PersonnalDF_StatdayCostPerHour]
            PersonnalDF_Gen = pd.DataFrame(PersonnalDF_Gen)
            PersonnalDF_Gen = PersonnalDF_Gen.reset_index(drop=True)

            ## Updating Personnel DB After Finish Calculation
            User_Entry_Cal = {'ShiftHour': [ShiftHour_Cal], 'WeatherStandby': [WeatherStandby_Cal],
                              'WeatherRate': [WeatherRate_Cal], 'StatdayRate': [StatdayRate_Cal]}
            User_EntryDF_Cal = pd.DataFrame(User_Entry_Cal, columns = ['ShiftHour', 'WeatherStandby', 'WeatherRate', 'StatdayRate'])
            User_EntryDF_Cal = User_EntryDF_Cal.reset_index(drop=True)
            conn = sqlite3.connect("EagleBidWidget.db")
            PersonnalDF_Cal.to_sql('EagleBidWidget_Personnal_Log', conn, if_exists="replace", index=False)
            User_EntryDF_Cal.to_sql('EagleBidWidget_Personnal_Entry',conn, if_exists="replace", index=False)
            PersonnalDF_Gen.to_sql('EagleBidWidget_Personnal_Expense',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()


        def Generate_Equipment_Expense():
            tree_EquipmentREPORT.delete(*tree_EquipmentREPORT.get_children())
            self.txtEquipmentShiftHOUR.delete(0,END)
            self.txtEquipmentWeatherHOUR.delete(0,END)
            self.txtEquipmentWeatherRATE.delete(0,END)
            self.txtEquipmentStatRATE.delete(0,END)
            self.txtEquipmentQuantity.delete(0,END)
            self.txtEquipmentCostPerDay.delete(0,END)
            self.txtEquipmentCostPerHour.delete(0,END)            
            self.txtEquipmentMobCostPerDay.delete(0,END)
            self.txtEquipmentMobCostPerHour.delete(0,END)
            self.txtEquipmentWeatherCostPerHour.delete(0,END)
            self.txtEquipmentStatCostPerHour.delete(0,END)

            ShiftHour_Cal          = float(self.txtShiftHourEQ.get())
            WeatherStandby_Cal     = float(self.txtWeatherStandbyEQ.get())
            WeatherRate_Cal        = float(self.txtWeatherRateEQ.get())
            StatdayRate_Cal        = float(self.txtStatdayRateEQ.get())
            EquipmentMobRATE_Cal   = float(self.txtEquipmentMobRATE.get())
            EquipmentCurrency_Cal  = (self.txtEquipmentCurrency.get())

            self.txtEquipmentShiftHOUR.insert(tk.END,ShiftHour_Cal)
            self.txtEquipmentWeatherHOUR.insert(tk.END,WeatherStandby_Cal)
            self.txtEquipmentWeatherRATE.insert(tk.END,WeatherRate_Cal)
            self.txtEquipmentStatRATE.insert(tk.END,StatdayRate_Cal)

            conn = sqlite3.connect("EagleBidWidget.db")
            EquipmentDF_Cal = pd.read_sql_query("SELECT * FROM EagleBidWidget_Equipment_Log ORDER BY `Rate` DESC ;", conn)
            EquipmentDF_Cal = pd.DataFrame(EquipmentDF_Cal)
            EquipmentDF_Cal = EquipmentDF_Cal.reset_index(drop=True)

            ## Equipment Expense Report Generating Here
            EquipmentDF_Gen = pd.DataFrame(EquipmentDF_Cal)
            EquipmentDF_Gen = EquipmentDF_Gen.reset_index(drop=True)

            EquipmentDF_Gen['EquipmentCostPerDay']  = EquipmentDF_Gen['Rate'].mul(EquipmentDF_Gen['Quantity'])
            EquipmentDF_Gen['EquipmentCostPerHour'] = round(EquipmentDF_Gen['EquipmentCostPerDay'].mul(1/ShiftHour_Cal),2)


            def trans_Mobilization_PerDay(y):
                if y == "Y":
                    return (EquipmentMobRATE_Cal/100)

                elif y == "Yes":
                    return (EquipmentMobRATE_Cal/100)

                elif y == "y":
                    return (EquipmentMobRATE_Cal/100)

                elif y == "yes":
                    return (EquipmentMobRATE_Cal/100)

                elif y == "YES":
                    return (EquipmentMobRATE_Cal/100)

                elif y == "N":
                    return 0.0

                elif y == "No":
                    return 0.0

                elif y == "NO":
                    return 0.0

                elif y == "no":
                    return 0.0

                else:
                    return (float(y)*(EquipmentMobRATE_Cal/100))

            EquipmentDF_Gen['MobCostPerDay_X'] = EquipmentDF_Gen['Mobilization'].apply(trans_Mobilization_PerDay)
            EquipmentDF_Gen['MobCostPerDay']   = round(EquipmentDF_Gen['EquipmentCostPerDay'].mul(EquipmentDF_Gen['MobCostPerDay_X']),2)

            def trans_Mobilization_PerHour(y):
                if y == "Y":
                    return (1/ShiftHour_Cal)

                elif y == "Yes":
                    return (1/ShiftHour_Cal)

                elif y == "y":
                    return (1/ShiftHour_Cal)

                elif y == "yes":
                    return (1/ShiftHour_Cal)

                elif y == "YES":
                    return (1/ShiftHour_Cal)

                elif y == "N":
                    return 0.0

                elif y == "No":
                    return 0.0

                elif y == "NO":
                    return 0.0

                elif y == "no":
                    return 0.0

                else:
                    return (float(y)*(1/ShiftHour_Cal))

            EquipmentDF_Gen['MobCostPerHour_X'] = EquipmentDF_Gen['Mobilization'].apply(trans_Mobilization_PerHour)
            EquipmentDF_Gen['MobCostPerHour']   = round(EquipmentDF_Gen['EquipmentCostPerDay'].mul(EquipmentDF_Gen['MobCostPerHour_X']),2)
            EquipmentDF_Gen['MobCostPerHour']   = round(EquipmentDF_Gen['MobCostPerHour'].mul((EquipmentMobRATE_Cal)/100),2)

            def trans_Weather(y):
                if y == "Y":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "Yes":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "y":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "yes":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "YES":
                    return ((1/WeatherStandby_Cal)*(WeatherRate_Cal/100))

                elif y == "N":
                    return 0.0

                elif y == "No":
                    return 0.0

                elif y == "NO":
                    return 0.0

                elif y == "no":
                    return 0.0

                else:
                    return (float(y)*((1/WeatherStandby_Cal)*(WeatherRate_Cal/100)))

            EquipmentDF_Gen['WeatherCostPerHour_X'] = EquipmentDF_Gen['Weather'].apply(trans_Weather)
            EquipmentDF_Gen['WeatherCostPerHour']   = round(EquipmentDF_Gen['EquipmentCostPerDay'].mul(EquipmentDF_Gen['WeatherCostPerHour_X']),2)
            EquipmentDF_Gen['StatdayCostPerHour']   = round(EquipmentDF_Gen['EquipmentCostPerHour'].mul(StatdayRate_Cal/100),2)

            EquipmentDF_Gen['ShiftHour']            = EquipmentDF_Gen.shape[0]*[ShiftHour_Cal]
            EquipmentDF_Gen['WeatherStandby']       = EquipmentDF_Gen.shape[0]*[WeatherStandby_Cal]
            EquipmentDF_Gen['WeatherRate']          = EquipmentDF_Gen.shape[0]*[WeatherRate_Cal]
            EquipmentDF_Gen['StatdayRate']          = EquipmentDF_Gen.shape[0]*[StatdayRate_Cal]
            EquipmentDF_Gen['MobRate']              = EquipmentDF_Gen.shape[0]*[EquipmentMobRATE_Cal]
            EquipmentDF_Gen['Currency']             = EquipmentDF_Gen.shape[0]*[EquipmentCurrency_Cal]

           
            EquipmentDF_Gen  = EquipmentDF_Gen.loc[:,['Mobilization','Weather','Equipment','Quantity','Rate',
                                                      'EquipmentCostPerDay','EquipmentCostPerHour','MobCostPerDay',
                                                      'MobCostPerHour','WeatherCostPerHour','StatdayCostPerHour',
                                                      'ShiftHour','WeatherStandby','WeatherRate','StatdayRate', 'MobRate', 'Currency']]
            EquipmentDF_Gen = pd.DataFrame(EquipmentDF_Gen)
            EquipmentDF_Gen = EquipmentDF_Gen.reset_index(drop=True)

            EquipmentDF_Gen_TreeView  = EquipmentDF_Gen.loc[:,['Mobilization','Weather','Equipment','Quantity','Rate',
                                                               'EquipmentCostPerDay','EquipmentCostPerHour','MobCostPerDay',
                                                               'MobCostPerHour','WeatherCostPerHour','StatdayCostPerHour']]
            EquipmentDF_Gen_TreeView = pd.DataFrame(EquipmentDF_Gen_TreeView)
            EquipmentDF_Gen_TreeView = EquipmentDF_Gen_TreeView.reset_index(drop=True)

            for each_rec in range(len(EquipmentDF_Gen_TreeView)):
                tree_EquipmentREPORT.insert("", tk.END, values=list(EquipmentDF_Gen_TreeView.loc[each_rec]))

            SUM_EquipmentDF_EquipmentQuantity    = round((EquipmentDF_Gen_TreeView['Equipment'].count()),2)
            SUM_EquipmentDF_EquipmentCostPerDay  = round((EquipmentDF_Gen_TreeView['EquipmentCostPerDay'].sum(axis = 0, skipna = True)),2)
            SUM_EquipmentDF_EquipmentCostPerHour = round((EquipmentDF_Gen_TreeView['EquipmentCostPerHour'].sum(axis = 0, skipna = True)),2)
            SUM_EquipmentDF_MobCostPerDay        = round((EquipmentDF_Gen_TreeView['MobCostPerDay'].sum(axis = 0, skipna = True)),2)
            SUM_EquipmentDF_MobCostPerHour       = round((EquipmentDF_Gen_TreeView['MobCostPerHour'].sum(axis = 0, skipna = True)),2)
            SUM_EquipmentDF_WeatherCostPerHour   = round((EquipmentDF_Gen_TreeView['WeatherCostPerHour'].sum(axis = 0, skipna = True)),2)
            SUM_EquipmentDF_StatdayCostPerHour   = round((EquipmentDF_Gen_TreeView['StatdayCostPerHour'].sum(axis = 0, skipna = True)),2)
            
            self.txtEquipmentQuantity.insert(tk.END,SUM_EquipmentDF_EquipmentQuantity)
            self.txtEquipmentCostPerDay.insert(tk.END,SUM_EquipmentDF_EquipmentCostPerDay)
            self.txtEquipmentCostPerHour.insert(tk.END,SUM_EquipmentDF_EquipmentCostPerHour)
            self.txtEquipmentMobCostPerDay.insert(tk.END,SUM_EquipmentDF_MobCostPerDay)
            self.txtEquipmentMobCostPerHour.insert(tk.END,SUM_EquipmentDF_MobCostPerHour)
            self.txtEquipmentWeatherCostPerHour.insert(tk.END,SUM_EquipmentDF_WeatherCostPerHour)
            self.txtEquipmentStatCostPerHour.insert(tk.END,SUM_EquipmentDF_StatdayCostPerHour)

            EquipmentDF_Gen['TotalEquipment_Quantity']             = EquipmentDF_Gen.shape[0]*[SUM_EquipmentDF_EquipmentQuantity]
            EquipmentDF_Gen['TotalEquipment_CostPerDay']           = EquipmentDF_Gen.shape[0]*[SUM_EquipmentDF_EquipmentCostPerDay]
            EquipmentDF_Gen['TotalEquipment_CostPerHour']          = EquipmentDF_Gen.shape[0]*[SUM_EquipmentDF_EquipmentCostPerHour]
            EquipmentDF_Gen['TotalEquipment_MobCostPerDay']        = EquipmentDF_Gen.shape[0]*[SUM_EquipmentDF_MobCostPerDay]
            EquipmentDF_Gen['TotalEquipment_MobCostPerHour']       = EquipmentDF_Gen.shape[0]*[SUM_EquipmentDF_MobCostPerHour]
            EquipmentDF_Gen['TotalEquipment_WeatherCostPerHour']   = EquipmentDF_Gen.shape[0]*[SUM_EquipmentDF_WeatherCostPerHour]
            EquipmentDF_Gen['TotalEquipment_StatdayCostPerHour']   = EquipmentDF_Gen.shape[0]*[SUM_EquipmentDF_StatdayCostPerHour]
            EquipmentDF_Gen = pd.DataFrame(EquipmentDF_Gen)
            EquipmentDF_Gen = EquipmentDF_Gen.reset_index(drop=True)

            
            ## Updating Personnel DB After Finish Calculation
            User_Entry_Cal = {'ShiftHour': [ShiftHour_Cal], 'WeatherStandby': [WeatherStandby_Cal],
                              'WeatherRate': [WeatherRate_Cal], 'StatdayRate': [StatdayRate_Cal]}
            User_EntryDF_Cal = pd.DataFrame(User_Entry_Cal, columns = ['ShiftHour', 'WeatherStandby', 'WeatherRate', 'StatdayRate'])
            User_EntryDF_Cal = User_EntryDF_Cal.reset_index(drop=True)
            conn = sqlite3.connect("EagleBidWidget.db")
            EquipmentDF_Cal.to_sql('EagleBidWidget_Equipment_Log', conn, if_exists="replace", index=False)
            User_EntryDF_Cal.to_sql('EagleBidWidget_Equipment_Entry',conn, if_exists="replace", index=False)
            EquipmentDF_Gen.to_sql('EagleBidWidget_Equipment_Expense',conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()

        def GenPersonnel_Clear_Report():
            tree_PersonnelREPORT.delete(*tree_PersonnelREPORT.get_children())
            self.txtPersonnelShiftHOUR.delete(0,END)
            self.txtPersonnelWeatherHOUR.delete(0,END)
            self.txtPersonnelWeatherRATE.delete(0,END)
            self.txtPersonnelStatRATE.delete(0,END)
            self.txtPersonnelQuantity.delete(0,END)
            self.txtPersonnelCostPerDay.delete(0,END)
            self.txtPersonnelCostPerHour.delete(0,END)
            self.txtMobCostPerDay.delete(0,END)
            self.txtMobCostPerHour.delete(0,END)
            self.txtWeatherCostPerHour.delete(0,END)
            self.txtStatCostPerHour.delete(0,END)

        def GenEquipment_Clear_Report():
            tree_EquipmentREPORT.delete(*tree_EquipmentREPORT.get_children())
            self.txtEquipmentShiftHOUR.delete(0,END)
            self.txtEquipmentWeatherHOUR.delete(0,END)
            self.txtEquipmentWeatherRATE.delete(0,END)
            self.txtEquipmentStatRATE.delete(0,END)
            self.txtEquipmentQuantity.delete(0,END)
            self.txtEquipmentCostPerDay.delete(0,END)
            self.txtEquipmentCostPerHour.delete(0,END)            
            self.txtEquipmentMobCostPerDay.delete(0,END)
            self.txtEquipmentMobCostPerHour.delete(0,END)
            self.txtEquipmentWeatherCostPerHour.delete(0,END)
            self.txtEquipmentStatCostPerHour.delete(0,END)
            
                

        ## Command Buttons For Personnal Expense Only
        btnModifyUpdatePersonnel_LOG = Button(self.root, text="Update", font=('aerial', 10, 'bold'), height =1, width=6, bd=1, command = update_Personnel_LOG)
        btnModifyUpdatePersonnel_LOG.place(x=2,y=436)
        btnDeletePersonnel_LOG = Button(self.root, text="Delete", font=('aerial', 10, 'bold'), height =1, width=6, bd=1, command = Delete_Personnel_LOG)
        btnDeletePersonnel_LOG.place(x=62,y=436)
        btnAddPersonnel_LOG = Button(self.root, text="Add", font=('aerial', 10, 'bold'), height =1, width=4, bd=1, command = Add_Personnel_LOG)
        btnAddPersonnel_LOG.place(x=122,y=436)        
        btnLoad_New_Personnel_Profile = Button(self.root, text="Load New Profile", font=('aerial', 10, 'bold'), height =1, width=14, bd=1, command = Load_Personnel_New_Profile)
        btnLoad_New_Personnel_Profile.place(x=168,y=436)        
        btnGenPersonnel_Exp_Report = Button(self.root, text="Preview Expense", font=('aerial', 10, 'bold'),  height =1, width=14, bd=1, command = Generate_Personnel_Expense)
        btnGenPersonnel_Exp_Report.place(x=322,y=436)
        btnGenPersonnel_Clear_Report = Button(self.root, text="Clear Output", font=('aerial', 9, 'bold'),  height =1, width=10, bd=1, command = GenPersonnel_Clear_Report)
        btnGenPersonnel_Clear_Report.place(x=363,y=0)
        

        ## Command Buttons For Equipment Expense Only
        btnModifyUpdateEquipment_LOG = Button(self.root, text="Update", font=('aerial', 10, 'bold'), height =1, width=6, bd=1, command = update_Equipment_LOG)
        btnModifyUpdateEquipment_LOG.place(x=2,y=830)        
        btnDeleteEquipment_LOG = Button(self.root, text="Delete", font=('aerial', 10, 'bold'), height =1, width=6, bd=1, command = Delete_Equipment_LOG)
        btnDeleteEquipment_LOG.place(x=62,y=830)
        btnAddEquipment_LOG = Button(self.root, text="Add", font=('aerial', 10, 'bold'), height =1, width=4, bd=1, command = Add_Equipment_LOG)
        btnAddEquipment_LOG.place(x=122,y=830)        
        btnLoad_New_Equipment_Profile = Button(self.root, text="Load New Profile", font=('aerial', 10, 'bold'), height =1, width=14, bd=1, command = Load_Equipment_New_Profile)
        btnLoad_New_Equipment_Profile.place(x=168,y=830)        
        btnGenEquipment_Exp_Report = Button(self.root, text="Preview Expense", font=('aerial', 10, 'bold'),  height =1, width=14, bd=1, command = Generate_Equipment_Expense)
        btnGenEquipment_Exp_Report.place(x=322,y=830)
        btnGenEquipment_Clear_Report = Button(self.root, text="Clear Output", font=('aerial', 9, 'bold'),  height =1, width=10, bd=1, command = GenEquipment_Clear_Report)
        btnGenEquipment_Clear_Report.place(x=363,y=471)


        ########################### GLOBAL FUNTIONS FOR EQUIPMENT AND EXPENSE CALCULATION #################################

        ### Functions For Global Personnel And Equipment Calculation

        def Generate_Global_PersonnelEquipment_Expense():
            self.txtTotalDailyCostPerDay.delete(0,END)
            self.txtTotalDailyCostPerHour.delete(0,END)
            self.txtTotalMobCostPerDay.delete(0,END)
            self.txtTotalMobCostPerHour.delete(0,END)
            self.txtTotalWeatherCostPerHour.delete(0,END)
            self.txtTotalStatCostPerHour.delete(0,END)
            Generate_Personnel_Expense()
            Generate_Equipment_Expense()

            TotalDailyCostPerDay_Cal = round(float(self.txtPersonnelCostPerDay.get()) + float(self.txtEquipmentCostPerDay.get()),2)
            self.txtTotalDailyCostPerDay.insert(tk.END,TotalDailyCostPerDay_Cal)

            TotalDailyCostPerHour_Cal = round(float(self.txtPersonnelCostPerHour.get()) + float(self.txtEquipmentCostPerHour.get()),2)
            self.txtTotalDailyCostPerHour.insert(tk.END,TotalDailyCostPerHour_Cal)

            TotalMobCostPerDay_Cal = round(float(self.txtMobCostPerDay.get()) + float(self.txtEquipmentMobCostPerDay.get()),2)
            self.txtTotalMobCostPerDay.insert(tk.END,TotalMobCostPerDay_Cal)

            TotalMobCostPerHour_Cal = round(float(self.txtMobCostPerHour.get()) + float(self.txtEquipmentMobCostPerHour.get()),2)
            self.txtTotalMobCostPerHour.insert(tk.END,TotalMobCostPerHour_Cal)

            TotalWeatherCostPerHour_Cal = round(float(self.txtWeatherCostPerHour.get()) + float(self.txtEquipmentWeatherCostPerHour.get()),2)
            self.txtTotalWeatherCostPerHour.insert(tk.END,TotalWeatherCostPerHour_Cal)

            TotalStatCostPerHour_Cal = round(float(self.txtStatCostPerHour.get()) + float(self.txtEquipmentStatCostPerHour.get()),2)
            self.txtTotalStatCostPerHour.insert(tk.END,TotalStatCostPerHour_Cal)

            TotalWeatherCostPerDay_Cal = round(float(self.txtWeatherCostPerHour.get())*float(self.txtWeatherStandby.get()) + float(self.txtEquipmentWeatherCostPerHour.get())*float(self.txtWeatherStandbyEQ.get()),2)
            TotalStatCostPerDay_Cal    = round(float(self.txtPersonnelCostPerDay.get())*((float(self.txtStatdayRate.get()))/100) + float(self.txtEquipmentCostPerDay.get())*((float(self.txtStatdayRateEQ.get()))/100),2)

            
            Global_PersonnelEQ_Summary = {'ItemIndex':       [1, 2,3,4],
                                          'ExpenseItem':     ["Total Fixed Cost",           "Mobilization/Demobilization Cost",
                                                              "Weather Day Standby Cost", "Stat Holiday Day Cost"],
                                          'DailyCost':       [TotalDailyCostPerDay_Cal,  TotalMobCostPerDay_Cal,  TotalWeatherCostPerDay_Cal,  TotalStatCostPerDay_Cal],
                                          'HourlyCost':      [TotalDailyCostPerHour_Cal, TotalMobCostPerHour_Cal, TotalWeatherCostPerHour_Cal, TotalStatCostPerHour_Cal],
                                          'HourlyBidEntry':  [TotalDailyCostPerHour_Cal, TotalMobCostPerHour_Cal, TotalWeatherCostPerHour_Cal, TotalStatCostPerHour_Cal]}
            Global_PersonnelEQ_SummaryDF = pd.DataFrame(Global_PersonnelEQ_Summary, columns = ['ItemIndex', 'ExpenseItem', 'DailyCost', 'HourlyCost', 'HourlyBidEntry'])
            Global_PersonnelEQ_SummaryDF = Global_PersonnelEQ_SummaryDF.reset_index(drop=True)
            conn = sqlite3.connect("EagleBidWidget.db")
            Global_PersonnelEQ_SummaryDF.to_sql('EagleBidWidget_Personnel_Equipment_GLOBAL', conn, if_exists="replace", index=False)
            conn.commit()
            conn.close()
        
        def Gen_Bid_Entry_Submit():
            conn = sqlite3.connect("EagleBidWidget.db")
            cur=conn.cursor()
            cur.execute("DELETE FROM EagleBidWidget_ClientSupply_GLOBAL")
            conn.commit()
            conn.close()
            data = pd.DataFrame([])
            for item in tree_EquipmentREPORT.selection():                
                list_item = (tree_EquipmentREPORT.item(item, 'values'))                
                x1= list_item[2]
                x2= list_item[6]
                x3= list_item[8]
                x4= list_item[9]
                x5= list_item[10]
                data = data.append(pd.DataFrame({'ClientSuppliedItem': x1,
                                                 'CostHour': x2,
                                                 'MobCostHour': x3,
                                                 'WeatherCostHour': x4,
                                                 'StatDayCostHour': x5
                                                 }, index=[0]), ignore_index=True)
            if len(data)>0:
                ClientSuppliedEquipmentList = pd.DataFrame(data)
                ClientSuppliedEquipmentList =ClientSuppliedEquipmentList.reset_index(drop=True)
                conn = sqlite3.connect("EagleBidWidget.db")
                ClientSuppliedEquipmentList.to_sql('EagleBidWidget_ClientSupply_GLOBAL', conn, if_exists="replace", index=False)
                conn.commit()
                conn.close()

            Eagle_Bid_Personnel_Equipment_BID_ENTRY.BID_Entry_Personnel_Equipment()

        def Gen_Personnel_Equipment_REPORT():
            Eagle_Bid_Personnel_Equipment_REPORT.BID_Entry_Personnel_Equipment_Report()

        def Clear_Personnel_Equipment_REPORT():
            self.txtTotalDailyCostPerDay.delete(0,END)
            self.txtTotalDailyCostPerHour.delete(0,END)
            self.txtTotalMobCostPerDay.delete(0,END)
            self.txtTotalMobCostPerHour.delete(0,END)
            self.txtTotalWeatherCostPerHour.delete(0,END)
            self.txtTotalStatCostPerHour.delete(0,END)
            


        ## GLOBAL COMMAND BUTTON FOR PERSONNEL AND EQUIPMENT
        btnGenPersonnel_Equipment_Exp_Report = Button(DataFrameGLOBAL, text="Generate Report", font=('aerial', 11, 'bold'),  bg='yellow', height =1, width=14, bd=3, command = Generate_Global_PersonnelEquipment_Expense)
        btnGenPersonnel_Equipment_Exp_Report.place(x=0,y=26)
        btnBidEntry = Button(DataFrameGLOBAL, text="Bid Entry", font=('aerial', 11, 'bold'),  bg='yellow', height =1, width=8, bd=3, command = Gen_Bid_Entry_Submit)
        btnBidEntry.place(x=143,y=26)
        btnExportReport = Button(DataFrameGLOBAL, text="Export Report", font=('aerial', 11, 'bold'),  bg='yellow', height =1, width=12, bd=3, command = Gen_Personnel_Equipment_REPORT)
        btnExportReport.place(x=236,y=26)

        btnCLRReport = Button(DataFrameGLOBAL, text="Clear", font=('aerial', 11, 'bold'),  bg='yellow', height =1, width=4, bd=3, command = Clear_Personnel_Equipment_REPORT)
        btnCLRReport.place(x=370,y=26)
                                              

if __name__ == '__main__':
    root = Tk()
    application  = BidEagle_Personnel_Equipment_Expense (root)
    root.mainloop()

