"""
inheritance :                       Inheritance is the capability of one class to derive
                                    or inherit the properties from another class.


The benefits of inheritance are:   1)  It represents real-world relationships well.
                                       It provides reusability of a code. We don’t have to write the same code again and again.
                                   2)  Also, it allows us to add more features to a class without modifying it.
                                   3)  It is transitive in nature, which means that if class B inherits from another class A,
                                       then all the subclasses of B would automatically inherit from class A.


types:

1. Single inheritance:             When a child class inherits from only one parent class,
                                   it is called single inheritance.

2.Multiple inheritance:            When a child class inherits from multiple parent classes,
                                   it is called multiple inheritance.
                                   Unlike Java and like C++, Python supports multiple inheritance.
                                   We specify all parent classes as a comma-separated list in the bracket.

3. Multilevel inheritance:         When we have a child and grandchild relationship.

4. Hierarchical inheritance:       More than one derived classes are created from a single base.
                                   more than one child classes have the same parent class
                                   then this type of inheritance is known as hierarchical inheritance.

5. Hybrid inheritance:            This form combines more than one form of inheritance. Basically,
                                  it is a blend of more than one type of inheritance.


Private members of parent class
                                 We don’t always want the instance variables of the parent class to be inherited by the child class
                                 i.e. we can make some of the instance variables of the parent class private, which won’t be available to the child class.
                                 We can make an instance variable by adding double underscores before its name. For example,
"""


# 1. Single inheritance:
'''
class animal:
    def print1(self):
     print("i am the class animal")
     
class dog(animal):
    def print2(self):
     print("i am the class dog")
     
obj_dog=dog()
obj_dog.print1()
obj_dog.print2()
'''

# 2.Multiple inheritance:
'''
class animal:
    def print1(self):
     print("i am the class animal")
     
class dog:
    def print2(self):
     print("i am the class dog")
     
class cat(animal,dog):
    def print3(self):
        print("i am in cat class")
        
obj=cat()
obj.print1()
obj.print2()
obj.print3()
'''
# 3. Multilevel inheritance:
'''
class first:
    def f(self):
        print("first")
        
class second(first):
    def s(self):
        print("second")
        
class third(second):
    def t(self):
        print("third")
        
class fourth(third):
    def fo(self):
        print("fourth")
        
obj=fourth()
obj.f()
obj.s()
obj.t()
obj.fo()
'''
# 4. Hierarchical inheritance:
'''
class a:
    def __init__(self):
        print("this is the hirarchial inheritance")
        
class b(a):
    pass      #  we can pass " pass " keyword in the class when we want to keep the class blank
              #otherwies it will throws an error to us

class c(a):
    pass

obj=b()
obj=c()
'''

# 5. Hybrid inheritance: combination of the multiple types of the inheritance
"""
class GrandPa:
    def __init__(self):
        print("Grand Pa")

class Father(GrandPa):
    def __init__(self):
        super().__init__()
        print("Father")

class Mother(GrandPa):
    def __init__(self):
        super().__init__()
        print("Mother")


class child(Father, Mother):
    def __init__(self):
        super().__init__()
        print("Child")

obj= child()
"""

