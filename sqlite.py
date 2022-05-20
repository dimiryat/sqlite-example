# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:39:08 2022

@author: DennisLin
"""

import sqlite3
import csv

cmd_create = 'CREATE TABLE record (id INTEGER PRIMARY KEY AUTOINCREMENT, class_name TEXT, price INTEGER, recommendation TEXT)'
cmd_insert = 'INSERT INTO record (class_name, price, recommendation) VALUES ("dummy class", 1000, "student")'
cmd_select = 'SELECT * FROM record WHERE recommendation="有程式基礎的初學者"'

def execute_db(fname, sql_cmd):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute(sql_cmd)
    conn.commit()
    conn.close()
    
def write_data_in(fname, db_name):
    with open(fname, 'r', encoding='utf-8') as f:
       reader = csv.DictReader(f)
       for row in reader:
           cmd = 'INSERT INTO record (class_name, price, recommendation) VALUES ("%s",%d,"%s")' % (row['Class'], int(row['Price']), row['Recommendation'])
           execute_db(db_name, cmd)

def select_db(fname, sql_cmd):
    conn = sqlite3.connect(fname)
    c = conn.cursor()
    c.execute(sql_cmd)
    rows = c.fetchall()
    conn.close()
    return rows

if __name__=='__main__':
    print()
    print("Main program...")
    print()
    
    db_name = 'db.sqlite' 
    #write_data_in('class_price.csv', db_name)
    for row in select_db(db_name, cmd_select):
        print(row)