# default parameter only make at the end of the function
# for example :-> def reet(name,last,age=23)


def reet(FirstName,LastNAme,Age):               # normal parameter passing in function
    print(f"your first name is {FirstName}")
    print(f"your last name is {LastNAme}")
    print(f"your age is {Age}")

reet("tanmay","bansal",21)   


def neet(FirstName1,LastNAme1,Age1=20):       # default parameter passing in function in which 21 is overwrite on 20
    print(f"your first name is {FirstName1}")
    print(f"your last name is {LastNAme1}")
    print(f"your age is {Age1}")

neet("tanmay","bansal",21)   


def reet2(FirstName2,LastNAme2,Age2=None):         # default parameter passing in function in which age can not contain value
    print(f"your first name is {FirstName2}")
    print(f"your last name is {LastNAme2}")
    print(f"your age is {Age2}")

reet2("tanmay","bansal",)   


#def reet3(FirstName3,LastNAme3=None,Age3):               # wronge it through the error we can't use a value containe parameter after none or default parameter
    #print(f"your first name is {FirstName3}")
    #print(f"your last name is {LastNAme3}")
    #print(f"your age is {Age3}")

#reet3("tanmay",21)   


def reet4(FirstName4,LastNAme4=None,Age4=None):       # it is right it can't through the error we use default after default
    print(f"your first name is {FirstName4}")
    print(f"your last name is {LastNAme4}")
    print(f"your age is {Age4}")

reet4("tanmay")   