
"""
class                   : A Class is like an object constructor, or a "blueprint" for creating objects.
                        class is an extensible program-code-template for creating objects, providing initial values
                        for state (member variables) and implementations of behavior (member functions or methods)

object                  :For example: in real life, a car is an object.
                        The car has attributes, such as weight and color and methods, such as drive and brake.


use of the self keyword:
                       when we create the object of the class the object itself get pass to the self ,with
                       the help of the self keyword we can differentiate what operation is to do to which
                       object

                       The Object is passed into the self parameter so that the object can keep hold of its own data.

"""
class demo:  #decleration of the class
    msg="this is the message"
    def printmsg(self):      # def printmsg(d1):    self=d1
                             # def printmsg(d2):    self=d2

     print(self.msg)

    def __init__(self):
        print("we are in the init method")
d1=demo()   #decleration of the object
d2=demo()
d1.printmsg()
d2.printmsg()