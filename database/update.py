def insert1(args) :

    try :
        cursor = myconn.cursor()
        args = tuple(args)
        #cursor = myconn.cursor()
        sql="insert into os values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

        print(args)
        cursor.execute(sql % args)
        myconn.commit()
        print(i+1," inserted")
    finally:
         print("Jai Mata di")