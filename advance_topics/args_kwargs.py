def pritnmarks(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
marklist={"adi":22,"aditya":44,"zeus":55,"tyrant":66}
pritnmarks(**marklist)