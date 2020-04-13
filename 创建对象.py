class Hero(object):


    def move(self):
        print(id(self))
        print('hero can move')



wukong = Hero()

wukong.move()

wukong.name="悟空"
wukong.age=20
wukong.hp=3000
wukong.atk=400


print(wukong.name,wukong.age,wukong.hp,wukong.atk)

print(wukong)

print(id(wukong))