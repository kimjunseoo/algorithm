N = int(input())

words = [input() for _ in range(N)]

jbjg_words = list(set(words))

jbjg_words.sort()

jbjg_words.sort(key=lambda x : len(x))

for i in range(len(jbjg_words)):
    print(jbjg_words[i])