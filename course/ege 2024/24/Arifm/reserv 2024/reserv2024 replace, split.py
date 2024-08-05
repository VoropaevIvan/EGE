with open('reserv2024.txt') as file:
    s = file.readline().strip()

#s = '120*10*1+0*123'
#s = '01*0+1000*10*1*1*1+1+0'
s = ' ' + s
for x in '23456789':
    s = s.replace(x, '1')

s = s.replace('++', ' ')
s = s.replace('*+', ' ')
s = s.replace('+*', ' ')
s = s.replace('**', ' ')

s = s.replace('* ', ' ')
s = s.replace('+ ', ' ')
s = s.replace(' *', ' ')
s = s.replace(' +', ' ')

s = s.replace('+01', '+0 1')
s = s.replace('*01', '+0 1')
s = s.replace('+00', '+0 0')
s = s.replace('*00', '*0 0')
while ' 00' in s:
    s = s.replace(' 00', ' 0 0')
s = s.replace('01', '0 1')
#print(s)
print('_____')
new_str = ' '
for x in s.split():
    if ('+' in x) or ('*' in x):
        plus_split = x.split('+')
        #print(x)
        for s_t in plus_split:
            mul_split = s_t.split('*')
            if '0' in mul_split:
                new_str = new_str + '+' + s_t
            elif '0*' in s_t:
                pos = s_t.find('0*')
                new_str = new_str + ' +' + s_t[pos:]
            else:
                new_str += ' '
new_str = new_str.replace(' +', ' ')
a = max(new_str.split(), key=len)
print(new_str)
print(len(a))