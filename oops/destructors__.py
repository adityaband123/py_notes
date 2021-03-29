"""
destructors:  Destructors are called when an object gets destroyed.
              In Python, destructors are not needed as much needed in C++ because
              Python has a garbage collector
              that handles memory management automatically.

syntax:      def__del__(self):
               # body of the destuctor

"""
class des:
    # constuctor
    def __init__(self):
        print("constuctor get called")

    # destructor
    def __del__(self):
        print("destuctor get called and the constuctor get distroyed")

obj=des()
