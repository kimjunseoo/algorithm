s = list(input())
bomb = list(input())
result = []

for i in s:
    result.append(i)
    
    if len(result) < len(bomb):
        continue
    else:
        if result[-len(bomb):] == bomb:
            del result[-len(bomb):]

if len(result) == 0:
    print('FRULA')
else:
    for s in result:
        print(s, end='')
