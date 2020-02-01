''' import pyodbc
con = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};server=localhost;database=record;uid=root;pwd=Bhingle@123")
cur = con.excute()
cur.execute("SELECT * FROM student WHERE quantity < 3")
for row in cur:
    print(row.roll_no + row.name + row.total)
cur.close()
con.close()'''
'''
import pyodbc
server = 'localhost'
database = 'record'
username = 'root'
password = 'Bhingle@123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.close()
cnxn.close()
'''

""""
import pymysql
myconn = pymysql.connect(host='localhost',user='root',password='password',db='attendance')
print("connection done")
sql="Select name from student "
list=[]
try:
    cur=myconn.cursor()
    for i in range(cur.rowcount):
        cur.execute(sql,( i ) )
        for b in cur:
            name=b[0];
            print(name)
            list.append(name);
        print(list)
finally:
    myconn.close()
"""

import pymysql
myconn = pymysql.connect(host='localhost',user='root',password='password',db='attendance')
print("connection done")
sql="Select name from student "
list1=[]
try:
    cur=myconn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    for b in rows:
        for t in b:
                list1.append(t)
    print(list1)
finally:
    myconn.close()


#code for updatetion

