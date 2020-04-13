# f=lambda : print('hello world')
# f()


# (lambda : print('hello world'))()
#
# f=lambda :3.14
# print(f())

# f=lambda name: print('nihao %s' % name)
# f('aa')


# f= lambda a,b : a+b
# ret = f(1,3)
# print(ret)

#排序
# my_list=[1,2,5,3,6]
# my_list.sort()
# print(my_list)

my_list=[{"name":"xiaoming","class":"bb","age":3},{"name":"zz","class":"xx","age":9},{"name":"cc","class":"yy","age":5}]
my_list.sort(key=lambda my_key: my_key["age"])
print(my_list)

