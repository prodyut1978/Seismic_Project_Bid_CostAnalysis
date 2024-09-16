import pandas as pd

##Crew_List    = ["101", "102", "103", "104", "105", "106", "107", "108"]
##self.lblCrew = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "1. Crew :", padx =1, pady= 1, bg = "cadet blue")
##self.lblCrew.grid(row =0, column = 0, sticky =W)
##self.txtCrew = ttk.Combobox(DataFrameLEFT, font=('aerial', 10, 'bold'), textvariable = Crew, width = 6)
##self.txtCrew.grid(row =0, column = 1)
##self.txtCrew['values'] = sorted(list(Crew_List))
##
##Prov_List    = ["AB", "BC", "SK", "MB","ON", "NT", "YT", "NB", "NL", "PE", "NS", "QC", "NU"]
##self.lblProvince = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "2. Province :", padx =1, pady= 1, bg = "cadet blue")
##self.lblProvince.grid(row =1, column = 0, sticky =W)
##self.txtProvince = ttk.Combobox(DataFrameLEFT, font=('aerial', 10, 'bold'), textvariable = Province, width = 6)
##self.txtProvince.grid(row =1, column = 1)
##self.txtProvince['values'] = sorted(list(Prov_List))
##
##Prov_Tax    = [5.0, 7.0, 6.0, 8.0, 13.0, 15.0]
##self.lblProvinceTax = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "3. Province Tax (%) :", padx =1, pady= 1, bg = "cadet blue")
##self.lblProvinceTax.grid(row =2, column = 0, sticky =W)
##self.txtProvinceTax = ttk.Combobox(DataFrameLEFT, font=('aerial', 10, 'bold'), textvariable = ProvinceTax, width = 6)
##self.txtProvinceTax.grid(row =2, column = 1)
##self.txtProvinceTax['values'] = sorted(list(Prov_Tax))
##
##Currency_List    = ["CAD", "USD"]
##self.lblCurrency = Label(DataFrameLEFT, font=('aerial', 10, 'bold'), text = "4. Currency :", padx =1, pady= 1, bg = "cadet blue")
##self.lblCurrency.grid(row =3, column = 0, sticky =W)
##self.txtCurrency = ttk.Combobox(DataFrameLEFT, font=('aerial', 10, 'bold'), textvariable = Currency, width = 6)
##self.txtCurrency.grid(row =3, column = 1)
##self.txtCurrency['values'] = sorted(list(Currency_List))


txtEQEquipment_List = ["Rental Recording System","Rental Geophone","Personal Trucks","Tapes\Supplies","Equipment R&M","Fleet R&M","Fuel - Recording","Fuel - Vibes","One Time Cost",
                                 "Subsistence","Motel-Crew Office","Motel - Single Rooms","Motel - Double Rooms"]

PersonnelDF = {'Mobilization': ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
              'Weather': ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
              'Personnel': ["Party Manager","Assist.Party Manager","Field Service Tech","Merge Operator","FMC Operator","Mechanic","HSE Advisor","Administrator","Co-ordinator",
                                 "Shooters","Shooter's Helpers","Vibrator Technician","Vibrator Operators","Fuel Driver","Trouble Shooters/Viewers","Line Boss","Recorder Helpers",
                                 "Staging Helpers","Night Watchman","Rotation"],
              'Quantity': [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
              'Rate': [800.00,650.00,650.00,650.00,600.00,600.00,600.00,450.00,500.00,450.00,400.00,600.00,450.00,450.00,450.00,450.00,375.00,375.00,400.00,100.00]}

PersonnelDF = pd.DataFrame(PersonnelDF, columns = ['Mobilization', 'Weather', 'Personnel', 'Quantity','Rate'])
PersonnelDF = PersonnelDF.reset_index(drop=True)



MakeEquipmentDF = {'Mobilization':    ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                   'Weather':         ["Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y"],
                   'Equipment': ["Rental Recording System", "Rental Geophone", "Rental Box Unit (3C)", "Rental Box Unit (1C)", "Rental Box Battery", "Rental Blaster",
                                         "Personal Trucks", "Tapes\Supplies", "Equipment R&M", "Fleet R&M", "Fuel - Recording", "Fuel - Vibes",
                                         "One Time Cost", "Subsistence", "Motel-Crew Office", "Motel - Single Rooms", "Motel - Double Rooms"],
                   'Quantity': [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                   'Rate':     [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 110.0, 500.0, 1000.0, 1000.0, 150.0, 400.0, 0.0, 50.0, 125.0, 125.0, 125.0]}
MakeEquipmentDF = pd.DataFrame(MakeEquipmentDF, columns = ['Mobilization', 'Weather', 'Equipment', 'Quantity','Rate'])
MakeEquipmentDF = MakeEquipmentDF.reset_index(drop=True)
MakeEquipmentDF_Length = len(MakeEquipmentDF)
