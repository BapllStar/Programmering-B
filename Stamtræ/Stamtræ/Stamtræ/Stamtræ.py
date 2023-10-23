def are_related(pers1,pers2):
    value = pers1.getOldestDescendant() == pers2.getOldestDescendant()
    print(f"{pers1.name} og {pers2.name}")
    print(f"({value})\n")     

class Node(object):
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.children = []

    def addChild(self, obj):
        self.children.append(obj)
        obj.parent = self

    def displayDescendants(self, depth = 0):
        if depth == 0: print("\n--------------------")
        box = ""
        for i in range(depth):
            box = box + "   "
        print(f"{box}{self.name}")
        for c in self.children:
            c.displayDescendants(depth + 1)

    def getOldestDescendant(self):
        if self.parent == None: return self
        else: return self.parent.getOldestDescendant()


# family 1
esther = Node("Esther")

elias = Node("Elias")
esther.addChild(elias)
emil = Node("Emil")
esther.addChild(emil)
eva = Node("Eva")
esther.addChild(eva)

ellen = Node("Ellen")
eva.addChild(ellen)
erik = Node("Erik")
emil.addChild(erik)
elvira = Node("Elvira")
emil.addChild(elvira)

edith = Node("Edith")
ellen.addChild(edith)
elmer = Node("Elmer")
ellen.addChild(elmer)
elsa = Node("Elsa")
erik.addChild(elsa)

esther.displayDescendants()

# family 2

anna = Node("Anna")

anders = Node("Anders")
anna.addChild(anders)
astrid = Node("Astrid")
anna.addChild(astrid)
alfred = Node("Alfred")
anna.addChild(alfred)

alma = Node("Alma")
alfred.addChild(alma)
anton = Node("Anton")
astrid.addChild(anton)
agnes = Node("Agnes")
astrid.addChild(agnes)

albert = Node("Albert")
alma.addChild(albert)
amalie = Node("Amalie")
alma.addChild(amalie)
arthur = Node("Arthur")
anton.addChild(arthur)

anna.displayDescendants()

# Family 3

diana = Node("Diana")

daniel = Node("Daniel")
diana.addChild(daniel)
david = Node("David")
diana.addChild(david)
daisy = Node("Daisy")
diana.addChild(daisy)

dexter = Node("Dexter")
daniel.addChild(dexter)
daphne = Node("Daphne")
daniel.addChild(daphne)

deborah = Node("Deborah")
david.addChild(deborah)
dennis = Node("Dennis")
david.addChild(dennis)

dominic = Node("Dominic")
daisy.addChild(dominic)
dana = Node("Dana")
daisy.addChild(dana)

damien = Node("Damien")
dexter.addChild(damien)

dora = Node("Dora")
deborah.addChild(dora)

derek = Node("Derek")
dominic.addChild(derek)

dylan = Node("Dylan")
dana.addChild(dylan)

desiree = Node("Desiree")
damien.addChild(desiree)

diana.displayDescendants()



# Checking
are_related(erik, alfred)
are_related(anna, anders)
are_related(daisy, ellen)
are_related(anton, elias)
are_related(diana, dennis)
are_related(dominic, elsa)
are_related(esther, eva)
are_related(agnes, daphne)
are_related(dylan, emil)
are_related(elvira, amalie)