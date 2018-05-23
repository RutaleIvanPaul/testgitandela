import cPickle,shelve
list1 = ["one","two","three","four","five"]
pickle_file = open("dump.dat","w")
cPickle.dump(list1,pickle_file)
pickle_file.close()
#unpickling stored object.
list_unpickled = cPickle.load(open("dump.dat","r"))
print list_unpickled
dictionary1 = {"Entry one":"Value one","Entry two":"Value two","Entry three":"Value three"}
cPickle.dump(dictionary1,open("dump.dat","a"))

