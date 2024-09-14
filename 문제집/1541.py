Sik = input()

numbers = list(Sik.split('-'))
final_numbers = []

for number in numbers:

    if '+' in number:
        string = list(number.split('+'))
        value = 0
        for a in string:
            value += int(a)
        final_numbers.append(value)
    else:
        final_numbers.append(int(number))

answer = final_numbers[0]

if len(final_numbers) > 1:
    for i in range(1, len(final_numbers)):
        answer -= final_numbers[i]
     
    print(answer)
else:
    print(answer)