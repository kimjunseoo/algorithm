N = int(input())

M = int(input())

S = input()

key = "IOI"

count = i = answer = 0

while i < (M-1):
    
    if S[i: i+3] == key:

        i += 2

        count += 1

        if count == N:
            answer += 1

            count -= 1
    else:
        i += 1
        count = 0

print(answer)