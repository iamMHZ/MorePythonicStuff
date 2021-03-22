# Decorators
# You may need to debug some of the functions to see how they actually run

# first let's review Inner Functions

# Example 1
# Just an inner function
from symbol import decorated
import random
import string


def test1():
    print('Above inner')

    def inner():
        print('Inside the inner')

    inner()
    print('Below inner')


# Example 2
# returning the inner function
# Inner functions are good for encapsulation and hiding stuff
def test2():
    def inner(message):
        print(message)

    return inner('Inside inner function ywwwhwwww')


# Example 3
# An inner function that can be called
def repeat(message):
    def inner():
        print(message)
        print(message)
        print(message)

    return inner


# Example 4
# another inner function returning that can be reused
def multiply_by(number):
    def inner(another_number):
        return number * another_number

    return inner


# Decorators

# Example 1
# A simple decorator showing the simple way of using them
# check out the main method and see how we called it
def decorator1(func):
    def inner():
        print('Before ')

        func()

        print('After')

    return inner


def say_sth():
    print("Hallo My sth is nothing")


# Example2
# This example shows the other way of decorating a function (using '@nameOfDecorator')
@decorator1
def say_another_thing():
    print('I am saying another thing lol')


# Example 3
# Passing the function arguments to the decorator
# The following code has this error : inner() takes 0 positional arguments but 1 was given
def decorator2(func):
    def inner():
        func()

    return inner


@decorator2
def print_message(message):
    print('The message is: ' + str(message))


# Example 4
# A correct way of example 3
def decorator3(func):
    def inner(msg):
        func(msg)

    return inner


@decorator3
def print_message2(message):
    print('The message is: ' + str(message))


# Example 5
# A better way to handle arguments passed to a decorator
# using args and kwargs you can pass multiple arguments to a function
def decorator_that_handles_arguments(func):
    def inner(*args, **kwargs):
        print('kwargs: ' + str(kwargs))
        print('args: ' + str(args))
        print('Hey I am counting: ')

        if args:
            func(*args)
        else:
            func(**kwargs)

    return inner


@decorator_that_handles_arguments
def count(star, end):
    for i in range(star, end):
        print(i)


# Example 6
# The below code shows the wrong way of returning values while
# The problem is tha we don't return anything from the inner function
def decorator4(func):
    def inner(*args, **kwargs):
        func(*args)

    return inner


@decorator4
def generate_random_number(start, end):
    return random.randint(start, end)


# Example 6
# if your decorated function returns something make sure that
# your inner function in the decorator returns the thing
# that you want
def decorator_that_knows_correct_returning(func):
    def inner(*args, **kwargs):
        value_to_return = func(*args)

        return value_to_return

    return inner


@decorator_that_knows_correct_returning
def return_random_message(message_size):
    message = ''
    for _ in range(message_size):
        message += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)

    return message


# TODO add/see some real-world decorators from opensource projects
if __name__ == '__main__':
    # test1()

    # test2()

    # repeat_hello = repeat('Hello')
    # repeat_hello()

    # multiply_by_12 = multiply_by(12)
    # print(multiply_by_12(3))

    # say = decorator1(say_sth)
    # say()

    # say_another_thing()

    # print_message2('message is nothingggggg ...')

    # count(2, 5)
    # count(star=2, end=5)

    # random_int = generate_random_number(10, 100)
    # print(random_int)  # the output will be None because of no returning anything from inner function in the decorator

    random_string = return_random_message(20)
    print(random_string)
