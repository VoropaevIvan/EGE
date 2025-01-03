alf = 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
count = 0
with open('files/10/Понедельник начинается в субботу.txt') as file:
    s = '!' + file.read() + '!'
    cur_word = ''
    for x in s:
        if x in alf:
            cur_word += x
        else:
            if cur_word:
                if (cur_word[0] in 'аА') and (cur_word[-1] in 'яЯ'):
                    print(cur_word)
                    count += 1
            cur_word = ''
print(count)

