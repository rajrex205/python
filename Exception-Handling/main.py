
a = input("enter your number for table: ")
try:
    for i in range(1,11):
     print(f"{a} X {i} =", int(a)*i)
except ValueError:
    print ("please provide number in int")
    