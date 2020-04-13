class Hero(object):

    def __init__(self,name,blood,apk):
        self.name=name
        self.blood=blood
        self.apk=apk
        print("创建成功")


    def __str__(self):
        print("ziduan")
        return("name:%s,blood:%d,apk:%d" % (self.name,self.blood,self.apk))




    def __del__(self):
        print("byebye")

gailun=Hero("gailun",3000,400)
gailun1=gailun
gailun2=gailun

del gailun

input("input something:")
