# yield vs return
def h():
    print("hello")
    yield 1
    print("xxxx")
    yield 2
    print("bye")
    yield 3


gen_1 = h()  # create a generator
answer_1 = gen_1.__next__()  # h() 开始执行，直到遇到yield，输出拿到yield值
print(answer_1)  # 1

answer_2 = gen_1.__next__()  # h() 继续执行，直到遇到第二个yield
print(answer_2)

answer_3 = gen_1.__next__()  # h() 继续执行，直到遇到第三个yield
print(answer_3)

# 如果继续使用next（）， 会报错因为之后没有yield了

print('##############################################################')


def g():
    m = yield -1
    d = yield 4
    c = yield m


gen_2 = g()
answer_1 = gen_2.__next__()  # -1
print(answer_1)  # -1
answer_2 = gen_2.send('hello')  # answer_2 得到了下一个yield值：4，而且将前一个yield改成了hello
print(answer_2)  # 4
answer_3 = gen_2.send(None)  # send 中不加东西 == next()
print(answer_3)  # 得到了下一个yield值：m，此时m被send改成了 hello，所以print（hello）

print('##############################################################')
# throw(), close() 来中断 Generator
# close() = throw(GeneratorExit_exception)
def f():
    m = yield -1
    d = yield 4
    c = yield m

f = f()
print(f.__next__())
f.close()
print('hello')
print(f.__next__())  # close 终止了 generator, 这行没有运行
# yield 生成器相比 return一次返回所有结果的优势：
#
# （1）反应更迅速
#
# （2）更节省空间
#
# （3）使用更灵活

