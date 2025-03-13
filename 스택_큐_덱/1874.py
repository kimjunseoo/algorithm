n = int(input())
s = 1
stack = []
ans = []
flag = ''

for i in range(1,n+1):
    num = int(input())

    while s <= num:
        stack.append(s)
        s += 1
        ans.append('+')

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        flag = 'NO'

if flag == 'NO':
    print(flag)
else: 
    for i in range(len(ans)):
        print(ans[i])