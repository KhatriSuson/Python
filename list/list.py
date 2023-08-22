# l = ['apple','ball','cat','dog','apple','ball','cat','dog']
# c = l.count(l)
# for i in range(c):
#     l.remove = "ball"
# print(l)


# Creating a List

# fruits = ["apple","banana","cherry","date"]

# # Accessing Elements

# print(fruits[0])
# print(fruits[2])


# # Appending Elements

# fruits.append("grape")

# print("After Appending Fruits list Output",fruits)


# # Removing Elements 

# fruits.remove("cherry")
# print("After Removing cherry from the fruits list ", fruits)


# # Length of the list 

# print(len(fruits))

# # Iterating Over Elements
# for fruit in fruits:
#     print(fruit)

# # checking if a elements exitsts in the list 

# if 'banana' in fruits:
#     print("Apple is in the list ")
# else:
#     print("Apple is no appear in the list")


# # Reversing the list 

# fruits.reverse()
# print(fruits)
# s = fruits.sort()
# print(s)


# a = ['apple','banana','cat','dog']

# # Slicing a list 
# sliced_a = a[1:3]
# print(sliced_a)


# # Copying a List to next list
# copy_a = a.copy()
# copy_a.append("Coppy apped hehe ..")
# print("Print after copy",copy_a)


# # Extending a List 
# a.extend(["grape",'kiwi'])
# print("print after list extend",a)



# # Counting occurrences of an element

# count = a.count("banana")


# # Finding or Searching the element of the list
# index = a.index("dog")
# print("Print the index of dog",index)



# # Removing an element by index

# removed_a = a.pop(2)
# print("list print after pop() index 2",removed_a)




# # Clearing a list 

# a.clear()
# print(a)


# l = ["apple","banana","cherry","dog"]
# pop_l = l.pop(3)

# print(pop_l)
# print(l)

# l = ["apple","banana","cherry","dog"]
# copyList = l.copy()
# print(copyList)

l = ["apple","banana","cherry","dog"]
l.extend(["apple","BANANA","CHERRY"])
l.extend([1,2,3,4,5,6])
print(l)

