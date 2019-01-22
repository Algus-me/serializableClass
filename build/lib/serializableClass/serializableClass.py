# Class for ease procedure of saving and loading of classes hierarchy

# each inherited class should not implement __init__ function
# and should implement saveThisObjectDataOnly_ and loadThisObjectDataOnly_ functions which have to just install values of 
# current class, not it's parent classes values (only if necessary)

# Also each class should have string: "ClassName.registerClass()" at the end of file (without indent)

import os

from .getInheritenceSequence import getInheritenceSequence
from .makeDirectoryIfNotExist import makeDirectoryIfNotExist

class SerializableClass:
    @classmethod
    def initNewRootOfInheritance(cls):
        cls.registeredDescendants_ = {}
    
    @classmethod
    def registerClass(cls, className=""):
        if className == "":
            className = getInheritenceSequence(cls)
        if className in cls.registeredDescendants_:
            raise Exception("Attempt to replace object with name " + className)
            #print("Class " + className + " has been replaced!")
        cls.registeredDescendants_[className] = cls
        cls.registrationFullName_ = className
        return className
    
# SAVE AND LOAD:

    def save(self, folder):
        self.save_(folder, set())
    
    def save_(self, folder, alreadySavedClasses=set()):
        if type(self) in alreadySavedClasses:
            return
        makeDirectoryIfNotExist(folder)
        self.saveThisObjectDataOnly_(folder)
        alreadySavedClasses.add(type(self))
        with open(os.path.join(folder, "className.txt"), "w") as fp:
            fp.write(self.getRegistrationFullName())
        superClasses = type(self).__bases__
        originalClass = self.__class__
        for superClass in superClasses:
            self.__class__ = superClass
            if hasattr(superClass, "save") == True and self.getRegistrationFullName() is not None:
                superClassFolder = os.path.join(folder, self.getRegistrationFullName())
                self.save_(superClassFolder, alreadySavedClasses)
        self.__class__ = originalClass
        
    def saveThisObjectDataOnly_(self, folder):
        pass
        
    @classmethod
    def load(cls, folder):
        with open(os.path.join(folder, "className.txt"), "r") as fp:
            className = fp.read()
            classType = cls.registeredDescendants_[className]
            res = classType()
            res.load_(folder)
            res.loadThisObjectDataOnly_(folder)
            return res
        raise Exception("Can't open " + os.path.join(folder, "className.txt") + "!")
        
    def load_(self, folder):
        superClasses = type(self).__bases__
        originalClass = self.__class__
        for superClass in superClasses:
            self.__class__ = superClass
            if hasattr(superClass, "load_") == True and self.getRegistrationFullName() is not None:
                superClassFolder = os.path.join(folder, self.getRegistrationFullName())
                if os.path.isdir(superClassFolder) == False:
                    continue
                self.load_(superClassFolder)
                self.loadThisObjectDataOnly_(folder)
        self.__class__ = originalClass
    
    def loadThisObjectDataOnly_(self, folder):
        pass
        
# SETTERS AND GETTERS:
        
    @classmethod
    def getRegisteredDescendants(cls):
        return cls.registeredDescendants_
    
    def getRegistrationFullName(self):
        return self.registrationFullName_
    
# FIELDS:
    
    registeredDescendants_ = None
    registrationFullName_ = None
    
    