class Student(object):
    def __init__(self):
        self.__age=20


    def set_age(self,age):
        self.__age=age

    def get_age(self):
        print(self.__age)


xiaoming=Student()
xiaoming.get_age()
xiaoming.set_age(30)
xiaoming.get_age()