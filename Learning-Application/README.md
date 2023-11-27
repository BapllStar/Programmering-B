# Learning Application
I dette dokument, kan du læse om [mit projekt](https://github.com/BapllStar/Programmering-B/tree/main/Learning-Application).
## Programmets formål
Jeg vil udvikle en app, der træner dens brugere i hovedregning. Dette gøres ved at holde en score for, hvor godt brugeren klarer sig, og give opgaver, der svarer til nivauet. 
Selv projektet kan du finde [her](https://github.com/BapllStar/Programmering-B/tree/main/Learning-Application).
## Målgruppen
Målgruppen er hovedsagligt elever i starten af udskolingen, men da programmet tilpasser sig en sværhedsgrad til den individuelle bruger, bør man teknisk set godt kunne bruge de, så længe man kan addere og subtrahere.
## Design Pattern -- Builder
Builder Pattern er et meget simpelt designmønster, der går ud på at bygge klasser ved hjælp af specifikke metoder der returnerer sig selv, så man kan kæde metoderne sammen, hvilket giver mere overskuelighed.
### Eksempel på Builder Pattern
```python
class Hotdog():
	def __innit__(self):
		self.bread = ""
		self.sausage = ""

	def add_wheat_bread():
		self.bread = "Wheat"
		return self
		# Metoden returnerer sig selv, så man kan kæde
		# flere af disse buildermetoder sammen på samme
		# linje.

	def add_frankfurter():
		self.sausage = "Frankfurter"
		return self
```
```python
my_hotdog = Hotdog()
my_hotdog.add_what_bread().add_frankfurter()
# Her kædes de to buildermetoder sammen.
```
---
Hvis disse metoder ikke returnerede `self`, ville man være nødt til at splitte samme funktionalitet over flere linjer:
```python
my_hotdog = Hotdog()
my_hotdog.add_wheat_bread()
my_hotdog.add_frankfurter()
```
Lige specifikt i dette tilfælde er det ikke så slemt, men med flere variabler, kan de gå hen og dække over ret mange linjer.
### Uden Builder Pattern
```python
skole = Skole()

klasse_a = Klasse()

klasse_a.add("Laura")
klasse_a.add("Lucas")
klasse_a.add("Matthias")
klasse_a.add("Marcus")

klasse_b = Klasse()

klasse_b.add("William")
klasse_b.add("David")
klasse_b.add("Asta")
klasse_b.add("Sofie")
klasse_b.add("Albert")
klasse_b.add("Karla")

skole.klasser.append(klasse_a)
skole.klasser.append(klasse_b)
```
### Med Builder Pattern
```python
skole = Skole()
skole.klasser.append(Klasse().add("Laura").add("Lucas").add("Matthias").add("Marcus"))
skole.klasser.append(Klasse().add("William").add("David").add("Asta").add("Sofie").add("Albert").add("Karla"))
```

## Integrering af Builder Pattern i Appen
Her er et udklip af en klasse fra mit program, der bruger Builder Pattern:
```python
class Equation:
    def __init__(self, operation = "", value = "", parent = None):
        self.operation = operation
        self.children = []
        self.value = value
        self.parent = parent

    # The method for adding a sub equation the the equation.
    def Add(self, operation = "", value = ""):
        
        # If the new equation is a lone number, use the AddNum Method for adding a number equation.
        if isinstance(operation, (float, int)):
            self.AddNum(operation)

            # The Builder pattern returns self so I can chain methods:
            return self
        
        # Else, just at the info from the constructor to children as a sub equation.
        self.children.append(Equation(operation,value,self))

        # This isn't classical Builder Pattern, since I'm diving a level. Here, I just added a shortcut to make things easier here in building.
        return self.children[len(self.children)-1]

    def AddNum(self, num):
        self.children.append(Equation("",str(num),self))

        # The Builder pattern returns self so I can chain methods:
        return self

	# Mere kode...
```

Og her vises den udnyttet i programmet:
```python
first_dict = {
    1: Equation("+").Add(2).Add(2),    
    2: Equation("+").Add(5).Add(7),    
    3: Equation("-").Add(8).Add(3),    
    4: Equation("+").Add(1).Add(4),    
    5: Equation("-").Add(6).Add(2),    
    6: Equation("+").Add(3).Add(3),    
    7: Equation("-").Add(9).Add(4),    
    8: Equation("+").Add(2).Add(6),    
    9: Equation("-").Add(7).Add(1),    
    10: Equation("+").Add(4).Add(5),   
    11: Equation("-").Add(10).Add(3),  
    12: Equation("+").Add(1).Add(9),   
    13: Equation("-").Add(5).Add(2),   
    14: Equation("+").Add(6).Add(1),   
    15: Equation("-").Add(8).Add(5)    
}
```

Min klasse kan også vises ved hjælp af et klassediagram:
```mermaid
classDiagram
    class Equation {
        -operation: string
        -children: list<Equation>
        -value: string
        -parent: Equation
        +__init__(operation, value, parent)
        +Add(operation, value)
        +AddNum(num)
        +ToString()
        +Calculate()
    }
	class MultiplicationEquation{
		-operation: "*"
        -children: list<Equation>
        -value: string
        -parent: None
        +__init__(operation, value, parent)
        +Add(operation, value)
        +AddNum(num)
        +ToString()
        +Calculate()
	}
	MultiplicationEquation --> Equation
	note right for Equation "test"
```
## Udviklingsprocessen
Jeg startede med at researche omkring forskellige design patterns, men valgte ikke et før, jeg vidste, hvad jeg ville arbejde med.
Efter at have fundet ud af det, brugte jeg mit design pattern til at skrive en masse regnestykker, som brugerne kan løse. Dette har jeg brugt Builder Pattern til.

## Brugergrænsefladen
Brugergrænsefladen er meget simpel, da jeg hovedsageligt fokuserede på at lave noget udfordrende. Da jeg godt ved, hvordan man bruger Tkinter i forvejen, kunne jeg godt holde lidt tilbage med det.

### Brugergrænsefladen har blot 4 elementer
1. **Equation Label:** Her bliver regnestykkerne vist for brugerne.
2. **Input Field:** Her kan brugeren skrive sit svar ind.
3. **Submit Button:** Brugeren kan trykke på denne for at få sit svar valideret.
4. **Result Text:** Denne tekst giver resultatet for brugerens svar.


## Test af programmet
|Hvad Testes?|Forventet Resultat|Faktisk Resultat|
|--|--|--|
|Input af korrekt svar|"Correct!"|"Correct!"|
|Input af forkert svar|"Not Correct :C"|"Not Correct :C"|
|Input af intet svar|"Not Correct :C"|"Not Correct :C"|
|Input af bogstaver|"Not Correct :C"|"Not Correct :C"|
|Spamming "Submit"|"Not Correct :C"|"Not Correct :C"|


