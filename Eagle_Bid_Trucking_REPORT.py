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

def Export_Trucking_Report():
    Default_Date_today   = datetime.date.today()
    conn = sqlite3.connect("EagleBidWidget.db")

    ## Global Trucking Report
    TruckingEquipmentGLOBAL = pd.read_sql_query("SELECT * FROM EagleBidWidget_Trucking_GLOBAL ORDER BY `ItemIndex` ASC ;", conn)        
    TruckingEquipmentGLOBAL = pd.DataFrame(TruckingEquipmentGLOBAL)
    TruckingEquipmentGLOBAL = TruckingEquipmentGLOBAL.reset_index(drop=True)
    TruckingEquipmentGLOBAL.rename(columns = {'ItemIndex': 'Bid Item Index',
                                              'AddDeductionPercent' : 'Add/Deduct (%)',
                                              'TruckingItem':'Item Name And Description',
                                              'TotalCost':'Total Trucking Cost',
                                              'CostPerSP':'Trucking Cost/SP',
                                              'CostPerRP':'Trucking Cost/RP',
                                              'CostPerKM':'Trucking Cost/KM'},inplace = True)
    TruckingEquipmentGLOBAL['']            = TruckingEquipmentGLOBAL.shape[0]*['']


    TruckingEquipmentGLOBAL  = TruckingEquipmentGLOBAL.loc[:,['Bid Item Index', 'Item Name And Description', '', 'Add/Deduct (%)', 'Total Trucking Cost',
                                                              'Trucking Cost/SP', 'Trucking Cost/RP', 'Trucking Cost/KM']]

    ## Trucking Main Report DF
    TruckingEXPENSEREPORT = pd.read_sql_query("SELECT * FROM EagleBidWidget_Trucking_Expense ORDER BY `RatePerHour` DESC ;", conn)        
    TruckingEXPENSEREPORT = pd.DataFrame(TruckingEXPENSEREPORT)
    TruckingEXPENSEREPORT = TruckingEXPENSEREPORT.reset_index(drop=True)

    ## Trucking Main Frame Body
    TruckingEXPENSEREPORT_MAIN  = TruckingEXPENSEREPORT.loc[:,['TruckingEquipment', 'Quantity',       'ShiftHour',      'RatePerHour',
                                                               'TotalCost',         'TotalCostPerSP', 'TotalCostPerRP', 'TotalCostPerKM']]
    TruckingEXPENSEREPORT_MAIN.rename(columns = {'TruckingEquipment':'Trucking Equipment Name',
                                                 'Quantity'         :'Quantity',
                                                 'ShiftHour'        :'Shift Hour',
                                                 'RatePerHour'      :'Rate/Hour',
                                                 'TotalCost'        :'Total Trucking Cost/Shift',
                                                 'TotalCostPerSP'   :'Trucking Cost/Shot Points',
                                                 'TotalCostPerRP'   :'Trucking Cost/Receiver Points',
                                                 'TotalCostPerKM'   :'Trucking Cost/Kilometers (Km)'},inplace = True)
    TruckingEXPENSEREPORT_MAIN  = pd.DataFrame(TruckingEXPENSEREPORT_MAIN)
    TruckingEXPENSEREPORT_MAIN  = TruckingEXPENSEREPORT_MAIN.reset_index(drop=True)
    Length_Trucking_MAIN        = len(TruckingEXPENSEREPORT_MAIN)

    ## Trucking Main Frame Results

    Trucking_MAIN_RESULTS  = TruckingEXPENSEREPORT.loc[:,['SUMTotalQuantity', 'Currency', 'SUMTotalCost', 'SUMTotalCostPerSP',
                                                          'SUMTotalCostPerRP','SUMTotalCostPerKM']]
    Trucking_MAIN_RESULTS = pd.DataFrame(Trucking_MAIN_RESULTS)
    Trucking_MAIN_RESULTS.rename(columns = {'SUMTotalQuantity': 'Total Qty', 'Currency':'Rate Currency',
                                            'SUMTotalCost':     'Sum Total Trucking Cost',
                                            'SUMTotalCostPerSP':'Sum Total Cost/Shot Points',
                                            'SUMTotalCostPerRP':'Sum Total Cost/Rec Points',
                                            'SUMTotalCostPerKM':'Sum Total Cost/Kms'},inplace = True)
    Trucking_MAIN_RESULTS     = Trucking_MAIN_RESULTS.reset_index(drop=True)
    Trucking_MAIN_RESULTS     = Trucking_MAIN_RESULTS.head(n=1)
    Trucking_MAIN_RESULTS[''] = Trucking_MAIN_RESULTS.shape[0]*['']
    Trucking_MAIN_RESULTS_1   = Trucking_MAIN_RESULTS.loc[:,['Total Qty', '', 'Rate Currency']]
    Trucking_MAIN_RESULTS_2   = Trucking_MAIN_RESULTS.loc[:,['Sum Total Trucking Cost', 'Sum Total Cost/Shot Points',
                                                            'Sum Total Cost/Rec Points','Sum Total Cost/Kms']]
    ## Trucking Main Frame Headers
    TruckingEXPENSEREPORT_MAIN_HEADER  = TruckingEXPENSEREPORT.loc[:,['TotalPlannedSP','TotalPlannedRP','TotalLinearKMS']]
    TruckingEXPENSEREPORT_MAIN_HEADER = pd.DataFrame(TruckingEXPENSEREPORT_MAIN_HEADER)
    TruckingEXPENSEREPORT_MAIN_HEADER.rename(columns = { 'TotalPlannedSP':'Total Planned Shot Points',
                                                         'TotalPlannedRP':'Total Planned Receiver Points',
                                                         'TotalLinearKMS':'Total Linear Kilometers (Km)'},inplace = True)
    TruckingEXPENSEREPORT_MAIN_HEADER = TruckingEXPENSEREPORT_MAIN_HEADER.reset_index(drop=True)
    TruckingEXPENSEREPORT_MAIN_HEADER = (TruckingEXPENSEREPORT_MAIN_HEADER.head(n=1))

    conn.commit()
    conn.close()

            
    ## Exporting Generated Report        
    def get_ReportGen_datetime():
        return  "- Eagle Trucking Equipment Bid Summary Report - " + str(Default_Date_today) + ".xlsx"

    root = Tk()
    root.filename = tkinter.filedialog.asksaveasfilename(title = "Select File Name To Export Trucking Equipment Bid Summary Report" ,
                                                         filetypes = (("Excel file",".xlsx"),("Excel file",".xlsx")))
    if len(root.filename) >0:
        GenBidReport        = get_ReportGen_datetime()
        GenBidReport_path   = root.filename + GenBidReport
        XLSX_writer_GenBidReport = pd.ExcelWriter(GenBidReport_path)                
        header_Trucking = '&L&G'+'&R&18 Eagle Canada Bid Expense Report'+ '\n'+'Category: Trucking Equipment'
        footer = ('&CEAGLE CANADA SEISMIC SERVICES ULC' + '\n'
                  + '6806 Railway Street SE Calgary, AB T2H 3A8' + '\n' +
                    'Ph: (403) 263-7770  Fax: 403 263 7776 Web : www.eaglecanada.ca')
        Row_Start      = 2
        Set_Page_Break = 25
        TruckingEXPENSEREPORT_MAIN.to_excel(XLSX_writer_GenBidReport,'Trucking_BidReport',index=False, startrow = Row_Start)

        workbook                             = XLSX_writer_GenBidReport.book
        worksheet_Trucking = XLSX_writer_GenBidReport.sheets['Trucking_BidReport']
        worksheet_Trucking.set_margins(0.7, 0.4, 1.0, 0.7)        
        worksheet_Trucking.set_header(header_Trucking,{'image_left':"eagle logo.jpg"})
        worksheet_Trucking.set_footer(footer)
        workbook.formats[0].set_align('center')
        workbook.formats[0].set_font_size(11)
        workbook.formats[0].set_bold(True)
        workbook.formats[0].set_border(4)    
        worksheet_Trucking.print_area(0,0,Set_Page_Break,7)
        worksheet_Trucking.print_across()
        worksheet_Trucking.fit_to_pages(1, 1)
        worksheet_Trucking.set_paper(9)
        worksheet_Trucking.set_start_page(1)
        worksheet_Trucking.hide_gridlines(0)
        worksheet_Trucking.set_v_pagebreaks([Set_Page_Break])    
        
        worksheet_Trucking.set_column('A:A',28)
        worksheet_Trucking.set_column('B:B',16)
        worksheet_Trucking.set_column('C:D',16)
        worksheet_Trucking.set_column('E:H',29)
            
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
        
        worksheet_Trucking.merge_range(0,0,1,4, "Trucking Equipment Profile And Expense Calculation :", cell_format_2)


        worksheet_Trucking.merge_range((Row_Start + Length_Trucking_MAIN + 1),0,(Row_Start + Length_Trucking_MAIN + 2),0, " Sum Trucking Expenses :", cell_format_2)
        Trucking_MAIN_RESULTS_1.to_excel(XLSX_writer_GenBidReport,'Trucking_BidReport',index=False, header=True, startcol = 1, startrow=(Row_Start+Length_Trucking_MAIN+1))
        Trucking_MAIN_RESULTS_2.to_excel(XLSX_writer_GenBidReport,'Trucking_BidReport',index=False, header=True, startcol = 4, startrow=(Row_Start+Length_Trucking_MAIN+1))
        TruckingEXPENSEREPORT_MAIN_HEADER.to_excel(XLSX_writer_GenBidReport,'Trucking_BidReport',index=False, header=True, startcol = 5, startrow=0)

       

        Row_Start_GLOBAL      = ((Row_Start + Length_Trucking_MAIN + 1)+1)
        merge_format2 = workbook.add_format({'bold':     True,
                                            'border':   2,
                                            'align':    'center',
                                            'valign':   'vcenter',
                                            'fg_color': '#cccccc',})
        merge_format2.set_font_size(14)
        worksheet_Trucking.merge_range((Row_Start_GLOBAL)+2,0,(Row_Start_GLOBAL)+3,7, " TRUCKING EQUIPMENTS EXPENSE SUMMARY", merge_format2)
        Numberof_Row = len(TruckingEquipmentGLOBAL) + 1

        worksheet_Trucking.merge_range((Row_Start_GLOBAL)+4, 1, (Row_Start_GLOBAL)+4, 2, '')
        worksheet_Trucking.merge_range((Row_Start_GLOBAL)+5, 1, (Row_Start_GLOBAL)+5, 2, '')
        TruckingEquipmentGLOBAL.to_excel(XLSX_writer_GenBidReport, 'Trucking_BidReport', index=False, merge_cells=True, header=True, startcol = 0, startrow=(Row_Start_GLOBAL)+4)

        worksheet_Trucking.merge_range((Row_Start_GLOBAL + Numberof_Row+5),0,(Row_Start_GLOBAL + Numberof_Row+6),7, "END OF TRUCKING EQUIPMENT EXPENSE REPORT", merge_format2)

        ## XLSX Writer Save And Close
        XLSX_writer_GenBidReport.save()
        XLSX_writer_GenBidReport.close()
        tkinter.messagebox.showinfo("Eagle Trucking Bid Summary Report Export Message","Trucking Equipment Bid Summary Report Saved as Excel")
        root.destroy()
    else:
        tkinter.messagebox.showinfo("Eagle Trucking Equipment Bid Summary Report Message","Please Select Trucking Equipment Bid Summary Report File Name To Export")
        root.destroy()
        






















