# we use enumerate function with for loop to track position of our
# item in iterable

# how we can do this without enuerate function

name=["abc","asdf","aserf"]
pos2=0
for names in name:
    print(f"{pos2}--->{names}")
    pos2 +=1 
print("-----------------------------")
# with enumerate function       

for pos1, names in enumerate(name):        # enumerate function take pos as 0 and can do incerment also
    print(f"{pos1}-------{names}")



print("----------------------------------------")

def find_pos(l,target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1   
listt=["abc","tanmay","shiv","bhama"]
print(find_pos(listt,'tanmay'))