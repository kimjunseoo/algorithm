T = int(input())

for i in range(T):

    H, W, N = map(int, input().split())

    hotel = []

    for j in range(1, W+1):
        for i in range(1, H+1):

            hotel.append(i * 100 + j)

    print(hotel[N-1])