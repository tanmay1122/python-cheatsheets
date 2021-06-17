name=input("enter your name:->")     # normally take input name 
def add(n,m):                        #  make a functions
   return n+m
def sub(n,m):
    return n-m
def multiply(n,m):
    return n*m
def divide(n,m):
   return n/m
print("welecome to my calculator")
while True:                              # put condition is true
    menu=input("a:add , s:subtraction , m:multiply , d:divide ::--->>>  ")    # choose operation
    if menu in('a','s','m','d'):                    #if-else statement
        n1=float(input("enter a first number:->"))      # take 2 number as input
        n2=float(input("enter a second number:->"))

        if menu=='a':                           # doing the operation with the help of functions
            print(n1,'+',n2,'=',add(n1,n2))
            break                       # use to stop the operation after completion
        if menu=='s':
            print(n1,'-',n2,'=',sub(n1,n2))
            break
        if menu=='m':
            print(n1,'*',n2,'=',multiply(n1,n2))
            break
        if menu=='d':      
            print(n1,'/',n2,'=',divide(n1,n2))      
            break
    else:
        print("any error is present")   
        continue
print("thankyou",name)            # use just for good look


