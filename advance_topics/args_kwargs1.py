def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
list=["adi",55,22]
marklist={"adi":22,"aditya":44,"zeus":55,"tyrant":66}
(master("normal args",*list,**marklist))