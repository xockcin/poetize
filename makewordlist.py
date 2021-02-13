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


    
    

# for word in ef_list:
#     word = word.upper()
    