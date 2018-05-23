if __name__ == "__main__":
    print "Module run directly. Meant to be imported."
def functionImported():
    print "Function imported from tobeimported.py"
class Imported(object):
    def __init__(self,name):
        self.__name = name
        print "Object from Class Imported with name:",self.getName()
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name