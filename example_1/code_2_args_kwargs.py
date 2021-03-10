# In the nutshell args and kwargs enable you to pass optional, multiple, and arbitrary inputs to a function
# 'args' and 'kwargs' are just the arbitrary names you can choose whatever you want but they are conventions
# so it would be better to stick with them

# Example 1
# args, passing an arbitrary list of variables
def test1(*args):
    for a in args:
        print(a)


# Example 2
# args is a tuple not a list so it means that it is immutable
def test2(*args):
    print('Hey args is of type tuple')
    print(args[0])
    print(type(args))
    # args is of tuple type
    args[0] = 12


# **kwargs does the same thing as *args but the only difference is that they have names

# Example 3
# kwargs is of type dictionary
def test3(**kwargs):
    print(type(kwargs))


# Example 4
# printing the keys of kwargs as it is a dictionary
# printing the names of the passed variables to the function
def test4(**kwargs):
    for key in kwargs.keys():
        print(key)


# Example 5
# printing the values of the passed variables ( dictionary's values)
def test5(**kwargs):
    for val in kwargs.values():
        print(val)


# TODO Add about * **

if __name__ == '__main__':
    # test1('1', 1212, 'hey this is an arg')

    # test2('hahah running into erros')

    # test3()

    # test4(name='mhz', age=12)
    # test4(**{'name': 'mhz', 'age': 12})

    test5(name='mhz', age=12)
