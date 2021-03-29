# list=["adi","arun","aditya","band"]
# print(list)
# for i,item in enumerate(list):
#     if(i%2==0):
#         print(item)
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:", type(obj1))
print(list(enumerate(l1)))

    # changing start index to 2 from 0
    print(list(enumerate(s1, 2)))
