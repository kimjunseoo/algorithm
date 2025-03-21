N = int(input())

str_N = str(N)

pan = [ 0 for _ in range(10)]
count = 0
for i in range(len(list(str_N))):
    
    if str_N[i] == '9':
        if pan[9] == 1:
            if pan[6] == 1:
                count += 1
                pan = [ 0 for _ in range(10)]
            pan[6] = 1
        pan[9] = 1
    elif str_N[i] == '6':
        if pan[6] == 1:
            if pan[9] == 1:
                count += 1
                pan = [ 0 for _ in range(10)]
            
            pan[9] = 1
        pan[6] = 1
    elif pan[int(str_N[i])] == 1:
            count += 1
            pan = [ 0 for _ in range(10)]
    else: 
        pan[int(str_N[i])] = 1
        
print(count)
    

