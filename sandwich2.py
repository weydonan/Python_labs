def bread(func):
    def wrapper():
        return "Bread\n" + func() + "Bread"
    return wrapper

def salat(func):
    def wrapper():
        return "Salat\n" + func()
    return wrapper

def tomato(func):
    def wrapper():
        return "Tomato\n" + func()
    return wrapper

def meat(func):
    def wrapper():
        return "Meat\n" + func()
    return wrapper

@bread
@meat
@tomato
@salat
def make_sandwich():
    return ""

print(make_sandwich())