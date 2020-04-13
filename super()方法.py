class Master(object):
    def __init__(self):
        self.kongfu="古法秘方"
        self.__newname="lalala"
    def make_cake(self):
        print("制作古法煎饼果子")



class Predence(Master):
    def make_cake(self):
        print("制作新的煎饼果子")
        super(Predence, self).make_cake()
        super().make_cake()


damao = Predence()
damao.make_cake()

damao.kongfu
# damao.__newname