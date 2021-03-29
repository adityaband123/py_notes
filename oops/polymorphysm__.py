"""
Polymorphism : The word polymorphism means having many forms.
               In programming, polymorphism means same function name
              (but different signatures) being uses for different types.
"""
# inbuilt polymorphic fuction such as : length
# length can be used for differnt types as string as well as array
'''
print(len("tyrant"))
print(len([1,2,3,4]))
'''
# simple example of polymorphysm:
#by passing the add can be use as per passing of arguments
'''
def add(x,y,z=0):
    return  x+y+z
print(add(1,3))
print(add(1,2,3))
'''
#****************************#

# we can use same method name in two differnt class
#by creating their seperate objects
'''
class programmer:

    def coding(self):
        print("_____i am coder")

    def hacking(self):
        print("________i am hacker")

    def full_stack_developer(self):
        print("_________i am full stack devloper")

class hacker():

    def coding(self):
        print("i am coder")

    def hacking(self):
        print("i am hacker")
obj=hacker()

obj.coding()
obj.hacking()
obj_=programmer()
obj_.coding()
obj_.hacking()
obj_.full_stack_developer()
'''

# polymorphysm with inhritance
#  METHOD OVERLOADING:   If a class has multiple methods having same name
#  but different in parameters, it is known as Method Overloading.
"""
Like other languages (for example, method overloading in C++) do,
python does not support method overloading by default.
But there are different ways to achieve method overloading in Python.
"""
"""
class student:
    def add(self,m1,m2):
        return m1+m2
    # def add(self,m1,m2,m3):
    #     return m1+m2+m3
    # as above we cant create the method with same name in the same class
    #even after passing different arguments
obj=student()
print(obj.add(1,2))
# print(obj.add(1,2,3))

"""
#but we can achive method overloading as follow
'''
class student:

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
         s=a+b+c
        elif a!=None and b!=None:
         s=a+b
        else:
            s=a
        return  s

obj=student()
print(obj.sum(1))
'''
# METHOD OVERRIDING:Method overriding, in object-oriented programming, is a language feature
# that allows a subclass or child class to provide a specific implementation of a method
# that is already provided by one of its superclasses or parent classes.

'''
class a:
    def method1(self):
        print("this is the first method")
class b(a):
     def method1(self):
         print("_____________")
     def method2(self):
        print("this is the second method")

obj=b()
obj.method1()
obj.method2()
'''
# in the above example  when we called to the object  for method1
#    then it will first search in the class b ,if found it will override it and print
#    the data ,whats is in the method for the class b
#    ..but if their is not any of the method called as the method1 then it will go to
#    the method1 of the class a and prints the data inside this method

