num = int(input())

line = 0
line_end = 0

while line_end < num:
    line += 1
    line_end += line

gap = line_end - num

if line % 2 == 0:
    print(str(line - gap) + '/' + str(1 + gap))
else:
    print(str(1 + gap) + '/' + str(line - gap))