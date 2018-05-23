import cPickle,shelve
shelf = shelve.open("shelf.dat")
shelf["list1"] = ["1","2","3"]
shelf["list2"] = ["one","two","three"]
shelf.sync()
shelf2 = shelve.open("shelf.dat")
print shelf2["list2"]