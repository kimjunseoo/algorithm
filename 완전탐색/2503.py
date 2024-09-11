
try_count = int(input())

hint = [list(map(int, input().split())) for _ in range(try_count)]
answer = 0
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            cnt = 0
            #자리의 수가 서로 같은 경우 제외
            if ( a == b or b == c or a == c):
                continue

            for h in hint:
                hint_number = list(str(h[0]))
                hint_strike_count = h[1]
                hint_ball_count = h[2]

                # abc와 hint_number를 비교
                strike_count = 0
                ball_count = 0

                if int(hint_number[0]) == a :
                    strike_count += 1
                if int(hint_number[0]) == b or int(hint_number[0]) == c :
                    ball_count += 1 

                if int(hint_number[1]) == b :
                    strike_count += 1
                if int(hint_number[1]) == a or int(hint_number[1]) == c :
                    ball_count += 1 

                if int(hint_number[2]) == c :
                    strike_count += 1
                if int(hint_number[2]) == a or int(hint_number[2]) == b :
                    ball_count += 1 

                if(ball_count == hint_ball_count and strike_count == hint_strike_count):
                    cnt += 1


            if(cnt == try_count):
                answer += 1
        
print(answer)