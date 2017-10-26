import sys
from math import log

def convert(s):
    '''Convert to integer'''
    x = -1
    try:
        x = int(s)
        print("Conversion successful! x = ", x)
    except (ValueError, TypeError):
        print("Conversion failed!")
    return x

# Simplified
def convert_sim(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return -1

# Raporting error with syserr
def convert_stderr(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1

# Re-rising error along with handled exception
def convert_raise(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise
# Exception of string_log will include error raised in convert_raise
def string_log(s):
    v = convert_raise(s)
    return log(v)




"""Exceptions types to handle

IndexError: when the index value is out of range

ValueError: Right type of object but incorrect value

KeyError: When we try to look for non existing key in dict  

"""

'''Not for catching - programmers errors: 

IndentationError
 
SyntaxError
 
NameError
'''
