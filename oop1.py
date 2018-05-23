class One(object):
    def __init__(self,name,age=0):
        self.__name = name
        self.__age = age
        
    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def invokeMethodone(self,objectTwo):
        print "Method one."
        objectTwo.invokeMethodtwo()
    def __str__(self):
        strg = "Object from class Three.\nName:",self.getName(),"\nAge:",self.getAge()
        return strg
    
class Two(object):
    def invokeMethodtwo(self):
        print "Method two invoked."

class Three(One):
    def __init__(self,name,age=0,sex=""):
        super(Three,self).__init__(name,age)
        self.__sex = sex
        
    def setSex(self,sex):
        self.__sex = sex
    def getSex(self):
        return self.__sex
    def __str__(self):
        strg = "Object from class Three.\nName:",self.getName(),"\nAge:",self.getAge(),"\nSex:",self.getSex()
        return strg

fromTwo = Two()
fromOne = One("Rutax")
print fromOne.__str__()
fromThree = Three("IVan")
print fromThree.__str__()
fromOne.invokeMethodone(fromTwo)