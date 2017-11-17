g = open('ex_text.txt', mode='rt', encoding='utf-8')
g.read(32)  # Read first 32 characters
g.read()  # Read the rest of the text

g.seek(0)  #  Resets the reader to starting position
# 0
g.readline()
# 'Yellow duck and big brown dog, live together in the woods\n'
g.readline()
# 'Eating mostly mushrooms'
g.seek(0)

g.readlines()  # Reading lines to a list
g.close()