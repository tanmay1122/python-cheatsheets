# string are immutable

string = "string"
print(string[1])      # normal and its works in all lang. 

#string[1]  = "T"      # mutable and its can not works in all lang. python is immutable so it can not use this so we use replace method

print(string.replace("t","T"))    # in this replace method is use and output can be generated by create new veriable of string. 

# for example

new_string = string.replace("s","T")

print(new_string)

