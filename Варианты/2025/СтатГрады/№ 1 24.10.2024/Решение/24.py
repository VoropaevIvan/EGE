with open('files/24.txt') as file:
    s = 'B' + file.readline().replace('-', '*').strip()

q = '5*43541346*66*256*1*21423154624*3*33*565*26*5*2236*2*533*11*613251515*646*23625*1*4*125*4*143'

max_len = -1
for v in s.split('A')[1:]:
    v = ' ' + v.replace('**', ' ').replace('B', ' ').replace('C', ' ').replace('D', ' ') + ' '
    while ' *' in v or '* ' in v:
        v = v.replace(' *', ' ')
        v = v.replace('* ', ' ')
    for cur in v.split():
        if len(cur) >= max_len:
            print(len(cur), cur)
            max_len = len(cur)
