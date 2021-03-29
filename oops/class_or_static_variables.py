"""
class or the static variables are the variables whose single copy is available
to all the instance of the class.

if we modify the copy of class variable in an instance, it will effect all the
copies in the other instance or other class objects

class or the instance variables are always get write outside the class
methods of consturctors

to access class variable we need class methods with the "cls" as first parameter
then we can access class variables using cls.variable_name

if we want to access the class variable outside the class
then we can do it as "class_name.variable_name

class variables are the variables whoes single copy is available to all
instance of the class.
if we modefy the copy of class variable in an instance it will
efect all the copies in the other

"""
'''
class Mobile:
    fp="yes" #class variable

    @classmethod
    def id_fp(cls): #class method
        print(cls.fp)

realme=Mobile()
print(Mobile.fp)  # accessing the class variable outside the class
Mobile.id_fp()    # call the class method we need to use the class method name with class name


'''

#a bit modified code
class Mobile:
    #class variable or static variable
    class_var='class_variable'

    #constuctor
    def __init__(self):
        #instance  variable
        self.model="realme 6i"

    #instance method
    def show_model(self):
        #accessing instance variable
        print("Model:",self.model)

    #class method
    @classmethod
    def class_method(cls):
        #accessing class variable
        print("which variable is this: ",cls.class_var)

realme=Mobile()
realme.show_model()
Mobile.class_var="changed_class_var"     # in this way we can change the class variable outside the
                                        # class by using class name and class_variable name
Mobile.class_method()