import random

with open("word_database.csv") as f:
    lines = f.readlines()

database = []

for line in lines:
    newline = line.rstrip().split(",")
    database.append(newline)

stressed = {}
unstressed = {}

for line in database:
    if (line[2] == "True"):
        stressed[line[0]] = int(line[1])
    else:
        unstressed[line[0]] = int(line[1])

def write_line():
    sylls_left = 10
    line = ""
    this_word = ""
    while sylls_left > 0:
        if sylls_left % 2 == 0:
            this_word = random.choice(list(unstressed))
            line += f"{this_word} "
            sylls_left -= unstressed[this_word]
        else:
            this_word = random.choice(list(stressed))
            line += f"{this_word} "
            sylls_left -= stressed[this_word]
    print(line)

def write_poem(length):
    for i in range(1,length):
        write_line()
        