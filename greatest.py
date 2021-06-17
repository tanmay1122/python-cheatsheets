
def greater(n1,n2,n3):
    if n1>n2 and n1>n3:
         return n1
    elif n2>n1 and n2>n3:
         return n2    
    else :
        return n3 
a=int(input("enter 1 number :->"))
b=int(input("enter 2 number :->"))           
c=int(input("enter 3 number :->"))  
num=(greater(a,b,c))
print( num)