age = int(input("enter your age: "))

match age:
    case _ if age<18:
        print ("you are kid:" )
    case _ if age<50:
        print ("you are young now" )
    case _ if age<70:
        print ("you are old")
    case _:
        print ("you are too old")

