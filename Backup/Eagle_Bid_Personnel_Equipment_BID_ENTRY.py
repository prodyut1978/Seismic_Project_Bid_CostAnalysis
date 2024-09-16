import os
from tkinter import*
import tkinter.messagebox
import Eagle_Bid_Database_BackEnd
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

def BID_Entry_Personnel_Equipment():
    Default_Date_today   = datetime.date.today()
    Window =Tk()
    Window.title ("Eagle Bid Entry For Personnel and Equipment Expenses")
    Window.geometry("842x550+0+0")
    Window.config(bg="lightblue")
    Window.resizable(0, 0)

    MODIFYBID                = DoubleVar()
    Index                    = IntVar()
    ItemName                 = StringVar()
    costDay                  = DoubleVar()
    costHour                 = DoubleVar()
    BidEntry                 = DoubleVar()

    Label_PersonnelEquipment = Label(Window, text = "CALCULATED PERSONNEL AND EQUIPMENT EXPENSE SUMMARY AND USER BID ENTRY:",
                                     font=("arial", 12,'bold'),bg = "lightblue", fg="blue").place(x=2,y=2)
    Label_MODIFYBID = Label(Window, text = "MODIFY/UPDATE SELECTED BID ENTRY COST/HOUR :",
                                     font=("arial", 12,'bold'),bg = "lightblue", fg="blue").place(x=240,y=228)

    Label_ClientSupplyList = Label(Window, text = "CLIENT SUPPLY FUEL AND SUBSISTANCE LIST:",
                                     font=("arial", 12,'bold'),bg = "lightblue", fg="blue").place(x=0,y=280)
    Label_ClientDeductable = Label(Window, text = "Total Deduction:",
                                     font=("arial", 11,'bold'),bg = "lightblue", fg="blue").place(x=0,y=433)


    txtLabel_MODIFYBIDUSERENTRY= Entry(Window, font=('aerial', 11, 'bold'), textvariable = MODIFYBID, width = 19, bd=4)
    txtLabel_MODIFYBIDUSERENTRY.place(x=675,y=228)

    txtLabel_Index= Entry(Window, font=('aerial', 10, 'bold'), bg='cadet blue', textvariable = Index, width = 6, bd=1)
    txtLabel_Index.place(x=2,y=204)

    txtLabel_Item= Entry(Window, font=('aerial', 10, 'bold'), bg='cadet blue', textvariable = ItemName, width = 36, bd=1)
    txtLabel_Item.place(x=55,y=204)

    txtLabel_costDay= Entry(Window, font=('aerial', 10, 'bold'), bg='cadet blue', textvariable = costDay, width = 24, bd=1)
    txtLabel_costDay.place(x=318,y=204)

    txtLabel_costHour= Entry(Window, font=('aerial', 10, 'bold'), bg='cadet blue', textvariable = costHour, width = 24, bd=1)
    txtLabel_costHour.place(x=497,y=204)

    txtLabel_BidEntry= Entry(Window, font=('aerial', 10, 'bold'), bg='cadet blue', textvariable = BidEntry, width = 23, bd=1)
    txtLabel_BidEntry.place(x=675,y=204)


    txtClientSupply_costHour= Entry(Window, font=('aerial', 8, 'bold'), bg='lightgreen', textvariable = DoubleVar(), width = 12, bd=1)
    txtClientSupply_costHour.place(x=150,y=435)

    txtClientSupply_MobcostHour= Entry(Window, font=('aerial', 8, 'bold'), bg='lightgreen', textvariable = DoubleVar(), width = 12, bd=1)
    txtClientSupply_MobcostHour.place(x=235,y=435)

    txtClientSupply_WxcostHour= Entry(Window, font=('aerial', 8, 'bold'), bg='lightgreen', textvariable = DoubleVar(), width = 12, bd=1)
    txtClientSupply_WxcostHour.place(x=320,y=435)

    txtClientSupply_StatcostHour= Entry(Window, font=('aerial', 8, 'bold'), bg='lightgreen', textvariable = DoubleVar(), width = 12, bd=1)
    txtClientSupply_StatcostHour.place(x=404,y=435)


    TableMargin_PersonnelEquipment = Frame(Window)
    TableMargin_PersonnelEquipment.place(x=2,y=30)         
    tree_PersonnelEquipment = ttk.Treeview(TableMargin_PersonnelEquipment, column=("column1", "column2", "column3", "column4", "column5"),
                        height=7, show='headings')
    tree_PersonnelEquipment.heading("#1", text="Index", anchor=W)
    tree_PersonnelEquipment.heading("#2", text="Personnel & Equipment Cost Item", anchor=W)
    tree_PersonnelEquipment.heading("#3", text="Calculated Cost/Day", anchor=W)
    tree_PersonnelEquipment.heading("#4", text="Calculated Cost/Hour", anchor=W)
    tree_PersonnelEquipment.heading("#5", text="Bid Entry Cost/Hour", anchor=W)
    tree_PersonnelEquipment.column('#1', stretch=NO, minwidth=0, width=60)
    tree_PersonnelEquipment.column('#2', stretch=NO, minwidth=0, width=260)            
    tree_PersonnelEquipment.column('#3', stretch=NO, minwidth=0, width=162)
    tree_PersonnelEquipment.column('#4', stretch=NO, minwidth=0, width=180)
    tree_PersonnelEquipment.column('#5', stretch=NO, minwidth=0, width=172)
    tree_PersonnelEquipment.pack()

    TableMargin_ClientEQ_List = Frame(Window)
    TableMargin_ClientEQ_List.place(x=2,y=305)
    scrollbary = Scrollbar(TableMargin_ClientEQ_List, orient=VERTICAL)
    tree_ClientEQ_List = ttk.Treeview(TableMargin_ClientEQ_List, column=("column1", "column2", "column3", "column4", "column5"),
                        height=5, show='headings')
    scrollbary.config(command=tree_ClientEQ_List.yview)
    scrollbary.pack(side=RIGHT, fill=Y)   

    tree_ClientEQ_List.heading("#1", text="Item", anchor=W)
    tree_ClientEQ_List.heading("#2", text="Cost/Hour", anchor=W)
    tree_ClientEQ_List.heading("#3", text="Mob/Hour", anchor=W)
    tree_ClientEQ_List.heading("#4", text="Weather/Hour", anchor=W)
    tree_ClientEQ_List.heading("#5", text="Stat/Hour", anchor=W)

    tree_ClientEQ_List.column('#1', stretch=NO, minwidth=0, width=150)
    tree_ClientEQ_List.column('#2', stretch=NO, minwidth=0, width=80)            
    tree_ClientEQ_List.column('#3', stretch=NO, minwidth=0, width=80)
    tree_ClientEQ_List.column('#4', stretch=NO, minwidth=0, width=85)
    tree_ClientEQ_List.column('#5', stretch=NO, minwidth=0, width=80)
    tree_ClientEQ_List.pack()

    def tree_PersonnelEquipmentRec(event):
        for nm in tree_PersonnelEquipment.selection():
            sd = tree_PersonnelEquipment.item(nm, 'values')

            txtLabel_Index.delete(0,END)
            txtLabel_Index.insert(tk.END,sd[0])

            txtLabel_Item.delete(0,END)
            txtLabel_Item.insert(tk.END,sd[1])

            txtLabel_costDay.delete(0,END)
            txtLabel_costDay.insert(tk.END,sd[2])

            txtLabel_costHour.delete(0,END)
            txtLabel_costHour.insert(tk.END,sd[3])

            txtLabel_BidEntry.delete(0,END)
            txtLabel_BidEntry.insert(tk.END,sd[4])
                                                                                                            
            txtLabel_MODIFYBIDUSERENTRY.delete(0,END)
            txtLabel_MODIFYBIDUSERENTRY.insert(tk.END,sd[4])                          

    tree_PersonnelEquipment.bind('<<TreeviewSelect>>',tree_PersonnelEquipmentRec)

    conn = sqlite3.connect("EagleBidWidget.db")
    PersonnelEquipmentDF = pd.read_sql_query("SELECT * FROM EagleBidWidget_Personnel_Equipment_GLOBAL ORDER BY `ItemIndex` ASC ;", conn)        
    PersonnelEquipmentDF = pd.DataFrame(PersonnelEquipmentDF)
    PersonnelEquipmentDF = PersonnelEquipmentDF.reset_index(drop=True)
    ClientSupplyEQ_DF = pd.read_sql_query("SELECT * FROM EagleBidWidget_ClientSupply_GLOBAL ORDER BY `CostHour` DESC ;", conn)        
    ClientSupplyEQ_DF = pd.DataFrame(ClientSupplyEQ_DF)
    ClientSupplyEQ_DF = ClientSupplyEQ_DF.reset_index(drop=True)
    conn.commit()
    conn.close()

    tree_PersonnelEquipment.delete(*tree_PersonnelEquipment.get_children())
    for each_rec in range(len(PersonnelEquipmentDF)):
            tree_PersonnelEquipment.insert("", tk.END, values=list(PersonnelEquipmentDF.loc[each_rec]))


    Length_ClientSupplyEQ_DF = len(ClientSupplyEQ_DF)
    if Length_ClientSupplyEQ_DF > 0:
        ClientSupplyEQ_DF['CostHour']        = (ClientSupplyEQ_DF.loc[:,['CostHour']]).astype(float)
        ClientSupplyEQ_DF['MobCostHour']     = (ClientSupplyEQ_DF.loc[:,['MobCostHour']]).astype(float)
        ClientSupplyEQ_DF['WeatherCostHour'] = (ClientSupplyEQ_DF.loc[:,['WeatherCostHour']]).astype(float)
        ClientSupplyEQ_DF['StatDayCostHour'] = (ClientSupplyEQ_DF.loc[:,['StatDayCostHour']]).astype(float)

        txtClientSupply_costHour.delete(0,END)
        txtClientSupply_MobcostHour.delete(0,END)
        txtClientSupply_WxcostHour.delete(0,END)
        txtClientSupply_StatcostHour.delete(0,END)

        SUM_ClientCostHour         = round((ClientSupplyEQ_DF['CostHour'].sum(axis = 0, skipna = True)),2)
        SUM_ClientMobCostHour      = round((ClientSupplyEQ_DF['MobCostHour'].sum(axis = 0, skipna = True)),2)
        SUM_ClientWeatherCostHour  = round((ClientSupplyEQ_DF['WeatherCostHour'].sum(axis = 0, skipna = True)),2)
        SUM_ClientStatDayCostHour  = round((ClientSupplyEQ_DF['StatDayCostHour'].sum(axis = 0, skipna = True)),2)

        tree_ClientEQ_List.delete(*tree_ClientEQ_List.get_children())
        for each_rec in range(len(ClientSupplyEQ_DF)):
                tree_ClientEQ_List.insert("", tk.END, values=list(ClientSupplyEQ_DF.loc[each_rec]))

        txtClientSupply_costHour.insert(tk.END,SUM_ClientCostHour)
        txtClientSupply_MobcostHour.insert(tk.END,SUM_ClientMobCostHour)
        txtClientSupply_WxcostHour.insert(tk.END,SUM_ClientWeatherCostHour)
        txtClientSupply_StatcostHour.insert(tk.END,SUM_ClientStatDayCostHour)

    def update_BidEntry():
        if(len(txtLabel_MODIFYBIDUSERENTRY.get())>0):
            conn = sqlite3.connect("EagleBidWidget.db")
            cur = conn.cursor()
            for selected_item in tree_PersonnelEquipment.selection():
                cur.execute("DELETE FROM EagleBidWidget_Personnel_Equipment_GLOBAL WHERE ItemIndex =? AND ExpenseItem =? AND \
                             DailyCost =? AND HourlyCost =? AND HourlyBidEntry =? ",\
                            (tree_PersonnelEquipment.set(selected_item, '#1'), tree_PersonnelEquipment.set(selected_item, '#2'),tree_PersonnelEquipment.set(selected_item, '#3'),\
                             tree_PersonnelEquipment.set(selected_item, '#4'), tree_PersonnelEquipment.set(selected_item, '#5'),))
                conn.commit()
                tree_PersonnelEquipment.delete(selected_item)
                conn.close()

        if(len(txtLabel_MODIFYBIDUSERENTRY.get())>0):
            Eagle_Bid_Database_BackEnd.addRec_Personnel_Equipment_GLOBAL(txtLabel_Index.get(), txtLabel_Item.get(), txtLabel_costDay.get(), txtLabel_costHour.get(), txtLabel_MODIFYBIDUSERENTRY.get())
            tree_PersonnelEquipment.delete(*tree_PersonnelEquipment.get_children())
            for row in Eagle_Bid_Database_BackEnd.viewPersonnel_Equipment_GLOBAL():
                tree_PersonnelEquipment.insert("", tk.END, values=row)
        else:
            tkinter.messagebox.showinfo("Update Error","User Bid entry can not be empty")

    def submit_exit():
        Window.destroy()

    ## Functions Buttons for Bid Entry
    btnModifyBidEntry = Button(Window, text="User Modify Bid Entry", font=('aerial', 10, 'bold'),  bg='yellow', height =1, width=19, bd=3, command = update_BidEntry)
    btnModifyBidEntry.place(x=675,y=260)
    btnSubmitBidEntry = Button(Window, text="Submit Bid Entry & Exit", font=('aerial', 10, 'bold'),  bg='yellow', height =1, width=19, bd=3, command = submit_exit)
    btnSubmitBidEntry.place(x=2,y=228)


