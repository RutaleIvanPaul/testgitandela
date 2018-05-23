scores = []
choice = ""
while choice !="0":
    choice = raw_input("""
    What would you like to do to your score list?\n
                1. Update
                2. Remove Score
                3. Sort
                4. Exit\n""")
    if choice is "1":
        scores.append(raw_input("Input new score: \n"))
        print scores
    elif choice is "2":
        removed = raw_input("Which score would you like to remove?\n")
        if removed in scores:
            scores.remove(removed)
        else:
            print"Score not in List."
    elif choice is "3":
        scores.sort(reverse=False)
        print scores
    elif choice is "4":
        break
    else:
        print "Invalid Selection."
