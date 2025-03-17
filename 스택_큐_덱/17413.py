from collections import deque

S = input()
ans = []
tagFlag = False
reverseWord = deque()

for i in range(len(S)):
    if S[i] == '<':
        ans.append(''.join(reverseWord))
        reverseWord.clear()
        tagFlag = True
        ans.append(S[i])
    elif tagFlag == True:
        ans.append(S[i])
        if S[i] == '>':
            tagFlag = False
    elif S[i] == ' ':
        reverseWord.append(' ')
        ans.append(''.join(reverseWord))
        reverseWord.clear()
    elif  len(S) - 1 == i:
        reverseWord.appendleft(S[i])
        ans.append(''.join(reverseWord))
        reverseWord.clear()
    else: 
        reverseWord.appendleft(S[i])

for a in ans:
    print(a, end='')