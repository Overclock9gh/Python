#!/usr/bin/python3.6
# --coding:Utf- -

import pymysql
import pandas as pd
import sys
import site
site.addsitedir('/home/hsaid/Bureau/scripts/python/jeu_video')
from dbHelpers import *

def mysql_to_csv(sql, file_path, con):
    '''
    The function creates a csv file from the result of SQL
    in MySQL database.
    '''
    try:
        df = pd.read_sql(sql, con)
        df.to_csv(file_path, encoding='utf-8', header = True,\
        doublequote = True, sep=',', index=False)
        print('File, {}, has been created successfully'.format(file_path))
        con.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)



def csv_to_mysql(load_sql, con):
    '''
    This function load a csv file to MySQL table according to
    the load_sql statement.
    '''
    try:
        cursor = con.cursor()
        cursor.execute(load_sql)
        print('successfully loaded the table from csv.')
        con.close()

    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)


def csv_integrity(InFileName, OutFileName):
    NumCommas = 0
    numberOfLines = 0
    print("Checking file")
    try:
        File = open(InFileName,'r')
        for line in File:
            if line.count(',') > NumCommas:
                NumCommas = line.count(',')
        #return to the start of the file
        File.seek(0)
        OutFile = open(OutFileName, 'w')
        for line in File:
            OutFile.write(line.rstrip() + ',' * (NumCommas - line.count(',')) + '\n')
            numberOfLines += 1
        OutFile.close()
        File.close()
    except Exception as e:
        print('Error: {}'.format(str(e)))
        sys.exit(1)
    print(numberOfLines, "lines processed",)