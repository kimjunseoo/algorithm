import sys

def recur(number, output):



    if number == M:
        sys.stdout.write(output+"\n")
        return

    for i in range(1, N + 1):
        if str(i) in output.split():
            continue
        recur(number+1, output+str(i)+" ")


N, M = map(int, input().split())

recur(0, "")

#if len(set(output.split())) == len(output.split()):
""" if len(set(output.split())) == len(output.split()):
        if number == M:
            sys.stdout.write(output+"\n")
            return """