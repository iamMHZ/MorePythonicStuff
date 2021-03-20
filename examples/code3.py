# Decorators
# You may need to debug some of the functions to see how they actually run

# first let's review Inner Functions

# Example 1
# Just an inner function
from symbol import decorated


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
# This example shows the other way of decorating a function
@decorator1
def say_another_thing():
    print('I am saying another thing lol')


if __name__ == '__main__':
    # test1()

    # test2()

    # repeat_hello = repeat('Hello')
    # repeat_hello()

    # multiply_by_12 = multiply_by(12)
    # print(multiply_by_12(3))

    # say = decorator1(say_sth)
    # say()

    say_another_thing()
