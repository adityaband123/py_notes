from functools import reduce
def sum(a,b):
    return a+b
lis=reduce(sum,[1,2,3,4,5,6])
print(lis)