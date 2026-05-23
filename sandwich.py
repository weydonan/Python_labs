def bread(func):
    def wrapper():
        print("Bread")
        func()
        print("Bread")
    return wrapper

def salat(func):
    def wrapper():
        print("Salat")
        func()
    return wrapper

def tomato(func):
    def wrapper():
        print("Tomato")
        func()
    return wrapper

def meat(func):
    def wrapper():
        print("Meat")
        func()
    return wrapper

@bread
@meat
@tomato
@salat
def make_sandwich():
    pass

make_sandwich()