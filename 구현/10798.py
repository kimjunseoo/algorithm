arr = [[ -1 for _ in range(15)] for _ in range(5)]

for i in range(5):

    string = input()

    for j in range(len(string)):
        arr[i][j] = string[j]
        
for i in range(15):

    for j in range(5):
        
        if arr[j][i] != -1:
            print(arr[j][i], end = '')