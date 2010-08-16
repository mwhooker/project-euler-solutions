total = 0
line_num = 1

def word_worth(word):
    worth = 0
    for i in word:
        worth += (ord(i.lower()) - 96)

    return worth


with open('names.txt') as f:
    for line in f:
        total += word_worth(line.rstrip()) * line_num
        line_num += 1

print total

