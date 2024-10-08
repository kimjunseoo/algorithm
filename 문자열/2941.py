s = list(input())

ans = 0

for i in range(len(s)):

    if i == len(s) - 1:
        break
    
    if i <= len(s) - 3:
        if s[i]+s[i+1]+s[i+2] == 'dz=':
        
            s[i] = '0'
            s[i+1] = '0'
            s[i+2] = '0'

            ans += 1
            continue

    if s[i]+s[i+1] in ['c=','c-','d-','lj','nj','s=','z=']:
        
        s[i] = '0'
        s[i+1] = '0'

        ans += 1
    

for s_ in s:
    if s_ != '0':
        ans += 1 


print(ans)