import random

# Define a list of responses for each command
responses = {
    "hello world": ["Hello!", "Hi there!", "How can I assist you today?"],
    "good morning": ["Good morning!", "Morning!", "How can I help you this morning?"],
    "what is your favourite number?": [f"My favourite number is {random.randint(0, 10)}"],
    "distrack": ['''Spiller for meget
Knepper for lidt 
Køber sin titel
This Lord is a shit 


Spiller for meget
knepper for lidt 
Skinny jeans all the way
Stilen er mid
Polo på kroppen 
Og krav' har den krøl'
Curlyboi flexer 
Men chopper den søl'
No rizz, no style and no skills and behold 
Curly boi dør just all old and alone 
Piller ved titties 
Forstår ik consent
Ind bag de bars 
Cause this man is no gent 


Spiller for meget 
Knepper for lidt 
Mangler den skejs 
For han ejer den ik
Addicted til gaming 
Han ser kun på skærm'
Social skills døde 
Og verden er fjern 
Minecraft og mindustry, muck og Celeste 
Spiller kun pik for pik spiller han bedst
Eneste rizz er den app han er done
Albert han taber for Trine har won''']
}

# Function to generate a response based on the command
def get_response(command):
    if command in responses:
        return random.choice(responses[command])
    else:
        return "I'm sorry, I don't understand that command."

# Main loop to interact with the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input.lower())
    print("Chatbot:", response)
