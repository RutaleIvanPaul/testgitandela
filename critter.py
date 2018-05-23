class Critter(object):
    """A virtual pet"""
   #class attribute
    total = 0
    #Static method
    def status():
        return Critter.total
    status = staticmethod(status)
    def __init__(self,name,mood):
        Critter.total+=1
        self.name = name
        self.__mood = mood
        print "Constructor for Critter class initiated.\n"
        print "Critter called:",self.name
        print "Current mood:",self.__mood
#Overloading not like this.
 #def __init__(self,name):
 #       print "Constructor initiated and pet named:",name

    def setMood(self,mood):
        self.__mood = mood
        print "Mood set to:",self.__mood

    def getMood(self):
        return self.__mood

    def __str__(self):
        print """This Object of Critter,
            Has these attributes along with values;
            Name:""",self.name,"""
            Mood:""",self.__mood

    def nameMe(self,crittername):
        self.name = crittername
        print "You named the pet:",crittername
    
    #Not True
   # def testNamespace():
    #    print "Methods can be accessed without object instance."


crit = Critter("Critter","happy")
print crit.name
crit.nameMe("Pett")
print crit.name
crit.__str__()
print Critter.status()
print Critter("bigg","moody").total
crit3 = Critter("third","moody")
crit.setMood("Jolly")
crit.__str__()
print "Crit Mood is:",crit.getMood()
print "Crit Mood accessed wrongly is:",crit._Critter__mood
#crit.status()
#Critter.testNamespace()
#crit2 = Critter("Pett 2")