f = open('ex_text.txt', mode='wt', encoding='utf-8')
help(f)

f.write('Yellow duck and big brown dog,' )

f.write('live together in the woods\n')

f.write('Eating mostly mushrooms')

f.close()