# Reading an excel file using Python
from database import sender
import xlrd

# Give the location of the file
loc = ("/home/abhishek/Downloads/OSTL.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(2)

# For row 0 and column 0
#sheet.cell_value(2, 1)
'''for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))'''

'''for i in range(3,sheet.nrows):
    print(sheet.cell_value(i, 1))'''



import pymysql
myconn = pymysql.connect(host='localhost',user='root',password='password',db='attendance')
print("connection done")

def drop():
    sql="drop table student"
    try:
        cur=myconn.cursor()
        cur.execute(sql)
        print("table troppped")
    finally:
            pass#      myconn.close()

'''list=['salman','aniket','abhishek','rutuja']
total=[0,0,50,10]
l=len(list)'''
def create():
    try:
        cursor=myconn.cursor()
        sql="create table student(rname varchar(40))"
        cursor.execute(sql)
        print("table created")
    finally:
        cursor.close()
def insert1() :
    try :
        cursor = myconn.cursor()
        print("rows= ",sheet.nrows)
        for j in range(3, sheet.nrows):
            #cursor = myconn.cursor()
            sql="insert into student values('%s')"
            #for j in range(3, sheet.nrows):
            args=(sheet.cell_value(j, 1))
            cursor.execute(sql % args)
            myconn.commit()
            print(j+1," inserted")
    finally:
        cursor.close()
        myconn.close()
#drop()
create()
insert1()