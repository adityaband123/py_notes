"""Bisect_module is the module contains bisect functionwhich tells
the position of the newly inserted element
and the insort is the another function in the bisect module
which actually prints this element at the specific position
"""
import bisect
num=4
list=[2,4,5,6,7,8,9]
print(bisect.bisect(list,num))
bisect.insort(list,num)
print(list)
