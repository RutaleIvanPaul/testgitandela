''' inventory = ()
inventoryTwo = (3,4,2,32,2,2)
#inventory+=inventoryTwo
#print inventory
#tuples are immutable
for x in range(5):
   # print "\nEnter inventory element",x+1,"."
    inventoryTwo = (x)
    inventory+=inventoryTwo

print "You entered",len(inventory),"items. And they are:\n"
for x in range(5):
    print(inventory[x]) 
 '''
 #now we try the jumble Game
print """===>WELCOME TO THE JUMBLED WORD GAME<===
                I PRESENT A JUMBLED WORD"""
raw_input("\Press Enter to continue")
print """
                YOU TRY TO GUESS THAT WORD.
                GUESS MY WORD IN LESS THAN 5 TRIES """
raw_input("\Press Enter to continue")
print """                           UNDERSTOOD?"""
raw_input("\Press Enter to continue")
import random
words = ("python","great","awesome","game","tame","people")
def jumbler():
    word = random.choice(words)
    #now to jumble the word
    correct = word
    jumbled = ""
    while word:
        position = random.randrange(0,len(word))
        #print position
        jumbled += word[position]
        word = word[:position]+word[position+1:] 
    guess=""
    count = 0
    print """******THE JUMBLED WORD IS:""",jumbled,"""*******"""
    while count != 5:
        count+=1
        guess = raw_input("\nEnter Guess:\n ")
        if guess !=correct:
            if count is 5:
                print """OUT OF CHANCES"""
                print """...GAME OVER...."""
                break
            print "Wrong!...Guess again"
            print 5-count,"tries left."
            continue
        else:
            print """******!!!WINNER!!!******"""
            break
    
    print "Would you like to continue?"
    answer=raw_input("\n Enter Y or N\n")
    if answer is "y" or "Y":
        jumbler()
    else:
        print "BYE"
jumbler()

