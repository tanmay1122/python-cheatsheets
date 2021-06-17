#i=0
#for i in range(10):
  #  print(f"hello:{i}")




#for loop sum

#total=0
#for i in range(1,11):
   # total+=i
    #print(total)










#n=int(input("enter a number"))
#total=0
#for i in range(1,n+1):
 #   total+=i
  #  print(total)




# sum of number 
     
#total=0
#n=input("entre a number :")
#for i in range(0,len(n)):
 #   total+=int(n[i])
  #  print(total)     



# count name by for loop


name=input("enter a name:-")
tem=""
for i in range(0,len(name)):
    if name[i] not in tem:
        print(f"{name[i]}:{name.count(name[i])}")
        tem+=name[i]