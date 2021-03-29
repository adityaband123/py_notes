"""
types:          default constructor
                parameterized constructor

syntax:         def __init__(self):
                  # body of the constructor

__init__(self): in python we can say that __init__ is as
                like the constructor in C++ and Java

                generally the use of the constructors is
                to initialize or to assign value to the data
                members of the class
                when the object of the class is created

                the constructor automatically get called as the object of the class is created
                no need to called explicitly

                python does not support explicit multiple constuctor
                i.e we can create only one constuctor ( __init__(self)__ ) in one class
"""
class employees:

    # #default_constuctors
    # def __int__(self):
    #     print("this is the default constructor")

    #parameterized constuctor
    def __init__(self,name,id):
        self.name=name
        self.id=id
    #simple method
    def print_details(self):
        print("Name: {}\nId: {}".format(self.name,self.id))

obj=employees("tyrant",99)
obj.print_details()

