# how to print
print("Hello world?")

# assign variable(no strict data type!)
var = "hello"
print(var)
var = 22
print(var)
var = True
print(var)

# in python, there don't have ; as command termination
# they use line break(each new line is a new command)
# however:(not recommend!)
val = 20
val = True
val = "hello"  # a string
val = 'hello'  # also a string
print(val)

isTrue = False
# python use indentation instead of braces
if not isTrue:  # if the variable is false
    print(isTrue)
else:
    print(not isTrue)
if isTrue:
    print("hello world")

# scan:
a = input("please input a var:")
print(a + "\n")
# get user input:
message = input("hello! what's your name?")
print(f"hello {message}!")
# for loop:
for i in range(4):
    print("this is a loop")
    print("===========end of loop %d===========\n" % (i + 1))
    # end of for loop

# print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))

# print octal value
print("%7.3o" % 25)

# print exponential value
print("%10.3E" % 356.08977)

# DATA TYPES
# bool : True(or anything isn't 0) ,False, 0,1
if 0:  # unreachable
    print("no hello")
if 2:  # anything other that 0 will be TRUE
    print("hello")
# int
# chr
# float

# and and or
testBoolean = ("yes" and "yes") and (1 < 2)
print("test boolean is %r" % testBoolean)
testBoolean = ("yes" and "yes") or (1 > 2)
print("test boolean is %r" % testBoolean)

# string is a array of characters
example = "hello nice to meet you"
print(example.split(" ")[3])  # meet
example += "!"  # "" '' same as java
# \n\t\'\"\\
pythonString = f"Hello I am {message} and I'm very excited to learn python and hopefully I can read the machine " \
               f"learning " \
               f"very soon! "
print(pythonString)

# manipulate the string
research = "find my name in this sentence, my name is David"
research = research.split(',')
print(research)
print(research[0])
print(research[1])
print("does this sentance have \'name\'?", research.__contains__('name'))
if 'name' in research:  # better way
    print("yes it has \'name\'")
elif 1 < 2:
    print("hello")
else:
    print("not it does not have \'name\'")
# 单引号双引号都是一样的
# \r : return to the beginning of the line

# float
a = 7.77
a += 3.33
a -= 3.33
++a
--a
print(a)

# Arrays:
students = [20, 30, 20, 30]
print(students)
# 3 20s
# 1:
what = [20] * 3
print(what)
# 2:
what = []
for i in range(3):
    what.append(20)
print(what)

# interpreted data type: you can assign the data with different data type with no error!
a = True
print(a)
a = 3.33
print(a)
a = 'j'
print(a)

# for loop
for i in range(10):
    print(i)

# while loop
price = 50
while price > 40:
    price -= 1
    print(price)
print("end of while loop")


# methods/functions
def add_two_nums(num1, num2):  # name like this!
    return num1 + num2


print(add_two_nums(1, 2))
# >>order operation matters! methods need to initiated before use it << #
# never write the same code twice


'''
print("hello world")
this is a comment
print("hello world")
'''
# this is also a comment
for letter in "hello world":
    print(letter)