import pandas as pd 
import csv 
import datetime as dt 
import time 
import mysql.connector
import mysql_connection as connect
import pandas_market_calendars as mcal 
import matplotlib.pyplot as plt

mydb, mycursor = connect.open_connection()

#1 day of 1 month pull ticker data 
start = '2016-01-01'
end = '2021-03-22'

#sort the data based on what the research you want
######Data pull is limited to first 1000 company symbols over two trading days
    #DATAFRAME
#ticker     #% change 
query_bnd = "SELECT company_id, date, close FROM pricing_data WHERE company_id in(21090) AND date BETWEEN '{}' AND '{}';".format(start, end)
query_spy = "SELECT company_id, date, close FROM pricing_data WHERE company_id in(23182) AND date BETWEEN '{}' AND '{}';".format(start, end)
df_bnd = pd.read_sql(query_bnd, con = mydb)
df_spy = pd.read_sql(query_spy, con = mydb)

print(df_bnd, df_spy)
plt.plot(df_bnd['date'], df_bnd['close'])
plt.plot(df_spy['date'], df_spy['close'])
plt.show()

print('now some changes have been made from my Air')



#define a date and the top 30 tickers of sorted data and write to csv