arr = []

학점총합 = 0
전공과목별의합 = 0

for i in range(20):

    
    과목, 학점, 등급 = map(str, input().split())

    if 등급 == "P":
        continue

    학점 = float(학점)

    학점총합 += 학점

    if 등급 == "A+":
        등급 = 4.5
    elif 등급 == "A0":
        등급 = 4.0
    elif 등급 == "B+":
        등급 = 3.5
    elif 등급 == "B0":
        등급 = 3.0
    elif 등급 == "C+":
        등급 = 2.5
    elif 등급 == "C0":
        등급 = 2.0
    elif 등급 == "D+":
        등급 = 1.5
    elif 등급 == "D0":
        등급 = 1.0
    elif 등급 == "F":
        등급 = 0.0
    
    전공과목별의합 += 학점 * 등급

print(전공과목별의합 / 학점총합)
    