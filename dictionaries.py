dictionaries = {"RealNigga":"Rutale","RealestNigga":"Still Rutale","Gangsta":"Guess who,Rutale"}
print "Wlecome to the Real Nigga Dictionary."
print "Choose an operation."
choice = ""
while choice != "0":
    print "1.Search Term 2. Add Term 3. View Full Dictionary 4. Redefine Term 0.Exit"
    choice = raw_input("Enter Choice Here\n")
    if choice is "0":
        print "BYE"
        break
    elif choice is "1":
        key = raw_input("Input search key:\n")
        print dictionaries.get(key,"Term is not in dictionary")
    elif choice is "2":
        addKey = raw_input("Input key:\n")
        if addKey in dictionaries:
            print "Term for that key already exists"
        else:
            addValue = raw_input("Input Term:\n")
            dictionaries[addKey] = addValue
    elif choice is "3":
        print "Full Dictionary so Far:\n"
        for x in dictionaries:
            print "\t",x,"\t",dictionaries[x],"\n"
    elif choice is "4":
        redefineKey = raw_input("Enter key for term to redefine\n")
        if redefineKey in dictionaries:
            dictionaries[redefineKey] = raw_input("Input new Definition\n")
        else:
            print "Key Doesn't Exist."
    else:
        print "Your choice is Invalid."
