class Dog(object):
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color


    def __str__(self):
        return('name:%s  age:%d  color:%d' % (self.name,self.age,self.color))


dog = Dog("wangcai",5,000)

print(dog)