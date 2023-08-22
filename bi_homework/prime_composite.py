# num = 35

# #define a flag variable

# flag = False
# if num == 1:
#     print(num,"is not a prime number")

# elif num > 1:

#     # Check for factors 

#     for i in range(2, num):
#         if (num % 2) == 0:
#             flag = True
#         break

#     if flag:
#         print(num, "is a composite  number")
#     else:
#         print(num, "is prime number")



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def detect_prime_or_composite():
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is a composite number.")

detect_prime_or_composite()