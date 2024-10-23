def func1():
    try:
        a = str("rajdeep")
        b = int(14)
        if (a != b):
             print("not equal")
             

    except ValueError:
            print("you got error")
    finally:
         print("i will execute allways")


x= func1()
print(x)
