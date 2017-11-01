import sys
import os
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

# Look Before You Leap: LBYL -> checks only for file existence
p = '/path/to/datafile.dat'

if os.path.exists(p):
    process_file(p)
else:
    print('No such file as {}'.format(p))

# It's Easyer to Ask Forgiveness than Permission: EAFP -> mode pythonic approach
try:
    process_file(p)
except OSError as e:
    print('Could not process file becouse {}'.format(str(e)))

# Clean-up with finally-block that is executed unconcerned of try-except outcome
def make_at(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)

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
