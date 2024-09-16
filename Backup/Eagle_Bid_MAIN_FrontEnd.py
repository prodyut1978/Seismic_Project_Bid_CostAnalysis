#Front End
import os
from tkinter import*
import tkinter.messagebox
import tkinter.ttk as ttk
import tkinter as tk
import sqlite3
import Eagle_Bid_Database_BackEnd
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename
from tkinter import simpledialog
import pandas as pd
import openpyxl
import csv
import time
import datetime

## Import For Personnel And Equipment
import Eagle_Bid_Personnel_Equipment_Expense
import Eagle_Bid_Personnel_Equipment_BID_ENTRY
import Eagle_Bid_Personnel_Equipment_REPORT

## Import For Trucking Equipment
import Eagle_Bid_Trucking_Expense
import Eagle_Bid_Trucking_REPORT


Default_Date_today   = datetime.date.today()

class EagleBIDFrontEnd_MAIN:    
    def __init__(self,root):
        
        ##  Define Main Window
        self.root =root
        self.root.title ("Eagle Biding Main")
        self.root.geometry("1180x600+10+0")
        self.root.config(bg="ghost white")
        self.root.resizable(0, 0)
        TitFrame = Frame(self.root, bd = 1, padx= 5, pady= 4, bg = "ghost white", relief = RIDGE)
        TitFrame.pack(side = TOP)
        self.lblTit = Label(TitFrame, bd= 4, font=('aerial', 14, 'bold'), bg = "ghost white", text="EAGLE JOB BIDING SYSTEM")
        self.lblTit.grid()


        ##  Define Main Functions 
        def GenFixedCost_Personnel_Equipment():
            from Eagle_Bid_Personnel_Equipment_Expense import BidEagle_Personnel_Equipment_Expense
            if __name__ == '__main__':
                root = Tk()
                application  = BidEagle_Personnel_Equipment_Expense(root)
                root.mainloop()

        def GenOperCost_Trucking_Equipment():
            from Eagle_Bid_Trucking_Expense import BidEagle_Trucking_Equipment_Expense
            if __name__ == '__main__':
                root = Tk()
                application  = BidEagle_Trucking_Equipment_Expense(root)
                root.mainloop()

    
        ##  Define Labels And Function Buttons
        L1 = Label(self.root, text = "A: Job Biding Profile And Parameters Entry Modules :", font=("arial", 12,'bold'), bg= "ghost white").place(x=10,y=55)            
        btnJobBidProfileParameters = Button(self.root, text="Job Biding Profile And Parameters Entry", font=('aerial', 11, 'bold'), height =1, width=32, bd=4,
                                 command = '')
        btnJobBidProfileParameters.place(x=30,y=84)


        L2 = Label(self.root, text = "B: Job Recording Days Calculation Modules :", font=("arial", 12,'bold'), bg= "ghost white").place(x=10,y=155)
        btnGenRecordingDayReport = Button(self.root, text="Job Recording Days Calculation Report", font=('aerial', 11, 'bold'), height =1, width=32, bd=4,
                                 command = '')
        btnGenRecordingDayReport.place(x=30,y=185)

       
        L3 = Label(self.root, text = "C: Fixed Cost - Personnel And Equipment Report:", font=("arial", 12,'bold'), bg= "ghost white").place(x=10,y=260)        
        btnGenFixedCost_Personnel_Equipment = Button(self.root, text="Personnel And Equipment Cost Report", font=('aerial', 11, 'bold'), height =2, width=32, bd=4,
                                         command = GenFixedCost_Personnel_Equipment)
        btnGenFixedCost_Personnel_Equipment.place(x=30,y=289)


        L4 = Label(self.root, text = "D: Operation Cost - Trucking And Helicopter Report:", font=("arial", 12,'bold'), bg= "ghost white").place(x=10,y=365)
        

        btnGenEquipment_Trucking = Button(self.root, text="Equipment Trucking Cost Report", font=('aerial', 11, 'bold'), height =1, width=32, bd=4,
                                         command = GenOperCost_Trucking_Equipment)
        btnGenEquipment_Trucking.place(x=30,y=395)

        btnGenHelicopter_Operation = Button(self.root, text="Helicopter Operation Cost Report", font=('aerial', 11, 'bold'), height =1, width=32, bd=4,
                                         command = '')
        btnGenHelicopter_Operation.place(x=30,y=445)

        


       


if __name__ == '__main__':
    root = Tk()
    application  = EagleBIDFrontEnd_MAIN(root)
    root.mainloop()
