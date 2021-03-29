def gretter_than_4(n):
    if n>4:
        return True
    else:
        return False
h1=[1,3,4,65,674564,55,3]
grt=list(filter(gretter_than_4,h1))
print(grt)
