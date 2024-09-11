import math

N = int(input())

value = math.factorial(N)

list_of_value = list(str(value))

zero_count = 0

for i in range(len(list_of_value) -1, 0, -1):

    if zero_count > 0 and list_of_value[i] != '0':
        break
    
    if list_of_value[i] == '0':
        zero_count += 1

print(zero_count)
