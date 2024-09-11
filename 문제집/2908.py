A,B = map(int, input().split())

l_A = list(str(A))
l_B = list(str(B))

l_A.reverse()
l_B.reverse()

print(max(int(''.join(l_A)), int(''.join(l_B))))