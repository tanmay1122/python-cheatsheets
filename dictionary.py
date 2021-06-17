# it is a unordered collection of data in key value pair
# it use because list have some limitation ,that is list dont represent real data
# for example:- user=["tanmay",21,[1,2,3],["w","e","r"],[1,2,34,4]]  this list contain user name,age,no.,word,no.
#you can do this but it is not a good way to repreesent

#dictionary

# method -1

user={"name":"tanmay","age":21}    #name and age are key and tanmay and 21 are the value
print(user)
print(type(user))

# method -2

user1=dict(name="tanmay",age=21)
print(user1)


# access data from dictionary 
# note:-> no indexing can be giving to access a data

user2=dict(name="tanmay",age=21)
print(user2["name"])
print(user2["age"])

# list inside dictoinar

user_info={"name":"tanmay","age":21,"num":[1,2,3],"word":["w","e","r"],"num_list":[1,2,34,4]}
print(user_info)

# dictionary inside dictionary

client={"users1":{"name":"tanmay","age":21},"name1":"shyam","age":21 }
print(client)
print(client["users1"]["age"])
print(client["users1"]["name"])

# add data in empty dictionary

user_112={}
user_112["name"]="tanmay"
user_112["age"]="21"

print(user_112)


