# filter function can use only 1 iteration that is can use only 1 loop 
# but when we canvert into list or a tuple the we can iterated as we want  

def is_even(a):
    return a%2==0

num=[1,4,6,7,8,9,3,3,5]
event=list(filter(is_even,num))
for i in event:     # first print
    print (i)
print(event)         # second print



print("********************************************")


# list comperhertion

new=[i for i in num if i%2==0]
print(new)              # third print