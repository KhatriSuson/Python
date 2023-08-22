# A function is a block of code that performs a specific task 
# whenever it is called. In bigger programs, where we have large amounts of code, 
# it is advisable to create or use exiting functions that make the program flow organized and neat.



# def claculateGmean(a, b):
#     mean = (a*b)/(a+b)
#     print(mean)

# def isGreater(a, b):
#     if(a>b):
#         print("First number is Greater ")

#     else:
#         print("Second number is Greater")

# def isLesser(a,b):
#     pass
# a = 9
# b = 12
# isGreater(a,b)
# claculateGmean(a,b)


# Funtion with pass arguments 

# def ave(a,b,c=2):
#     print("The average of this number is = ", (a+b+c)/2)

# ave(4,6)

# def average(*numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("The average = ", sum/len(numbers))

# average(1,2,3,4,5,6,7,7)


# def name(**name):
#     print("hello,", name["fname"],
#           name["mname"], name["lname"])

# name(fname = "Ram", lname= "Rai", mname= "Bdr")

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

c = average(3,4,5,6,7,8,9)
print(c)