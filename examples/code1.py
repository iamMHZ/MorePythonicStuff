# __init__ vs __new__


# showing the order of __init__ and __new__
class Test1:

    def __new__(cls, *args, **kwargs):
        print('__new__ is called')
        return super().__new__(cls)

    def __init__(self):
        print('__init__ is called')


# __new__ creates an object and __int__ initializes that object
class Test2:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        self.name = 'hey this is my name'

    def __str__(self):
        return self.name


# What if the __new__ does not return anything
class Test3:
    # __new__ doest not return an object
    def __new__(cls, *args, **kwargs):
        print('hey __new__ does not return an object')

    def __init__(self):
        self.name = 'hey this is my name'

    def __str__(self):
        return self.name


class Test4:
    # while __new__ doest not return an object the __init__ is not gonna be called
    def __new__(cls, *args, **kwargs):
        print('hey __new__ does not return an object So __init__ is not called')

    def __init__(self):
        print('Hey we do not call __init__ when __new__ does not return an object ')


# Can we return a different class in the __new__

class Test5:

    def __new__(cls, *args, **kwargs):
        return list()

    def __init__(self):
        pass


if __name__ == '__main__':
    # test = Test1()

    # test = Test2()
    # print(test)

    # test = Test3()
    # print(test)

    # test = Test4()

    test = Test5()
    print(type(test))
