class Master(object):
    def __init__(self):
        self.kongfu="古法煎饼果子秘籍"

    def __str__(self):
        return(self.kongfu)

    def make_cake(self):
        print("我会%s秘方"% self.kongfu)

    def dayandai(self):
        print("dayandai")


class School(object):
    def __init__(self):
        self.kongfu = "现代煎饼果子秘籍"

    def __str__(self):
        return(self.kongfu)

    def make_cake(self):
        print("我会%s秘方" % self.kongfu)

    def xiaoyandai(self):
        print("xiaoyandai")


class haizi(School,Master):
    pass


damao = haizi()
print(damao)
damao.make_cake()
damao.dayandai()
damao.xiaoyandai()
