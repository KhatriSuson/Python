# class Point:
#     def __init__(self,x=0, y = 0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         # return "({0},{1})".format(self.x,self.y)
        
#         return f"{self.x} {self.y}"
#     def __add__(self,other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)


# p1 = Point(2,3)
# p2 = Point(-1,2)
# print(p1 + p2)




#OPERATOR OVERLOADING
# class Point:
#     def __init__(self, x=0,y=0):
#         self.x = x
#         self.y = y
       
#     def __str__(self):
#         return f"{self.x} {self.y}"

#     def __add__(self,a):
#         x = self.x + a.x
#         y = self.y + a.y
#         return Point(x,y)
    
# p1 = Point(2,3)
# p2 = Point(-1,-3)
# print(p1+p2)

# class Point:
#     def __init__(self,x=0):
#         self.x = x
#         print("This is init method ", self.x)

#     def __str__(self):
#         print()
#         return f"This is str method  {self.x}"

#     def __add__(self,other):
#         x = self.x + other.x
#         print("This is add method")
#         return Point(x)
    
# p1 = Point(10)
# p2 = Point(20)
# p3 = Point(30)

# print(p1+p2+p3, "is total sum of the input value of Point classs p1,p2,p3 object")




# class Point:
#     def __init__(self,x =0):
#         self.x = x

#     def __str__(self):
#         return f"This is str method {self.x}"

#     def __add__(self,other):
#         x = self.x + other.x
#         return Point(x)

# p1 = Point(10)
# p2 = Point(20)
# p3 = Point(30)
# print(p1+p2+p3)
