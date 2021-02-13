import re
from random import randint

with open('ef_list.txt') as f:
    ef_list = f.read().splitlines()

with open('cmu_list.txt') as f:
    cmu_list = f.read().splitlines()

database = []

for entry in cmu_list:
    this_word = entry.split(" ")[0]
    if this_word in [word.upper() for word in ef_list]:
        string = ""
        sylls = re.findall(r"\d", string.join(entry.split(" ")[1:]))
        syllcount = len(sylls)
        stressed = bool(int(sylls[0]))
        db_entry = f"{this_word},{syllcount},{stressed}"
        database.append(db_entry)
        
def write_line():
    sylls_left = 10
    rand_range = len(database)
    line = ""
    while sylls_left > 0:
        if sylls_left % 2 == 0:
            stress = False
        else:
            stress = True
        rand_num = randint(0,rand_range - 1)
        choice = database[rand_num].split(",")
        print(choice)
        print(stress)
        if (int(choice[1]) < sylls_left) and (stress == bool(choice[2])):
            line += choice[0]
            sylls_left -= int(choice[1])
    print(line)
    
    
    

# for word in ef_list:
#     word = word.upper()
    