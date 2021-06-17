# function inside function 
def greater(a,b):               # first function which compare the 2 variable 
    if a>b:
        return a
    return b    
def greatest(a,b,c):             #  second function which  compare thr 1 function and the 3 variable         
    bigger = greater(a,b)
    return greater(bigger,c)
print(greatest(1,2,3))    



# 2 method  to declare the greatest function  its only combine the 7-8 line by removing bigger
# #def greatest(a,b,c):
#   return greater(greater(a,b),c)
# print(greatest(1,2,3)) 