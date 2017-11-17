h = open('ex_text.txt', mode='at', encoding='utf-8')
h.writelines(
    ['If you want specify new line like this,\n',
     'You need to do this yourself',
     'with new line character \n',
     'otherwise it will be the same line'])
h.close()