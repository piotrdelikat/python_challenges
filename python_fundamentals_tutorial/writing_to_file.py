f = open('ex_text.txt', mode='wt', encoding='utf-8')

help(f)  # as everything in python is object you can get help on instances too

f.write('Yellow duck and big brown dog, ')

f.write('live together in the woods\n')

f.write('Eating mostly mushrooms')

f.close()


# as explicit is better than implicit it is better to specify encoding

# open() modes
# 'r' - (default) open for readning
# 'w' - open for writing, it truncate the file at first
# 'x' - exclusive creation, fails if the file already exist
# 'a' - appending to the end of already existing data in file
# 'b' - binary mode
# 't' - (default) text mode
# '+' - open a disk file for updating (reading and writing)
# 'U' - (backwards compatibility) universal newlines mode; not to use in new code