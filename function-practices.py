# function practice
def last_char(name):         # function for char
    return name[-1]
print(last_char("tanmay"))    


def odd_even(n1):              #1 method function for int to check the odd and even
    if n1%2==0:
        return "even"
    else:
        return"odd"
print(odd_even(9))            


def odd_even2(n2):              #2 method function for int to check the odd and even
    if n2%2==0:
        return "even"
    return"odd"
print(odd_even2(9))            


def odd_even3(n3):              #3 method function for int to check the odd and even return only true and flase
    return n3%2==0
print(odd_even3(9))            


def song():                   # blank function
    return"happy birthday song"
print(song())    