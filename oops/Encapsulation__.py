"""
Encapsulation:       Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
                     It describes the idea of wrapping data and the methods
                     that work on data within one unit.
                     This puts restrictions on accessing variables and methods directly
                     and can prevent the accidental modification of data.
                     To prevent accidental change,
                     an object’s variable can only be changed by an object’s method.
                     Those types of variables are known as private variable.
                     A class is an example of encapsulation as it encapsulates
                     all the data that is member functions, variables, etc.


 Protected members :  (in C++ and JAVA) are those members of the class that cannot
                      be accessed outside the class but can be accessed from within the class and
                      its subclasses. To accomplish this in Python,
                      just follow the convention by prefixing
                      the name of the member by a single underscore “_”.

private:              __    use of double underscore
portected:            -     use of single underscore

"""
# in the following program the third party can
# easily chang the value of the price
'''class payment:
      def __init__(self,price):
          self.price=price
books=payment(19)
books.price=4
print(books.price)
'''

# in the following program we have used the oops concept
# i.e encapsulation so no one can chang the value of the price
'''
class payment:

    def __init__(self,price):
        self.__final_price=price+price*0.05
        #if we use single underscore then it will gives only defination
        #as a warning but stil the third party can change the value of the variables

    def get_final_price(self):
        return self.__final_price

books=payment(10)
#books.final_price=4  ->> in this case anyone  can change the value of the variable
books.__final_price=4 #   in this case no one can change the value of the variable
print(books.get_final_price())
'''
class payment:

    def __init__(self,price):
        self.__final_price=price+price*0.05

    def get_final_price(self):
        return self.__final_price

    def set_final_price(self,discount):
        self.__final_price=self.__final_price-self.__calculate_discount(discount)

    def __calculate_discount(self,discount):
        return self.__final_price*(discount/100)
    
book=payment(10)
book.__calculate_discount(50)
book.set_final_price(10)
print(book.get_final_price())


