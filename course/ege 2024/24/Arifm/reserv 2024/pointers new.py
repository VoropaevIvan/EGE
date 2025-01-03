# with open('bI4DufyyF.txt') as file:
#     s = file.readline().strip()


s = '1+4+5*0*4'
l = 0
r = 0
while True:
    if not(s[r] in '+*' and s[r-1] in '+*') and \
            not(s[r] == '0' and s[r-1] == '0' and s[r-2] in '+*') \
            and not (s[r] in '123456789' and s[r-1] == '0' and s[r-2] in '+*'):
        r+=1
    else:
        if s[r-1] in '*+':
            r-=1
        if l<=r:
            l+=1
    if eval(s[l:r+1]) == 0:
        ans = max(ans, r-l+1)
        print(s[l:r+1])
print(ans)


