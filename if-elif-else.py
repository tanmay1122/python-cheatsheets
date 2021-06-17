# if  elif else statement

name=input("enter your name:- ")
age=int(input("enter your age:- "))
if age<=0:
    print("you cant watch movie")
elif age>=1 and age<=3:
    print("your ticket is free")
elif age>=4 and age<=10:
    print("ticket is 150 rupess")
elif age>=11 and age<=60:
     print("ticket is 250 rupess")
else:
    print("ticket is 200 rupess")