class Person(object):
    def __init__(self):
        self.name="xiaoming"
        self.age=20

    def eat(self):
        return ("肯德基")



class Dog(object):
    def __init__(self):
        self.name="旺财"
        self.age=2

    def eat(self):
        return ("啃骨头")



wangcai = Dog()
xiaoming = Person()


def print_attribute(object):
    print("%s爱吃%s" % (object.name,object.eat()))


print_attribute(wangcai)
print_attribute(xiaoming)