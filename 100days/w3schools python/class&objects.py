# class Myclass:
#     x = 5
# obj = Myclass()
# print(obj.x)



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("Honny", 34)
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}  {self.age}"

# p1 = Person('JOhn', 34)
# print(p1)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
       
# obj = Person(" return f"{self.name}  {self.age}"
# john ",  43)
# print(obj)


# class Cal:
#     def __init__(self,a, b):
#         self.a = a

#         self.b = b

#     def __sum__(self):
#         sum = self.a + self.b
#         return sum
    

# obj = Cal(12,33)
# print(obj)




# Calculator using class and object in python

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
    def sub(self, num):
        self.result -= num
    def mul(self, num):
        self.result *= num
    def div(self, num):
        if num != 0:
            self.result /= num
        else:
            print("Error : Cannot divide by zero")

    def clear(self):
        self.result = 0

    def display_result(self):
        print("Result:", self.result)


# Create an instence of the Calculator class

calc = Calculator()
calc.add(5)
calc.sub(3)
calc.mul(8)
calc.div(10)
calc.display_result()
calc.clear()
calc.display_result()
