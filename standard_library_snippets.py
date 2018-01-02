#  OS
import os


#os.chdir('..')      # change current directory
print(os.getcwd())  # get current directory
#os.system('mkdir byOS')  # run command in the system dir

# dir(os)  # list all functions in the module
# help(os)  # help for the module

#################################################

# shutil - high level integrations with operating systemn
import shutil

#shutil.copyfile('data.db', 'archive.db')
#shutil.move('/build/executables', 'installdir')


#################################################
# glob

import glob

print(glob.glob('*.py')) # makes list with all python files
#filenames = glob('sales*.csv') # iterable with all the CSV
# to dataframe
# dataframes = [pd.read_csv(f) for f in filenames]

#################################################
# SYS

import sys


print(sys.argv) #get path and arguments as a list

#to write message to the console
sys.stdout.write('The message text\n')

#to write error message to the console
sys.stderr.write('This will be passed to the console \n')

#to terminate the script
# sys.exit()

#################################################
# Re
import re

print(re.findall(r'\bf[a-z]*', 'Rollo is a french dog lead by fictional facts and arguments'))

# Always prefer to use simpler string methods
text = 'tea or coffee'
print(text.replace('coffee', 'line'))

#################################################
# Random
import random

random.choice(['apple', 'pear', 'banana'])

random.sample(range(100), 10)
# [30, 12, 3, 7, 89, 41, 70, 33, 92, 28]

random.randrange(6)  # random integer from range
# 4

random.random()  # random float
# 0.7909690676817883
