# add , delete data in dictionary
User={
    "name" : "tanmay",
    "age" : 21,
    "movie" : ["abcd","kick","coco"],
    "song" : ["love","shyam","baba"]
}

# add data

User["movie2"]=["golmal","golimar"]
print(User)

# pop method  :->> delete

xx=User.pop("movie2")
print(f"pop item is {xx}")
print(User)

# pop item method :->> delete the last data in dict
yy=User.popitem()
print(yy)
print(type(yy))
print(User)