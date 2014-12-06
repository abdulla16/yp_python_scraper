class Business:
    
    def __init__(self):
        self.__branches = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter 
    def name(self, name): 
        self.__name = name
    
    @property
    def branches(self):
        return self.__branches
    
    def addBranch(self, branch):
        self.__branches.append(branch)
