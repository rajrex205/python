import time

timestamp = time.strftime('%H')


if int(timestamp) <= 9:
    print ("Good Morning")
elif int(timestamp) <= 12:
    print ("good noon")
elif int(timestamp) <= 20:
    print ("good evening")
else:
    print ("Good night")