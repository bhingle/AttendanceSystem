from database import *
from database.recevier import *
from database.sender import insert1, create


def add_new():

    print(list1)
    print("enter name and roll no")
    name=input()
    roll_no=int(input())
    list1.insert(roll_no-1,name)
    print(list1)

#add_new()
#create()
#insert1()
