import pandas as pd
import numpy as np
import pandas_profiling as pp
import sqlite3
import os
from sqlalchemy import create_engine

folder = 'D:/Shweta/pccm_db'
file = 'PCCM_BreastCancerDB_2021_02_22.db'

engine = create_engine('sqlite:///D://Shweta//pccm_db//PCCM_BreastCancerDB_2021_02_22.db')

db_path = os.path.join(folder, file)
conn = sqlite3.connect(db_path)
sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
tables = pd.read_sql(sql_stat, conn)
table_names = tables['name']
get_tab = pd.read_sql('SELECT * FROM ' + table_name, conn)


def get_pandas_profile_of_each_table(folder, file):
    db_path = os.path.join(folder, file)
    conn = sqlite3.connect(db_path)
    sql_stat = "SELECT * FROM sqlite_master WHERE TYPE = 'table'"
    tables = pd.read_sql(sql_stat, conn)
    table_names = tables['name']
    table_idx = [0, 4, 5, 15, 18, 19, 20, 23]

    for table_name in table_names[table_idx]:
        print(table_name)
        tab_stat = 'SELECT * FROM ' + table_name
        get_tab = pd.read_sql(tab_stat, conn)
        print(get_tab.head())
        profile = pp.ProfileReport(get_tab, title = 'pandas profile report')
        profile.to_file('D:\\Shweta\\pccm_db\\pp_html_files\\2021_03_30_pandas_profile_report_'+ table_name + '.html')


# get_pandas_profile_of_each_table(folder, file)