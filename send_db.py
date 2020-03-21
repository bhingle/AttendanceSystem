import pymysql
myconn = pymysql.connect(host='localhost',user='root',password='password',db='attendance')
print("connection done")



def create():
    try:
        cursor=myconn.cursor()
        sql="create table student(name varchar(20) )"
        cursor.execute(sql)
        print("table created")
    finally:
        cursor.close()



def insert1() :
    try :
        cursor = myconn.cursor()
        s=len(data)
        for i in range(s):
            for k in range(34)
                #cursor = myconn.cursor()
                sql="insert into student values('%s')"
                args=(data[i][k])
                cursor.execute(sql % args)
                myconn.commit()
                print(i+1," inserted")
    finally:
        cursor.close()
        myconn.close()
create()
insert1()