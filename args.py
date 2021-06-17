# make flexible function
# * operator

# * args

def total(a,b):
    return a+b
print(total(2,3))    
# print(total(2,3,6,4))    # this print the error because of more arrgument given  
print("------------------------------------")



def tt(c,d):
    return c+d

def all_total(*args):    # * represent the all arrugments present in string args is nothing act like a keyword
    print(args)
    print(type(args))    # type is tuple 

    tt=0
    for num in args:
        tt+=num
    return tt    
print(all_total(5,3,2,3,44,1) )   





print("------------------------------------------------------------------------------------")

# args with normal parameter


def mulpy(*argss):
    multiply = 1
    for j in argss:
        multiply*=j
    return multiply
print(mulpy(1,2,3))        



print("------------------------------------------------")
def mm(n,*argsss):
    print(n)              # here first elment is consider as n type arrugment
    print(argsss)        # rest are the * arrugment
    return mm
print(mm(1,5,5,4,5))      




print("---------------------------------------------")
# args as argument

def mi(*arg):
    m=1
    print(arg)
    for k in arg:
        m*=k
    return m

nuu = [1,2,3,4]             # for list
print(mi(*nuu))             # start * is use to open the list element
mm=(1,3,4,5)               # for tuple
print(mi(*mm))