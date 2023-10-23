class Node():
    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []

    def Birth(self, obj, other_parent):
        obj.parents = [self,other_parent]
        self.children.append(obj)
        other_parent.children.append(obj)
        
    def DisplayDescendants(self, depth = 0):
        if depth == 0: print("\n--------------------")
        box = ""
        for i in range(depth):
            box = box + "   "
        print(f"{box}{self.name}")
        for c in self.children:
            c.displayDescendants(depth + 1)

    def Dive(self):


    def GetOldestDescendants(self):
        if self.parents == []: return [self]
        if len(self.children) == 1 and self.parents == []: return [self.children[0]]



        if self.parents == []: 
            if len(self.children) == 1:
                return [True,self]
            else: return [self]
        else: 
            descendants = []
            ReachedEnd = True
            for parent in self.parents:
                TheseDescendants = parent.GetOldestDescendants()

                if TheseDescendants[0] != True: 
                    ReachedEnd = False
                    descendants.extend(TheseDescendants)
                

            #if ReachedEnd: descendants = [True,descendants.pop()]

            return descendants

esther = Node("Esther")
erik = Node("Erik")
erika = Node("Erika")

emil = Node("Emil")
esther.Birth(emil,erik)
ellen = Node("Ellen")
#erika.Birth(ellen,erik)

print(emil.GetOldestDescendants())