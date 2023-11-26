import random
#import PySimpleGUI as sg
#
# Define the layout for the app
#
#layout = [
#    [sg.Text("Phone App Look Alike", size=(20, 1), justification='center', font=("Arial", 20, "bold"))],
#    [sg.Text("Enter Your Name:"), sg.InputText(key='-NAME-')],
#    [sg.Text("Enter Your Number:"), sg.InputText(key='-NUMBER-')],
#    [sg.Button('Submit'), sg.Button('Exit')]
#]
#
#layout = [
#    [sg.Text("MatematikAppen", size=(20, 1), justification='center', font=("Arial", 20, "bold"))],
#    ]
#
## Create the window
#window = sg.Window('Phone App', layout, size=(108*3, 192*3))


class Equation:
    def __init__(self, operation = "", value = ""):
        self.operation = operation
        self.children = []
        self.value = value

    def Add(self, operation = "", value = ""):
        if isinstance(operation, (float, int)):
            self.AddNum(operation)
            return
        self.children.append(Equation(operation,value))

    def AddNum(self, num):
        self.children.append(Equation("",str(num)))

    def ToString(self):

        operation = self.operation
        # Case ""
        if operation == "":
            return self.value
        
        # Case "+"
        elif operation == "+":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" + {self.children[i+1].ToString()}"
            return f"({answer})"

        # Case "-"
        elif operation == "-":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" - {self.children[i+1].ToString()}"
            return f"({answer})"

        # Case "*"
        elif operation == "*":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" · {self.children[i+1].ToString()}"
            return f"({answer})"

        # Case "/"
        elif operation == "/":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" / {self.children[i+1].ToString()}"
            return f"({answer})"

        # Case "^"
        elif operation == "^":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" ^{self.children[i+1].ToString()}"
            return f"({answer})"

        # Case "nrt"
        elif operation == "nrt":
            
            answer = self.children[0].ToString()
            length = len(self.children)

            # Prefix
            prefix = ""
            for i in range(length-1):
                prefix += f"root\"{self.children[length-1-i].ToString()}\"("

            # Middle
            middle = self.children[0].ToString()

            # Suffix
            suffix = ")" * (length-1)

            return f"({prefix}{middle}{suffix})"

        else: return ""

    def Calculate(self):
        operation = self.operation
        
        # Case ""
        if operation == "":
            try:
                return float(self.value)
            except:
                return 0
        
        # Case "+"
        elif operation == "+":
            answer = 0
            for child in self.children:
                answer += child.Calculate()
            return answer

        # Case "-"
        elif operation == "-":
            answer = 0
            for child in self.children:
                answer -= child.Calculate()
            return answer

        # Case "*"
        elif operation == "*":
            answer = 1
            for child in self.children:
                answer *= child.Calculate()
            return answer

        # Case "/"
        elif operation == "/":
            answer = self.children[0].Calculate()
            for i in range(len(self.children)-1):
                answer /= self.children[i+1].Calculate()
            return answer

        # Case "^"
        elif operation == "^":
            answer = self.children[0].Calculate()
            for i in range(len(self.children)-1):
                answer = answer ** self.children[i+1].Calculate()
            return answer

        # Case "nrt"
        elif operation == "nrt":
            answer = self.children[0].Calculate()
            for i in range(len(self.children)-1):
                answer = answer ** 1/self.children[i+1].Calculate()
            return answer

        else: return 0


equation = Equation("*")

equation.Add("+")
equation.children[0].Add(5)
equation.children[0].Add(7)

equation.Add(2)
equation.Add(3)


print(equation.ToString())
print(equation.Calculate())

#def GenerateMathProblem(difficulty):
#    if (difficulty < 0): difficulty = 0
#    elif (difficulty > 4): difficulty = 4
#
#    operators = ["+","-"]
#    if difficulty == 4:
#        operators.append("*")
#        operators.append("/")
#
#    operator = random.choice(operators)
#    equation = Equation(operator)


    




# Event loop
#while True:
#    event, values = window.read()
#
#    if event == sg.WINDOW_CLOSED or event == 'Exit':
#        break
#    if event == 'Submit':
#        sg.popup(f"Name: {values['-NAME-']}\nNumber: {values['-NUMBER-']}")
#
#window.close()