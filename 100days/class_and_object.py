# class Person:
#     name = "suson"
#     occupation = "Web Designer"
#     networth = 12

#     def info(self):
#         print(f'{self.name} is a {self.occupation}')


# a = Person()
# b = Person()
# b.name = "gita"
# b.occupation = "accountant"
# a.name = "Rajesh"
# a.occupation = "Software Develper"
# # print(a.name,a.occupation)
# a.info()
# b.info()

class Person:
    def __init__(self,n,o):
        print("hey I am a person")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("suson ", "Developer")
b = Person("Divya", "Accountant")
# a.name = "Divya"
# a.occ = "HR"

# a.info()
a.info()
b.info()