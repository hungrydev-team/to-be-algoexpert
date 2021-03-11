# 1316 그룹 단어 체커

num_word = int(input())
words = [input() for i in range(num_word)]
group_word = 0

for word in words:
    foo = word[0]
    letter_list = [word[0]]
    for letter in word:
        if foo == letter:
            pass
        else:
            foo = letter
            letter_list.append(letter)
    if len(letter_list) == len(set(letter_list)):
        group_word += 1

print(group_word)
