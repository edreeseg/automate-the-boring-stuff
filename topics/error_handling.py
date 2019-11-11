def div42by(divideBy):
    return 42 / divideBy

print(div42by(2))
print(div42by(12))
print(div42by(0)) # Will throw ZeroDivisionError
print(div42by(1))

#############

def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0)) # Will return None and print error
print(div42by(1))

# You can also use an except statement without specifying the type of error,
# this will cause all errors to run code in except block

def cat_counter():
    numCats = input()
    try:
        n = int(numCats)
        if n >= 4:
            print('That is a lot of cats.')
        elif n < 0:
            print('That is an impossible number of cats.')
        else:
            print('That is not that many cats.')
    except ValueError:
        print('You did not enter a number.')