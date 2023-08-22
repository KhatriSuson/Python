# class Parrot:
#     def fly(self):
#         print("Parrot ca fly")

#     def swim(self):
#         print("Parrot can't swin")
# class Penguin:
#     def fly(self):
#         print("Penguin can't fly")

#     def swim(self):
#         print("Penguin can swim")
# # Common interface
# def flying_test(bird):
#     bird.fly()

# def swim_test(bird):
#     bird.swim()

# # Instantiate Objects
# blu = Parrot()
# peggy = Penguin()

# #Passing the object

# flying_test(blu)
# flying_test(peggy)
# swim_test(blu)
# swim_test(peggy)


class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot can't swim")


class Cow:
    def fly(self):
        print("cow can't fly")
    def swim(self):
        print("cow can't swim")

def test_fly(bird):
    bird.fly()
def test_swim(animal):
    animal.swim()

parr = Parrot()
cw = Cow()

test_fly(parr)
test_fly(cw)

test_swim(parr)
test_swim(cw)