# list comprehension
# with list comprehension we can create a list in one line 

print("----------------------------------")
print("list comprehension")
squares=[]              # normal method
for i in range(1,11):
    squares.append(i**2)
print(squares)    

square=[j**2 for j in range(1,11)]     # list comprehension
print(square)

square1=[-h for h in range(1,11)]  # for print negitive number
print(square1)


k=["harshit","tanmay","yash"]   # for print 1 position string 
square2=[k[0] for k in k]
print(square2)

# list comperhension with if statement
print("----------------------------------------")
print("list comperhension with if statement")
num=list(range(1,11))     # normal method
even_num=[]
for i1 in num:
    if i1%2==0:
        even_num.append(i1)
print(even_num)


n1=[i4 for i4 in range(1,11) if i4%2==0]   # list comperhension with if statement
print(n1)           # print even number

nn=[g for g in range(1,11) if g%2!=0]
print(nn)                   # print odd number
print("\n")


# list comprehension with if - else statement
print("list comprehension with if - else statement")
print("_________________________________")


number2=[1,2,3,4,5,6,7,8,9]         # normal method
new_number1=[]
for i5 in number2:
    if i5%2==0:
        new_number1.append(i5**2)
    else:
         new_number1.append(-i5)   
print(new_number1)


print("_________________________________")              # lit comprehension with if - else statement
num3=[i6**2 if (i6%2==0) else -i6 for i6 in number2  ]
print(num3)



# list comperhension with nested 
print("list comperhension with nested list")
nnn=[]              # normal methed
for j2 in range(3):
    nnn.append([1,2,3])
print(nnn)        


print("_________________________________")             
nested_list=[[i7 for i7 in range(1,4)]for j2 in range(3)]           # list comperhension with nested list
print(nested_list)


print("_________________________________")             

# dictionary comperhension 
print("_________________________________")             
print("dictionary comperhension ")

nn1={f"square of {n2} is":n2**2 for n2 in range(1,11)}
for k,v in nn1.items():
    print(f"{k}:{v}")
print("_________________________________")             

srt="tanmay"
wordss={char:srt.count(char) for char in srt}
print(wordss)

hh={ss:"tanmay".count(ss) for ss in "tanmay"}
print(hh)
print("_________________________________")             



# dictionary comprehension with if-else
print("dictionary comprehension with if-else")

odd_even={ii:("even" if ii%2==0 else "odd")for ii in range(1,11)}
print(odd_even)
print("_________________________________")             

printtt={iw:(iw**2 if iw%2==0 else -iw)for iw in range(1,11)}
for k1,v1 in printtt.items():
    print(f"{k1}:->>{v1}")



print("_________________________________")             
# set comprehension
print("set comprehension")

sett={k11**2 for k11 in range(1,11)}
print(sett)
print("_________________________________")             


name111=["tanmay","shyam","shiv","khwaja"]
set1={naa[0] for naa in name111}
print(set1)

print("_________________________________")             

mna={iq**2 if iq%2==0 else -iq  for iq in range(1,11) }
print(mna)
print("_________________________________")             
