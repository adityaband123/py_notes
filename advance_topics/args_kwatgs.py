#  *args and **kwargs tutorial
#  *vars and **kvars turorialf
#we can access the elements with the help of the *args
def documentry(*args):
    if(len(args)==2):
          print("name is:",args[0],"age is:",args[1],"roll_number is:",args[2])
    else:
        print("name is:", args[0], "age is:", args[1])
documentry("aditya",44,2)
