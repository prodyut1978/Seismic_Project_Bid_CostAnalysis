import sqlite3
#backend

## ------------------------------- DATABASE DEFINE-----------------------------------------------------
def EagleProjectBidLogData():
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()

                                  #################################### PERSONNEL DATABASE ##############################

    ## Input User Database For Personnel   
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Personnal_Entry (ShiftHour REAL, WeatherStandby REAL, WeatherRate REAL, StatdayRate REAL)")

    ## Personnel Database For Calculation Expense
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Personnal_Log (Mobilization TEXT NOT NULL, Weather TEXT NOT NULL, Personnel TEXT NOT NULL, Quantity INTEGER NOT NULL, Rate REAL NOT NULL)")   

    ## Generated Personnel Expense Database
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Personnal_Expense (Mobilization TEXT, Weather TEXT, Personnel TEXT, Quantity INTEGER, Rate REAL,\
                 PersonnelCostPerDay REAL, PersonnelCostPerHour REAL, MobCostPerDay REAL, MobCostPerHour REAL, WeatherCostPerHour REAL, StatdayCostPerHour REAL,\
                 ShiftHour REAL, WeatherStandby REAL, WeatherRate REAL, StatdayRate REAL, MobRate REAL, Currency TEXT, TotalPersonnal_Quantity INTEGER,\
                 TotalPersonnal_CostPerDay REAL, TotalPersonnal_CostPerHour REAL, TotalPersonnal_MobCostPerDay REAL, TotalPersonnal_MobCostPerHour REAL,\
                 TotalPersonnal_WeatherCostPerHour REAL, TotalPersonnal_StatdayCostPerHour REAL)")


                                 #################################### EQUIPMENT DATABASE ##############################


    ## Input User Database For Equipment     
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Equipment_Entry (ShiftHour REAL, WeatherStandby REAL, WeatherRate REAL, StatdayRate REAL)")

    ## Equipment Database For Calculation Expense
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Equipment_Log (Mobilization TEXT NOT NULL, Weather TEXT NOT NULL, Equipment TEXT NOT NULL, Quantity INTEGER NOT NULL, Rate REAL NOT NULL)")   

    ## Generated Equipment Expense Database
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Equipment_Expense (Mobilization TEXT, Weather TEXT, Equipment TEXT, Quantity INTEGER, Rate REAL,\
                 EquipmentCostPerDay REAL, EquipmentCostPerHour REAL, MobCostPerDay REAL, MobCostPerHour REAL, WeatherCostPerHour REAL, StatdayCostPerHour REAL,\
                 ShiftHour REAL, WeatherStandby REAL, WeatherRate REAL, StatdayRate REAL, MobRate REAL, Currency TEXT, TotalEquipment_Quantity INTEGER,\
                 TotalEquipment_CostPerDay REAL, TotalEquipment_CostPerHour REAL, TotalEquipment_MobCostPerDay REAL, TotalEquipment_MobCostPerHour REAL,\
                 TotalEquipment_WeatherCostPerHour REAL, TotalEquipment_StatdayCostPerHour REAL)")

                                #################################### GLOBAL PERSONNEL AND EQUIPMENT DATABASE ##############################

    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Personnel_Equipment_GLOBAL (ItemIndex INTEGER, ExpenseItem TEXT, DailyCost REAL, HourlyCost REAL, HourlyBidEntry REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_ClientSupply_GLOBAL (ClientSuppliedItem TEXT, CostHour REAL, MobCostHour REAL, WeatherCostHour REAL, StatDayCostHour REAL)")    
    

                                  #################################### TRUCKING DATABASE ##############################

    ## Input User Database For Personnel   
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Trucking_Entry (TotalPlannedSP INTEGER, TotalPlannedRP INTEGER, TotalLinearKMS REAL)")

    ## Personnel Database For Calculation Expense
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Trucking_Log (TruckingEquipment TEXT NOT NULL, Quantity INTEGER, ShiftHour REAL, RatePerHour REAL)")   

    ## Generated Personnel Expense Database
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Trucking_Expense (TruckingEquipment TEXT NOT NULL, Quantity INTEGER, ShiftHour REAL, RatePerHour REAL,\
                TotalCost REAL, TotalCostPerSP REAL, TotalCostPerRP REAL, TotalCostPerKM REAL,\
                TotalPlannedSP INTEGER, TotalPlannedRP INTEGER, TotalLinearKMS REAL, Currency TEXT,\
                SUMTotalQuantity INTEGER, SUMTotalCost REAL, SUMTotalCostPerSP REAL, SUMTotalCostPerRP REAL, SUMTotalCostPerKM REAL)")

                            #################################### GLOBAL  TRUCKING DATABASE ##############################
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Trucking_GLOBAL (ItemIndex, AddDeductionPercent REAL, TruckingItem TEXT, TotalCost REAL, CostPerSP REAL, CostPerRP REAL, CostPerKM REAL)")






    con.commit()
    con.close()



#################################### MASTER BIDING DATABASE ##############################

def EagleProjectBidLogData_MasterBackup():
    con= sqlite3.connect("EagleBidWidgetMasterBackup.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Personnal_Log_Master (Mobilization TEXT NOT NULL, Weather TEXT NOT NULL, Personnel TEXT NOT NULL, Quantity INTEGER NOT NULL, Rate REAL NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Equipment_Log_Master (Mobilization TEXT NOT NULL, Weather TEXT NOT NULL, Equipment TEXT NOT NULL, Quantity INTEGER NOT NULL, Rate REAL NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS EagleBidWidget_Trucking_Log_Master  (TruckingEquipment TEXT NOT NULL, Quantity INTEGER, ShiftHour REAL, RatePerHour REAL)")   
    con.commit()
    con.close()

###------------------------------ END OF DATABASE DEFINE--------------------------------------------------


def addRec_Personnal_Log(Mobilization, Weather, Personnel, Quantity, Rate):
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()    
    cur.execute("INSERT INTO EagleBidWidget_Personnal_Log VALUES (?,?,?,?,?)",(Mobilization, Weather, Personnel, Quantity, Rate))
    con.commit()
    con.close()

def viewPersonnal_LogData():
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM EagleBidWidget_Personnal_Log ORDER BY `Rate` DESC ")
    rows=cur.fetchall()
    con.close()
    return rows

def addRec_Equipment_Log(EQMobilization, EQWeather, EQEquipment, EQQuantity, EQRate):
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()    
    cur.execute("INSERT INTO EagleBidWidget_Equipment_Log VALUES (?,?,?,?,?)",(EQMobilization, EQWeather, EQEquipment, EQQuantity, EQRate))
    con.commit()
    con.close()

def viewEquipment_LogData():
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM EagleBidWidget_Equipment_Log ORDER BY `Rate` DESC ")
    rows=cur.fetchall()
    con.close()
    return rows

def addRec_Personnel_Equipment_GLOBAL(Index, ItemName, costDay, costHour, MODIFYBID):
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()    
    cur.execute("INSERT INTO EagleBidWidget_Personnel_Equipment_GLOBAL VALUES (?,?,?,?,?)",(Index, ItemName, costDay, costHour, MODIFYBID))
    con.commit()
    con.close()

def viewPersonnel_Equipment_GLOBAL():
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM EagleBidWidget_Personnel_Equipment_GLOBAL ORDER BY `ItemIndex` ASC ")
    rows=cur.fetchall()
    con.close()
    return rows



def addRec_Trucking_Log(TruckingEQ, Quantity, ShiftHours, RateHours):
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()    
    cur.execute("INSERT INTO EagleBidWidget_Trucking_Log VALUES (?,?,?,?)",(TruckingEQ, Quantity, ShiftHours, RateHours))
    con.commit()
    con.close()

def viewTrucking_LogData():
    con= sqlite3.connect("EagleBidWidget.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM EagleBidWidget_Trucking_Log ORDER BY `RatePerHour` DESC ")
    rows=cur.fetchall()
    con.close()
    return rows








EagleProjectBidLogData()
EagleProjectBidLogData_MasterBackup()
