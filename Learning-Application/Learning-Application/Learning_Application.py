import random as r
import tkinter as tk
import math as m

# A class for making a simple clamped value
class clamped_value:
    def __init__(self, min, max, initial_value=1):
        self.min = min
        self.max = max
        self._value = initial_value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = max(self.min, min(new_value, self.max))
        print(f"User Score: {self._value}")

# The brain of the program! It's a class for storing simple equations.
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

    
    # ToString() and Calculate() are cuite simmilar. They are both recursive functions, which dive into all of the children first and process them, then they work to the top and get an output.

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
            
            if self.parent != None:
                return f"({answer})"
            else:
                return f"{answer}"

        # Case "-"
        elif operation == "-":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" - {self.children[i+1].ToString()}"
            
            if self.parent != None:
                return f"({answer})"
            else:
                return f"{answer}"

        # Case "*"
        elif operation == "*":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" · {self.children[i+1].ToString()}"
            
            if self.parent != None:
                return f"({answer})"
            else:
                return f"{answer}"

        # Case "/"
        elif operation == "/":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" / {self.children[i+1].ToString()}"
            
            if self.parent != None:
                return f"({answer})"
            else:
                return f"{answer}"

        # Case "^"
        elif operation == "^":
            answer = self.children[0].ToString()
            for i in range(len(self.children)-1):
                answer += f" ^{self.children[i+1].ToString()}"
            
            if self.parent != None:
                return f"({answer})"
            else:
                return f"{answer}"

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

            if self.parent != None:
                return f"({prefix}{middle}{suffix})"
            else:
                return f"{prefix}{middle}{suffix}"

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
            answer = self.children[0].Calculate()
            for i in range(len(self.children)-1):
                answer -= self.children[i+1].Calculate()
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


# Using the Builder pattern to manually write in a lot of equations the user can try to solve.
# This would have been a lot harder, if I had to do this without the Builder Pattern. Bruh, imagine that hell...
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

second_dict = {
    1: Equation("+").Add(2).Add(7).Add("-").Add(5).Add(1).parent,   
    2: Equation("+").Add(3).Add(4).Add("-").Add(2).Add(1).parent,   
    3: Equation("-").Add(10).Add(2).Add("+").Add(1).Add(1).parent,  
    4: Equation("+").Add(5).Add(5).Add("-").Add(3).Add(2).parent,   
    5: Equation("-").Add(9).Add(4).Add("+").Add(2).Add(2).parent,   
    6: Equation("+").Add(1).Add(8).Add("-").Add(4).Add(1).parent,   
    7: Equation("-").Add(7).Add(3).Add("+").Add(5).Add(4).parent,   
    8: Equation("+").Add(2).Add(6).Add("-").Add(3).Add(1).parent,   
    9: Equation("-").Add(11).Add(5).Add("+").Add(3).Add(3).parent,  
    10: Equation("+").Add(4).Add(4).Add("-").Add(2).Add(2).parent,  
    11: Equation("-").Add(8).Add(2).Add("+").Add(1).Add(4).parent,  
    12: Equation("+").Add(3).Add(7).Add("-").Add(5).Add(3).parent,  
    13: Equation("-").Add(6).Add(1).Add("+").Add(2).Add(2).parent,  
    14: Equation("+").Add(5).Add(5).Add("-").Add(6).Add(1).parent,  
    15: Equation("-").Add(9).Add(3).Add("+").Add(4).Add(2).parent   
}

third_dict = {
    1: Equation("/").Add(10).Add(2),     
    2: Equation("*").Add(4).Add(4),      
    3: Equation("/").Add(12).Add(3),     
    4: Equation("*").Add(7).Add(3),      
    5: Equation("/").Add(15).Add(5),     
    6: Equation("*").Add(5).Add(2),      
    7: Equation("/").Add(20).Add(4),     
    8: Equation("*").Add(6).Add(6),      
    9: Equation("/").Add(16).Add(2),     
    10: Equation("*").Add(8).Add(9),     
    11: Equation("/").Add(18).Add(3),    
    12: Equation("*").Add(3).Add(4),     
    13: Equation("/").Add(21).Add(7),    
    14: Equation("*").Add(2).Add(5),     
    15: Equation("/").Add(24).Add(6)     
}

fourth_dict = {
    1: Equation("+").Add("/").Add(10).Add(2).parent.Add("*").Add(4).Add(2).parent, 
    2: Equation("-").Add("*").Add(8).Add(3).parent.Add("/").Add(6).Add(2).parent,  
    3: Equation("/").Add("-").Add(15).Add("*").Add(5).Add(2).parent.Add(5).parent, 
    4: Equation("+").Add("*").Add("/").Add(12).Add(3).parent.Add(2).parent.Add(4), 
    5: Equation("-").Add("/").Add(18).Add(2).parent.Add("+").Add(3).Add(2).parent, 
    6: Equation("/").Add("-").Add("*").Add(6).Add(2).parent.Add(4).parent.Add(2),  
    7: Equation("+").Add("/").Add(20).Add(4).parent.Add("*").Add(3).Add(5).parent, 
    8: Equation("-").Add("*").Add(7).Add(3).parent.Add("/").Add(8).Add(2).parent,  
    9: Equation("*").Add("/").Add(14).Add(2).parent.Add("-").Add(5).Add(3).parent, 
    10: Equation("*").Add("+").Add(9).Add("/").Add(15).Add(3).parent.parent.Add(2),
    11: Equation("/").Add("-").Add("*").Add(8).Add(4).parent.Add(10).parent.Add(2),
    12: Equation("+").Add("*").Add(6).Add("/").Add(12).Add(4).parent.parent.Add(3),
    13: Equation("/").Add("*").Add("+").Add(10).Add(5).parent.Add(2).parent.Add(5),
    14: Equation("*").Add("-").Add(7).Add("/").Add(14).Add(7).parent.Add(4).parent,
    15: Equation("*").Add("+").Add("/").Add(20).Add(5).parent.Add(7).parent.Add(2) 
}

# Used for debugging:
def print_all_answers():
    # Output:
    #  2 + 2 = 4.0
    #  5 + 7 = 12.0
    #  8 - 3 = 5.0
    #  1 + 4 = 5.0
    #  6 - 2 = 4.0
    #  3 + 3 = 6.0
    #  9 - 4 = 5.0
    #  2 + 6 = 8.0
    #  7 - 1 = 6.0
    #  4 + 5 = 9.0
    #  10 - 3 = 7.0
    #  1 + 9 = 10.0
    #  5 - 2 = 3.0
    #  6 + 1 = 7.0
    #  8 - 5 = 3.0
    #  2 + 7 + (5 - 1) = 13.0
    #  3 + 4 + (2 - 1) = 8.0
    #  10 - 2 - (1 + 1) = 6.0
    #  5 + 5 + (3 - 2) = 11.0
    #  9 - 4 - (2 + 2) = 1.0
    #  1 + 8 + (4 - 1) = 12.0
    #  7 - 3 - (5 + 4) = -5.0
    #  2 + 6 + (3 - 1) = 10.0
    #  11 - 5 - (3 + 3) = 0.0
    #  4 + 4 + (2 - 2) = 8.0
    #  8 - 2 - (1 + 4) = 1.0
    #  3 + 7 + (5 - 3) = 12.0
    #  6 - 1 - (2 + 2) = 1.0
    #  5 + 5 + (6 - 1) = 15.0
    #  9 - 3 - (4 + 2) = 0.0
    #  10 / 2 = 5.0
    #  4 · 4 = 16.0
    #  12 / 3 = 4.0
    #  7 · 3 = 21.0
    #  15 / 5 = 3.0
    #  5 · 2 = 10.0
    #  20 / 4 = 5.0
    #  6 · 6 = 36.0
    #  16 / 2 = 8.0
    #  8 · 9 = 72.0
    #  18 / 3 = 6.0
    #  3 · 4 = 12.0
    #  21 / 7 = 3.0
    #  2 · 5 = 10.0
    #  24 / 6 = 4.0
    #  (10 / 2) + (4 · 2) = 13.0
    #  (8 · 3) - (6 / 2) = 21.0
    #  (15 - (5 · 2) - 5) = 0.0
    #  ((12 / 3) · 2) + 4 = 12.0
    #  (18 / 2) - (3 + 2) = 4.0
    #  ((6 · 2) - 4) / 2 = 4.0
    #  (20 / 4) + (3 · 5) = 20.0
    #  (7 · 3) - (8 / 2) = 17.0
    #  (14 / 2) · (5 - 3) = 14.0
    #  (9 + (15 / 3)) · 2 = 28.0
    #  ((8 · 4) - 10) / 2 = 11.0
    #  (6 · (12 / 4)) + 3 = 21.0
    #  ((10 + 5) · 2) / 5 = 6.0
    #  (7 - (14 / 7) - 4) = 1.0
    #  ((20 / 5) + 7) · 2 = 22.0

    # For first_dict
    for key in first_dict:
        print(first_dict[key].ToString() + " = " + str(first_dict[key].Calculate()))
    
    # For second_dict
    for key in second_dict:
        print(second_dict[key].ToString() + " = " + str(second_dict[key].Calculate()))
    
    # For third_dict
    for key in third_dict:
        print(third_dict[key].ToString() + " = " + str(third_dict[key].Calculate()))
    
    # For fourth_dict
    for key in fourth_dict:
        print(fourth_dict[key].ToString() + " = " + str(fourth_dict[key].Calculate()))


# The program gives to problems according to how you are doing on the other problems.
def generate_math_problem(difficulty,current_equation = Equation(0)):
    if m.floor(difficulty) == 1:
        equation = first_dict[r.randint(1, len(first_dict))]
    elif m.floor(difficulty) == 2:
        equation = second_dict[r.randint(1, len(second_dict))]
    elif m.floor(difficulty) == 3:
        equation = third_dict[r.randint(1, len(third_dict))]
    elif m.floor(difficulty) == 4:
        equation = fourth_dict[r.randint(1, len(fourth_dict))]
    else:
        equation = first_dict[1]

    # Making sure, that the new equation isn't the same as the old one. If it is, use recursion to fix it.
    if equation.ToString() == current_equation.ToString():
        return generate_math_problem(score.value,current_equation)

    print("\nNew Equation: " + equation.ToString()  + " = " + str(equation.Calculate()))
    return equation

score = clamped_value(1,4)
current_equation = generate_math_problem(score.value)

# Submit Answer is called when pressing the Submit button in TKinter.
def submit_answer():
    global current_equation
    user_answer = answer_entry.get()

    print(f"User Answer: {user_answer}")
    print(f"Correct Answer: {current_equation.Calculate()}")
    
    # Making sure that the user inputted a float
    try:
        float_value = float(user_answer)
    except ValueError:
        # The conversion failed
        print(f"\"{user_answer}\" cannot be converted to a float")
        result_text.config(text="Not correct :C")
        answer_entry.delete(0, tk.END)
        return

    # Correct Answer!
    if float(user_answer) == current_equation.Calculate():
        result_text.config(text="Correct!")
        answer_entry.delete(0, tk.END)
        score.value += 0.3
        current_equation = generate_math_problem(score.value,current_equation)
        update_equation(current_equation)
    
    # WRONG!
    else:
        result_text.config(text="Not correct :C")
        answer_entry.delete(0, tk.END)
        score.value -= 0.1
        current_equation = generate_math_problem(score.value,current_equation)
        update_equation(current_equation)

def update_equation(new_equation):
    equation_label.config(text=new_equation.ToString())




root = tk.Tk()
root.title("Math Application")

# Set a fixed size to resemble a phone screen
root.geometry("360x640")

# Use frames to organize the layout
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

middle_frame = tk.Frame(root)
middle_frame.pack(pady=10)

bottom_frame = tk.Frame(root)
bottom_frame.pack(pady=10)

# Increase font size for mobile-like appearance
large_font = ('Verdana', 18)

# Equation label
equation_label = tk.Label(top_frame, text=current_equation.ToString(), font=large_font)
equation_label.pack()

# Answer entry
answer_entry = tk.Entry(middle_frame, font=large_font)
answer_entry.pack(pady=10, padx=20, fill='x')  # Fill in x direction

# Submit button
submit_button = tk.Button(bottom_frame, text="Submit", font=large_font, command=lambda: submit_answer())
submit_button.pack(pady=10, fill='x')

# Result text
result_text = tk.Label(bottom_frame, text="", font=large_font)
result_text.pack(pady=10)

root.mainloop()