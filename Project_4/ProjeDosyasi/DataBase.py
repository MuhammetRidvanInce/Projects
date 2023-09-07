# from ClassandFunctions import *
import tkinter
from tkinter import ttk
import mysql.connector


# Tablolar
AlanlarTablosu = "areas_table"
AlanTipiTablosu = "areatypes_table"
MarketTablosu = "markets_table"
OyuncularTablosu = "players_table"
EmlakTablosu = "realestates_tables"
RollerTablosu = "roles_table"
MagazaTablosu = "shoppingcenters_table"

AlanTablo = {"MARKET": "markets_table", "MAĞAZA": "shoppingcenters_table", "EMLAK": "realestates_tables"}
AreaTypesTableDict = {"ARSA": 1, "MARKET": 2, "MAĞAZA": 3, "EMLAK":4}
mydb = mysql.connector.connect( host = "localhost", user = "root", password = "145353", database = "metalanddb")


def DropTables():

    tables = ["areas_table", "areatypes_table", "markets_table", "players_table",
            "realestates_tables", "roles_table", "shoppingcenters_table"]

    # mydb = mysql.connector.connect(
    #     host = "localhost",
    #     user = "root",
    #     password = "145353",
    #     database = "metalanddb"
    # )


    mycursor = mydb.cursor()
    for i in tables:
        sql = "DROP TABLE IF EXISTS " + i
        mycursor.execute(sql)

def GenerateTables():
     
    # mydb = mysql.connector.connect( host = "localhost", user = "root", password = "145353", database = "metalanddb")

    mycursor = mydb.cursor()

    tables = ["areas_table", "areatypes_table", "markets_table", "players_table",
            "realestates_tables", "roles_table", "shoppingcenters_table"]

    for i in tables:

        if i == "areas_table":
            sql = "CREATE TABLE {} (Areaid INT, AreaTypeid INT, Ownerid INT, Value INT, Rented TINYINT, Renterid INT)".format(i)
            mycursor.execute(sql)

        elif i == "areatypes_table":
            sql = "CREATE TABLE {} (AreaTypeid INT, AreaType VARCHAR(255))".format(i)
            mycursor.execute(sql)

        elif i == "markets_table":
            sql = "CREATE TABLE {} (Marketid INT, Capacity INT, WorkerNumber INT, Grade INT, Rent FLOAT, FixIncome FLOAT, FoodFee FLOAT, MarketWage FLOAT, Areaid INT )".format(i)
            mycursor.execute(sql)
        
        elif i == "shoppingcenters_table":
            sql = "CREATE TABLE {} (ShoppingCenterid INT, Capacity INT, WorkerNumber INT, Grade INT, Rent FLOAT,\
                  FixIncome FLOAT, GoodFee FLOAT, ShoppingWage FLOAT, Areaid INT )".format(i)
            mycursor.execute(sql)

        elif i == "realestates_tables":
            sql = "CREATE TABLE {} (RealEstateid INT, Capacity INT, WorkerNumber INT, Grade INT, Rent FLOAT, FixIncome FLOAT, RentCommission FLOAT, \
                SoldCommission FLOAT, RealEstateWage FLOAT, Areaid INT)".format(i)
            mycursor.execute(sql)

        elif i == "players_table":
            sql = "CREATE TABLE {} (Playerid INT, Roleid INT, Name VARCHAR(255), Surname VARCHAR(255), Username VARCHAR(255), \
                  Password INT, Workplaceid INT, Money FLOAT, Eatings INT, Goods INT)".format(i)
            mycursor.execute(sql)
        
        elif i == "roles_table":
            sql = "CREATE TABLE {} (Roleid INT, Role VARCHAR(255))".format(i)
            mycursor.execute(sql)

    
    AreaTypeSql = "INSERT INTO areatypes_table (AreaTypeid, AreaType) VALUES (%s, %s)"
    ValuesAreaTypeSql = [[1, "ARSA"], [2, "MARKET"], [3, "MAĞAZA"], [4, "EMLAK"]]
    RoleSql = "INSERT INTO roles_table (Roleid, Role) VALUES (%s, %s)"
    ValuesRoleSql = [[1, "Yönetici"], [2, "Oyuncu"]]

    for value in ValuesAreaTypeSql:
        mycursor.execute(AreaTypeSql, value)
        mydb.commit()

    for value in ValuesRoleSql:
        mycursor.execute(RoleSql, value)
        mydb.commit()

def insertinfo(table, values):

    # mydb = mysql.connector.connect(
    #     host = "localhost",
    #     user = "root",
    #     password = "145353",
    #     database = "metalanddb"
    # )

    mycursor = mydb.cursor()
    sql = ""

    if table == "areas_table":
        sql = "INSERT INTO {} (Areaid,  AreaTypeid, Ownerid,  Value,  Rented,  Renterid) VALUES (%s,%s,%s,%s,%s,%s)".format(table)

    elif table == "markets_table":
        sql = "INSERT INTO {} (Marketid, Capacity, WorkerNumber, Grade, Rent, FixIncome, FoodFee, MarketWage, Areaid) VALUES\
            (%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(table)

    elif table == "shoppingcenters_table":
        sql = "INSERT INTO {} (ShoppingCenterid, Capacity, WorkerNumber, Grade, Rent,\
                FixIncome, GoodFee, ShoppingWage, Areaid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)".format(table)

    elif table == "realestates_tables":
        sql = "INSERT INTO {} (RealEstateid, Capacity, WorkerNumber, Grade, Rent, FixIncome, RentCommission, \
            SoldCommission, RealEstateWage, Areaid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)".format(table)
        
    elif table == "players_table":
            sql = "INSERT INTO {} (Playerid, Roleid, Name, Surname, Username, \
                  Password, Workplaceid, Money, Eatings, Goods) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ".format(table)


    mycursor.execute(sql, values)
    mydb.commit()

def GetInfoFromDataBase(table):
    root = tkinter.Tk()
    root.title(f"{table} Detay")
    root.config(bg="white")

    mydb = mysql.connector.connect( host = "localhost", user = "root", password = "145353", database = "metalanddb")
    mycursor = mydb.cursor()

    sql1 = f"SHOW COLUMNS FROM {table}"
    mycursor.execute(sql1)
    Columns = [x[0]+"_columns" for x in mycursor]

    root.geometry(f"{len(Columns)*100}x230")
    my_table = ttk.Treeview(root, columns=Columns, show='headings')
    my_table.grid(row=0, column=0, sticky='nsew')

    for i in Columns:
        my_table.column(i, width=100)

    for i in Columns:
        my_table.heading(i, text=i.split("_")[0])

    sql1 = f"SELECT * FROM {table}"
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()

    for val in myresult:
        my_table.insert('', tkinter.END, values = val)

    scrollbar = ttk.Scrollbar(root, orient=tkinter.VERTICAL, command=my_table.yview)
    my_table.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    root.mainloop()

def UpdateDataBase(SqlQuery):

    # mydb = mysql.connector.connect( host = "localhost", user = "root", password = "145353", database = "metalanddb")
    mycursor = mydb.cursor()
    mycursor.execute(SqlQuery)
    mydb.commit()

def DeleteInfoFromDataBase(SqlQuery):

    # mydb = mysql.connector.connect( host = "localhost", user = "root", password = "145353", database = "metalanddb")
    mycursor = mydb.cursor()
    mycursor.execute(SqlQuery)
    mydb.commit()


