text_file = open("readit.txt","r")
print text_file
print text_file.read(10)
print text_file.readline()
text_file_list = text_file.readlines()
print text_file_list
#first close file due to bookmark
text_file.close()
text_file = open("readit.txt","r+")
print "After closing and reopening"
print text_file.readlines()
print "You can print the items from the list too."
for line in text_file.readlines():
    print line
#File had reached end at this point. Need to close and reopen
text_file.close()
#text_file = open("readit.txt","r")
for line in open("readit.txt","r").readlines():
    print line

#now to write into file
write_file = open("write_file.txt","w")
write_file.write("This line 1\nLine 2 now\nThen Line 3")
#print write_file.readlines()
write_file.close()
#nothing printed because pointer at end
#print open("write_file.txt","w+").readlines() this rewrites the file. be careful with modes
print open("write_file.txt","r").readlines()

dictionaryFile = {"Entry one":"Value one","Entry two":"Value two","Entry three":"Value three"}
write_dictionary = open("dict.txt","w+")
write_dictionary.writelines(dictionaryFile)
for entry in dictionaryFile:
    write_dictionary.write(entry)
    write_dictionary.write("\n")
    write_dictionary.write(dictionaryFile[entry])
    write_dictionary.write("\n")
write_dictionary.close()