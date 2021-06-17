def fibo(n):
    a=0                # fisrt variable of series
    b=1                 # second variable of series
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a,b ,end =" ")
        for i in range(n-2):
            c=a+b                       # use to change the 2 variable (update value of  2 variable)
            a=b                         # store the value of 2 variable 
            b=c                         # use to store the update value of 2 variable
            print(b, end=" ")
num=int(input("enter a number to make fibonacci series :->"))
print(fibo(num))
