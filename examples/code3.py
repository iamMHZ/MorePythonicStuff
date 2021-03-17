# Decorators
# You may need to debug some of the functions to see how they actually run


# Example 1
# Just an inner function
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


if __name__ == '__main__':
    # test1()

    # test2()

    # repeat_hello = repeat('Hello')
    # repeat_hello()

    multiply_by_12 = multiply_by(12)
    print(multiply_by_12(3))
