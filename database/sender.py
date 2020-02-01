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

list=['salman','aniket','abhishek','rutuja']
total=[0,0,50,10]
l=len(list)
def create():
    try:
        cursor=myconn.cursor()
        sql="create table student(roll_no int primary key,name varchar(20),total int )"
        cursor.execute(sql)
        print("table created")
    finally:
        cursor.close()
def insert1() :
    try :
        cursor = myconn.cursor()
        for i in range(l):
            #cursor = myconn.cursor()
            sql="insert into student values('%d','%s','%d')"
            args=(i+1,list[i],total[i])
            cursor.execute(sql % args)
            myconn.commit()
            print(i+1," inserted")
    finally:
        cursor.close()
        myconn.close()
drop()
create()
insert1()