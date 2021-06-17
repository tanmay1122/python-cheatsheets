# fromkeys
# d = { "name" : "unknown" , "age" : "unknown"}

d=dict.fromkeys(["name","age","height"],"unknown")  # with list
print(d)

d1=dict.fromkeys(("name","age","height"),"unknown")  # with tuple
print(d1)

d2=dict.fromkeys(range(1,10),"unknown") # with intgier
print(d2)


# get method (useful)
d = {"name" : "tanmay","age" : "unknown"}
print(d["name"])                # normal method slicining type
print(d.get("name"))            # get method

if "name" in d:       # normal method
    print("preesent")
else:
    print("not present")

if d.get("name"):     # get method
    print('present')
else:
    print("not present")    

user = {"name" : "tanmay" , "age" : 34 , "age" : 21}   # 2 same key in dictionary useing get method
print(user.get("name","not found !"))
print(user.get("fav","not found !"))
print(user)           # the second value of age can over-ride the first value 

# clear method

d.clear()
print(d)

# copy method

d3 = d2.copy()
print(d3)
print(d3 is d1)
