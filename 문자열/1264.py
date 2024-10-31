while True:
    string = list(input())
    
    if string[0] == "#":
        break

    cnt = 0

    for s in string:
        if s in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            cnt += 1

    print(cnt)