import re

length = int(input())
str = input()

ans = 0

numbers = re.findall(r'\d+', str)

for n in numbers:

    ans += int(n)

print(ans)