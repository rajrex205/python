def average(*numbers):
    sum= 0 
    for i in numbers:
        sum = sum + i
    print("average of sum: ", sum / len(numbers))



average(5, 6)