class Master(object):
    def __init__(self,name):
        self.name=name
        self.kongfu="古法煎饼果子"

    def make_cake(self):
        print("%s会<%s>秘籍" % (self.name,self.kongfu))



lishifu=Master("lishifu")
lishifu.make_cake()


class Presient(Master):
    pass


damao = Presient("damao")
damao.make_cake()