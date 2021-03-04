# In the nutshell args and kwargs enable you to pass multiple and arbitrary inputs to a function
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

    args[0] = 12


if __name__ == '__main__':
    # test1('1', 1212, 'hey this is an arg')

    test2('hahah running into erros')
