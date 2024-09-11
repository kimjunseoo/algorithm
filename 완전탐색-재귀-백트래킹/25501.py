def recursion(s, l, r, c):
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

N = int(input())

for i in range(N):
    S = input()

    return_value, call_count = isPalindrome(S)

    print(return_value, call_count + 1)