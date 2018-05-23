try:
    inputText = int(raw_input("Will throw exception if you dont enter number here:\n"))
    print inputText
except(ValueError), e:
    print "Thrown Exception."
    print "Python says:"
    print e
else:
    print "The number you entered was:",inputText