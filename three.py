#Program checking length and content of string
message = raw_input("Enter any string and I will tell you the contained letters and length:\n")
print"The string is ",len(message),"characters long.\n"
#create list to store characters
characterslist = []
for x in message:
    if x is " ":
        continue
    elif x in characterslist:
        continue
    else:
        characterslist.append(x)

print(characterslist)