#map(function_to_apply,list fo inputs)
def square(n):
     return n**2
h1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sq=[]
# for i in h1:
#     sq.append(i**2)
# print(sq)
sq=list(map(square,h1))
print(sq)
