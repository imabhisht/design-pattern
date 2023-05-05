class Singleton:
    __instance = None
    
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            return Singleton()
        return Singleton.__instance        
 
    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            print("Im here")
            Singleton.__instance = self

# Test the implementation
s1 = Singleton.getInstance()
print("Object created: ", s1)

s2 = Singleton.getInstance()
print("Object created: ", s2)

if id(s1) == id(s2):
    print("Singleton works, both variables contain the same instance.")
else:
    print("Singleton failed, variables contain different instances.")