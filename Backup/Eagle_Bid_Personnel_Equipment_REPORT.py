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

def BID_Entry_Personnel_Equipment_Report():
    Default_Date_today   = datetime.date.today()
    conn = sqlite3.connect("EagleBidWidget.db")

    ## Global Data Frame Personnel And Equipment
    PersonnelEquipmentGLOBAL = pd.read_sql_query("SELECT * FROM EagleBidWidget_Personnel_Equipment_GLOBAL ORDER BY `ItemIndex` ASC ;", conn)        
    PersonnelEquipmentGLOBAL = pd.DataFrame(PersonnelEquipmentGLOBAL)
    PersonnelEquipmentGLOBAL = PersonnelEquipmentGLOBAL.reset_index(drop=True)
    PersonnelEquipmentGLOBAL.rename(columns = { 'ItemIndex': 'Item Index',
                                                          'ExpenseItem':'Personnel & Equipment Expense Index',
                                                          'DailyCost':'Calculated Cost/Day',
                                                          'HourlyCost':'Calculated Cost/Hour',
                                                          'HourlyBidEntry':'Bid Entry Cost/Hour'},inplace = True)
    PersonnelEquipmentGLOBAL['']            = PersonnelEquipmentGLOBAL.shape[0]*['']
    PersonnelEquipmentGLOBAL['']            = PersonnelEquipmentGLOBAL.shape[0]*['']
    PersonnelEquipmentGLOBAL['']            = PersonnelEquipmentGLOBAL.shape[0]*['']
    PersonnelEquipmentGLOBAL['']            = PersonnelEquipmentGLOBAL.shape[0]*['']
    PersonnelEquipmentGLOBAL['']            = PersonnelEquipmentGLOBAL.shape[0]*['']
    PersonnelEquipmentGLOBAL['']            = PersonnelEquipmentGLOBAL.shape[0]*['']

    PersonnelEquipmentGLOBAL  = PersonnelEquipmentGLOBAL.loc[:,['Item Index', '' , 'Personnel & Equipment Expense Index', '', '',
                                                                'Calculated Cost/Day','', 'Calculated Cost/Hour', '',
                                                                'Bid Entry Cost/Hour', '']]

    ## Personnel And Expense Report DF
    PersonnelEXPENSEREPORT = pd.read_sql_query("SELECT * FROM EagleBidWidget_Personnal_Expense ORDER BY `Rate` DESC ;", conn)        
    PersonnelEXPENSEREPORT = pd.DataFrame(PersonnelEXPENSEREPORT)
    PersonnelEXPENSEREPORT = PersonnelEXPENSEREPORT.reset_index(drop=True)

    PersonnelEXPENSEREPORT_MAIN  = PersonnelEXPENSEREPORT.loc[:,['Mobilization','Weather','Personnel','Quantity','Rate',
                                                                 'PersonnelCostPerDay','PersonnelCostPerHour', 'MobCostPerDay',
                                                                 'MobCostPerHour','WeatherCostPerHour','StatdayCostPerHour']]
    PersonnelEXPENSEREPORT_MAIN = pd.DataFrame(PersonnelEXPENSEREPORT_MAIN)
    PersonnelEXPENSEREPORT_MAIN.rename(columns = {'Mobilization': 'Mob', 'Weather':'Weather', 'Personnel':'Personnel',
                                                  'Quantity': 'Qty', 'Rate':'Daily Rate', 'PersonnelCostPerDay':'Cost/Day',
                                                  'PersonnelCostPerHour': 'Cost/Hour', 'MobCostPerDay':'Mob/Day', 'MobCostPerHour':'Mob/Hour',
                                                  'WeatherCostPerHour': 'Weather/Hour', 'StatdayCostPerHour':'Stat/Hour'},inplace = True)  
    PersonnelEXPENSEREPORT_MAIN  = PersonnelEXPENSEREPORT_MAIN.reset_index(drop=True)
    Length_PersonnelEXPENSE_MAIN = len(PersonnelEXPENSEREPORT_MAIN)


    PersonnelEXPENSEREPORT_MAIN_RESULTS  = PersonnelEXPENSEREPORT.loc[:,['TotalPersonnal_Quantity','Currency','TotalPersonnal_CostPerDay','TotalPersonnal_CostPerHour',
                                                                         'TotalPersonnal_MobCostPerDay','TotalPersonnal_MobCostPerHour',
                                                                         'TotalPersonnal_WeatherCostPerHour','TotalPersonnal_StatdayCostPerHour']]
    PersonnelEXPENSEREPORT_MAIN_RESULTS = pd.DataFrame(PersonnelEXPENSEREPORT_MAIN_RESULTS)
    PersonnelEXPENSEREPORT_MAIN_RESULTS.rename(columns = {'TotalPersonnal_Quantity': 'Total Qty','Currency':'Currency',
                                                          'TotalPersonnal_CostPerDay':'Total Cost/Day',
                                                          'TotalPersonnal_CostPerHour':'Total Cost/Hour',
                                                          'TotalPersonnal_MobCostPerDay': 'Total Mob/Day',
                                                          'TotalPersonnal_MobCostPerHour':'Total Mob/Hour',
                                                          'TotalPersonnal_WeatherCostPerHour': 'Total Weather/Hour',
                                                          'TotalPersonnal_StatdayCostPerHour': 'Total StatDay/Hour'},inplace = True)
    PersonnelEXPENSEREPORT_MAIN_RESULTS = PersonnelEXPENSEREPORT_MAIN_RESULTS.reset_index(drop=True)
    PersonnelEXPENSEREPORT_MAIN_RESULTS = (PersonnelEXPENSEREPORT_MAIN_RESULTS.head(n=1))

    PersonnelEXPENSEREPORT_MAIN_RESULTS_1  = PersonnelEXPENSEREPORT_MAIN_RESULTS.loc[:,['Total Qty','Currency']]

    PersonnelEXPENSEREPORT_MAIN_RESULTS_2  = PersonnelEXPENSEREPORT_MAIN_RESULTS.loc[:,['Total Cost/Day', 'Total Cost/Hour',
                                                                                        'Total Mob/Day','Total Mob/Hour',
                                                                                        'Total Weather/Hour','Total StatDay/Hour']]

    PersonnelEXPENSEREPORT_MAIN_HEADER  = PersonnelEXPENSEREPORT.loc[:,['ShiftHour','WeatherStandby','WeatherRate',
                                                                        'StatdayRate','MobRate']]
    PersonnelEXPENSEREPORT_MAIN_HEADER = pd.DataFrame(PersonnelEXPENSEREPORT_MAIN_HEADER)
    PersonnelEXPENSEREPORT_MAIN_HEADER.rename(columns = { 'ShiftHour': 'Shift Hour',
                                                          'WeatherStandby':'Weather Hour',
                                                          'WeatherRate':'Weather Rate (%)',
                                                          'StatdayRate':'Stat Rate (%)',
                                                          'MobRate':'Mob Rate (%)'},inplace = True)

    PersonnelEXPENSEREPORT_MAIN_HEADER = PersonnelEXPENSEREPORT_MAIN_HEADER.reset_index(drop=True)
    PersonnelEXPENSEREPORT_MAIN_HEADER = (PersonnelEXPENSEREPORT_MAIN_HEADER.head(n=1))


    ## Equipment And Expense Report DF

    EquipmentEXPENSEREPORT = pd.read_sql_query("SELECT * FROM EagleBidWidget_Equipment_Expense ORDER BY `Rate` DESC ;", conn)        
    EquipmentEXPENSEREPORT = pd.DataFrame(EquipmentEXPENSEREPORT)
    EquipmentEXPENSEREPORT = EquipmentEXPENSEREPORT.reset_index(drop=True)

    EquipmentEXPENSEREPORT_MAIN  = EquipmentEXPENSEREPORT.loc[:,['Mobilization','Weather','Equipment','Quantity','Rate',
                                                                 'EquipmentCostPerDay','EquipmentCostPerHour', 'MobCostPerDay',
                                                                 'MobCostPerHour','WeatherCostPerHour','StatdayCostPerHour']]
    EquipmentEXPENSEREPORT_MAIN = pd.DataFrame(EquipmentEXPENSEREPORT_MAIN)
    EquipmentEXPENSEREPORT_MAIN.rename(columns = {'Mobilization': 'Mob', 'Weather':'Weather', 'Equipment':'Equipment',
                                                  'Quantity': 'Qty', 'Rate':'Daily Rate', 'EquipmentCostPerDay':'Cost/Day',
                                                  'EquipmentCostPerHour': 'Cost/Hour', 'MobCostPerDay':'Mob/Day', 'MobCostPerHour':'Mob/Hour',
                                                  'WeatherCostPerHour': 'Weather/Hour', 'StatdayCostPerHour':'Stat/Hour'},inplace = True)  
    EquipmentEXPENSEREPORT_MAIN  = EquipmentEXPENSEREPORT_MAIN.reset_index(drop=True)
    Length_EquipmentEXPENSE_MAIN = len(EquipmentEXPENSEREPORT_MAIN)

    EquipmentEXPENSEREPORT_MAIN_RESULTS  = EquipmentEXPENSEREPORT.loc[:,['TotalEquipment_Quantity','Currency','TotalEquipment_CostPerDay','TotalEquipment_CostPerHour',
                                                                         'TotalEquipment_MobCostPerDay','TotalEquipment_MobCostPerHour',
                                                                         'TotalEquipment_WeatherCostPerHour','TotalEquipment_StatdayCostPerHour']]
    EquipmentEXPENSEREPORT_MAIN_RESULTS = pd.DataFrame(EquipmentEXPENSEREPORT_MAIN_RESULTS)
    EquipmentEXPENSEREPORT_MAIN_RESULTS.rename(columns = {'TotalEquipment_Quantity': '# of EQ','Currency':'Currency',
                                                          'TotalEquipment_CostPerDay':'Total Cost/Day',
                                                          'TotalEquipment_CostPerHour':'Total Cost/Hour',
                                                          'TotalEquipment_MobCostPerDay': 'Total Mob/Day',
                                                          'TotalEquipment_MobCostPerHour':'Total Mob/Hour',
                                                          'TotalEquipment_WeatherCostPerHour': 'Total Weather/Hour',
                                                          'TotalEquipment_StatdayCostPerHour': 'Total StatDay/Hour'},inplace = True)
    EquipmentEXPENSEREPORT_MAIN_RESULTS = EquipmentEXPENSEREPORT_MAIN_RESULTS.reset_index(drop=True)
    EquipmentEXPENSEREPORT_MAIN_RESULTS = (EquipmentEXPENSEREPORT_MAIN_RESULTS.head(n=1))

    EquipmentEXPENSEREPORT_MAIN_RESULTS_1  = EquipmentEXPENSEREPORT_MAIN_RESULTS.loc[:,['# of EQ','Currency']]

    EquipmentEXPENSEREPORT_MAIN_RESULTS_2  = EquipmentEXPENSEREPORT_MAIN_RESULTS.loc[:,['Total Cost/Day', 'Total Cost/Hour',
                                                                                        'Total Mob/Day','Total Mob/Hour',
                                                                                        'Total Weather/Hour','Total StatDay/Hour']]

    EquipmentEXPENSEREPORT_MAIN_HEADER  = EquipmentEXPENSEREPORT.loc[:,['ShiftHour','WeatherStandby','WeatherRate',
                                                                        'StatdayRate','MobRate']]
    EquipmentEXPENSEREPORT_MAIN_HEADER = pd.DataFrame(EquipmentEXPENSEREPORT_MAIN_HEADER)
    EquipmentEXPENSEREPORT_MAIN_HEADER.rename(columns = { 'ShiftHour': 'Shift Hour',
                                                          'WeatherStandby':'Weather Hour',
                                                          'WeatherRate':'Weather Rate (%)',
                                                          'StatdayRate':'Stat Rate (%)',
                                                          'MobRate':'Mob Rate (%)'},inplace = True)

    EquipmentEXPENSEREPORT_MAIN_HEADER = EquipmentEXPENSEREPORT_MAIN_HEADER.reset_index(drop=True)
    EquipmentEXPENSEREPORT_MAIN_HEADER = (EquipmentEXPENSEREPORT_MAIN_HEADER.head(n=1))

    conn.commit()
    conn.close()

    Set_Page_Break = (Length_PersonnelEXPENSE_MAIN + Length_EquipmentEXPENSE_MAIN) + 21
            
    ## Exporting Generated Report        
    def get_ReportGen_datetime():
        return  "- Eagle Personnel And Equipment Bid Summary Report - " + str(Default_Date_today) + ".xlsx"

    root = Tk()
    root.filename = tkinter.filedialog.asksaveasfilename(title = "Select File Name To Export Personnel And Equipment Bid Summary Report" ,
                                                         filetypes = (("Excel file",".xlsx"),("Excel file",".xlsx")))
    if len(root.filename) >0:
        GenBidReport        = get_ReportGen_datetime()
        GenBidReport_path   = root.filename + GenBidReport
        XLSX_writer_GenBidReport = pd.ExcelWriter(GenBidReport_path)                
        header_PersonnelEquipment = '&L&G'+'&R&18 Eagle Canada Bid Expense Report'+ '\n'+'Category: Personnel And Equipment'
        footer = ('&CEAGLE CANADA SEISMIC SERVICES ULC' + '\n'
                  + '6806 Railway Street SE Calgary, AB T2H 3A8' + '\n' +
                    'Ph: (403) 263-7770  Fax: 403 263 7776 Web : www.eaglecanada.ca')
        Row_Start = 2
        PersonnelEXPENSEREPORT_MAIN.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, startrow = Row_Start)

        workbook                             = XLSX_writer_GenBidReport.book
        worksheet_Personnel_Equipment = XLSX_writer_GenBidReport.sheets['Personnel_Equipment_BidReport']
        worksheet_Personnel_Equipment.set_margins(0.7, 0.4, 1.0, 0.7)        
        worksheet_Personnel_Equipment.set_header(header_PersonnelEquipment,{'image_left':"eagle logo.jpg"})
        worksheet_Personnel_Equipment.set_footer(footer)
        workbook.formats[0].set_align('center')
        workbook.formats[0].set_font_size(11)
        workbook.formats[0].set_bold(True)
        workbook.formats[0].set_border(4)    
        worksheet_Personnel_Equipment.print_area(0,0,Set_Page_Break,10)
        worksheet_Personnel_Equipment.print_across()
        worksheet_Personnel_Equipment.fit_to_pages(1, 1)
        worksheet_Personnel_Equipment.set_paper(9)
        worksheet_Personnel_Equipment.set_start_page(1)
        worksheet_Personnel_Equipment.hide_gridlines(0)
        worksheet_Personnel_Equipment.set_v_pagebreaks([Set_Page_Break])
        worksheet_Personnel_Equipment.set_page_view()    
        worksheet_Personnel_Equipment.set_column('E:I',16)
        worksheet_Personnel_Equipment.set_column('J:K',20)
        worksheet_Personnel_Equipment.set_column('A:B',8)
        worksheet_Personnel_Equipment.set_column('C:C',24)
        worksheet_Personnel_Equipment.set_column('D:D',12)
        cell_format_1 = workbook.add_format({
                                            'bold': True,
                                            'text_wrap': True,
                                            'valign': 'top'})
        cell_format_1.set_align('center')
        cell_format_1.set_font_size(12)
        cell_format_2 = workbook.add_format({
                                            'bold': True,
                                            'text_wrap': True,
                                            'valign': 'top'})
        cell_format_2.set_align('left')
        cell_format_2.set_font_size(14)
        
        worksheet_Personnel_Equipment.merge_range(0,0,1,5, "Personnel Profile And Expense Calculation :", cell_format_2)
        worksheet_Personnel_Equipment.merge_range((Row_Start + Length_PersonnelEXPENSE_MAIN+1),0,(Row_Start + Length_PersonnelEXPENSE_MAIN+2),2, "Total Personnel Expense Summary :", cell_format_2)    
        PersonnelEXPENSEREPORT_MAIN_RESULTS_1.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, header=True, startcol = 3, startrow=(Row_Start+Length_PersonnelEXPENSE_MAIN+1))
        PersonnelEXPENSEREPORT_MAIN_RESULTS_2.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, header=True, startcol = 5, startrow=(Row_Start+Length_PersonnelEXPENSE_MAIN+1))
        PersonnelEXPENSEREPORT_MAIN_HEADER.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, header=True, startcol = 6, startrow=0)

        Row_Start_EQ      = (Row_Start+Length_PersonnelEXPENSE_MAIN+1)
        Row_Start_EQ_Main = Row_Start_EQ + 5

        merge_format1 = workbook.add_format({'bold':     True,
                                            'border':   1,
                                            'align':    'center',
                                            'valign':   'vcenter',
                                            'fg_color': '#cccccc',})
        worksheet_Personnel_Equipment.merge_range((Row_Start_EQ)+2,0,(Row_Start_EQ)+2,10, "", merge_format1)    
        EquipmentEXPENSEREPORT_MAIN.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, startrow = Row_Start_EQ_Main)
        worksheet_Personnel_Equipment.merge_range((Row_Start_EQ)+3,0,(Row_Start_EQ)+4,5, "Equipment Profile And Expense Calculation :", cell_format_2)
        worksheet_Personnel_Equipment.merge_range((Row_Start_EQ_Main + Length_EquipmentEXPENSE_MAIN + 1),0,(Row_Start_EQ_Main + Length_EquipmentEXPENSE_MAIN + 2),2, "Total Equipment Expense Summary :", cell_format_2)
        EquipmentEXPENSEREPORT_MAIN_RESULTS_1.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, header=True, startcol = 3, startrow=(Row_Start_EQ_Main + Length_EquipmentEXPENSE_MAIN + 1))
        EquipmentEXPENSEREPORT_MAIN_RESULTS_2.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, header=True, startcol = 5, startrow=(Row_Start_EQ_Main + Length_EquipmentEXPENSE_MAIN + 1))
        EquipmentEXPENSEREPORT_MAIN_HEADER.to_excel(XLSX_writer_GenBidReport,'Personnel_Equipment_BidReport',index=False, header=True, startcol = 6, startrow=(Row_Start_EQ)+3)


        Row_Start_GLOBAL      = ((Row_Start_EQ_Main + Length_EquipmentEXPENSE_MAIN + 1)+1)
        Row_Start_GLOBAL_Main = Row_Start_GLOBAL + 2
        merge_format2 = workbook.add_format({'bold':     True,
                                            'border':   2,
                                            'align':    'center',
                                            'valign':   'vcenter',
                                            'fg_color': '#cccccc',})
        merge_format2.set_font_size(16)
        worksheet_Personnel_Equipment.merge_range((Row_Start_GLOBAL)+1,0,(Row_Start_GLOBAL)+3,10, " COMBINED PERSONNEL AND EQUIPMENT EXPENSE SUMMARY AND BID ENTRY", merge_format2)
        Numberof_Row = 5
        StartRow = (Row_Start_GLOBAL_Main)+2
        for i in range(Numberof_Row):
            worksheet_Personnel_Equipment.merge_range(i+StartRow, 0, i+StartRow, 1, '')
            worksheet_Personnel_Equipment.merge_range(i+StartRow, 2, i+StartRow, 4, '')
            worksheet_Personnel_Equipment.merge_range(i+StartRow, 5, i+StartRow, 6, '')
            worksheet_Personnel_Equipment.merge_range(i+StartRow, 7, i+StartRow, 8, '')
            worksheet_Personnel_Equipment.merge_range(i+StartRow, 9, i+StartRow, 10, '')       
        PersonnelEquipmentGLOBAL.to_excel(XLSX_writer_GenBidReport, 'Personnel_Equipment_BidReport', index=False, merge_cells=True, header=True, startcol = 0, startrow=(Row_Start_GLOBAL_Main)+2)
        worksheet_Personnel_Equipment.merge_range((Row_Start_GLOBAL + Numberof_Row+4),0,(Row_Start_GLOBAL + Numberof_Row+5),10, "END OF PERSONNEL AND EQUIPMENT EXPENSE REPORT", merge_format2)

        ## XLSX Writer Save And Close
        XLSX_writer_GenBidReport.save()
        XLSX_writer_GenBidReport.close()
        tkinter.messagebox.showinfo("Eagle Personnel And Equipment Bid Summary Report Export Message","Personnel And Equipment Bid Summary Report Saved as Excel")
        root.destroy()
    else:
        tkinter.messagebox.showinfo("Eagle Personnel And Equipment Bid Summary Report Message","Please Select Personnel And Equipment Bid Summary Report File Name To Export")
        root.destroy()
        






















