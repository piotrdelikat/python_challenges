import sys

def heron_sqrt(x):
    '''Compute square roots using methof of Heron of Alexandria

    :param x: The number for which the square root is to be computed
    :returns: The sqiare root of x.
    :raises: ValueError: If x is negative
    '''
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    try:
        print(heron_sqrt(9))
        print(heron_sqrt(2))
        print(heron_sqrt(-1))
        print("This is never printed")
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Program execution continues normally here.")

if __name__ == '__main__':
    main()