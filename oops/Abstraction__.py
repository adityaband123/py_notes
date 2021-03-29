"""
Abstraction:  in Python is the process of hiding
              the real implementation of an application
              from the user and emphasizing only on usage of it.

              OR

              In Python, an abstraction is used to hide the irrelevant data/class
              in order to reduce the complexity.
              It also enhances the application efficiency.

              in case python does not support method called ABSTRACTION directly
              but we can achive it with the help of the module called as ABC
              here ABC stands for   ABSTRACT BASE CLASSES



EX:          Another real life example of Abstraction is ATM Machine; All are performing operations on
              the ATM machine like cash withdrawal, money transfer, retrieve mini-statement…etc. but we can't
              know internal details about ATM. Note:
              Data abstraction can be used to provide security for the data from the unauthorized methods.


ABSTRACT CLASS: THE CLASS HAVING AT LEAST ONE ABSTRACT METHOD IS CALLED AS THE ABSTRACT CLASS


ABSTRACT METHOD: THIS IS THE METHOD WHICH DOES NOT HAVE BODY IS CALLED ABSTRACT METHOD



STEPS:        1) from abc import ABC ,abstractmethod
              2)create a method with decorator  as @abstract method
              when a method is abstract then user will not able to create
              the objcet of the abstract method

              3)pass ABC like ...class class_name(ABC):
              4)create another class which will inherite the parent one
              and then define the same process inside the child class  also

"""
'''
from abc import ABC ,abstractmethod
class parent(ABC):

    @abstractmethod
    def abstract_method(self):
       pass
class child(parent):

    def abstract_method(self):
        print("this is the abstract method")
# obj=parent()  we cant create object of an abstract class
#otherwies it will throws an error to us
obj=child()
obj.abstract_method()

'''

