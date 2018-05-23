print """===>WELCOME TO THE GUESS MY NUMBER GAME<===
                I CHOOSE A NUMBER FROM 0 TO 100"""
raw_input("\Press Enter to continue")
print """
                YOU TRY TO GUESS THAT NUMBER WITH HINTS FROM ME.
                GUESS MY NUMBER IN LESS THAN 5 TIMES """
raw_input("\Press Enter to continue")
print """UNDERSTOOD?"""
raw_input("\Press Enter to continue")
import random
def takeguess(mynumber):
    print """HINT:MY NUMBER IS WAY BELOW""",mynumber*2
    for x in range(5):
        guess = int(raw_input("""ENTER GUESS:"""))
        if guess < mynumber:
            print """LOW"""
        elif guess < mynumber/2:
            print """ TOO LOW"""
        elif guess > mynumber:
            print """HIGH"""
        elif guess > mynumber*2:
            print """TOO HIGH"""
        elif guess is mynumber:
            print """GOT IT"""
            break
        else:
            pass
    print"""TURNS ARE DONE"""
    print """The number was""",mynumber,"""!""" 
takeguess(random.randrange(100)+1)
#import two
#two.takeAge