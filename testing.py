def longest(words):
    wordsList = words.split(" ")
    longest = wordsList[0]
    for x in wordsList:
        if len(x) > len(longest):
            longest = x
    return longest

print longest("This is Andela")