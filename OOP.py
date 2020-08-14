class Student:
    pass  # python know you just want to skip


class Dog:
    def __init__(self, name, kind, age):
        self.__age = age  # __make it private
        self.__name = name
        self.__kind = kind

    def setAge(self, age):
        self.__age = age

    def setName(self, name):
        self.__name = name

    def setKind(self, kind):
        self.__kind = kind

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def getKind(self):
        return self.__kind


Alice = Student()  # auto use __init__ method
David = Student()

FirstDog = Dog("whatever", "water_ver", -1)
FirstDog.setAge(20)
FirstDog.setKind("abc")
FirstDog.setName("Your dad")
print("Dog name : %s,kind: %s,age: %d" % (FirstDog.getName(), FirstDog.getKind(), FirstDog.getAge()))
