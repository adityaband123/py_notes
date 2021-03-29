# try:
#     open("this.txt")
# except Exception as e:
#     print(e)
# try:
#     file=open("this.txt",'r')
# except EOFError as e:
#     print("eof exception")
# except IOError as e:
#     print("we can handle this type of the exception")
# finally:
#     print("e to print hona hi hain")
#
try:
    print("i will try this code and will throw an exceptin if their is any of the problem")
except:
    print("i will run if and only if try block fails")
else:
    print("i will execute if their is no exception ")
finally:
    print("i will execute every time")
