#犬类  查询你名字  旺财 5岁 皮色 黑色 吃骨头


class  Dog(object):

    def eat(self):
        print("吃骨头")

    def info(self):
        print(self.name,self.age,self.color)
wangcai = Dog()
wangcai.name = "wangcai"
wangcai.age = 5
wangcai.color="黑"

wangcai.info()