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