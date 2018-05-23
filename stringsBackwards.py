message = raw_input("Enter String and I will return it backwards\n")
backwards = ""
#iterate through string
''' while message:
    backwards+=message[len(message)-1]
    message = message[:len(message)-1] '''
for x in range(len(message)-1,-1,-1):
    backwards+=message[x]
print backwards