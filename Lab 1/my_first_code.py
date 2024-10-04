import random
print("My first line of code")
'''
print("Dear python, I know how display text",
      "\nHello",end = "")
print(" World!")
print("Hello" , "World!")

name = "Alex"
age = 20
print(f"{name} is {age} years old")
print(name , "is" , age , "years old")
print("{name} is {age} years old")

name = "Alice"
print("Hello " + name)
print("{} is {} years old".format("Alice",30))

'''
'''
print(365+456)
print(3+3)
print(3*3)
print(3-3)
print(9/3)
print(9//3)
print(50%100)
print(2**10)
'''

'''
current_year = 2024
age = 20
date_of_birth = current_year - age
print("Date of Birth =" , date_of_birth)
print(type(date_of_birth))
'''
'''
# List of random responses to be given after each answerresponses = ["Cool!","Nice!","Wow, great!"]
responses = ["Wow, great!",
             "Nice!",
             "cool!"
            ]

questions = ["What is your name?",
            "What is your favourite movie",
            "What is your favourite meal"
           ]
# Function to ask a question and provide a random 
def ask_question(question):
    answer = input(question + " ")
    print(random.choice(responses))
    print() 

# For spacing between questions# List of questions to be filled in by studentsquestions = ["What's your favoritehobby?",    

# Example question"What's your favoritemovie?",  ]
# Function to randomly select and ask two questionsdef 
def icebreaker():
    print("Let's break the ice! I'll ask you two random questions:")
    selected_questions= random.sample(questions, 3)  
# Randomly select 2 questionsfor question in 
    for question in selected_questions:
     ask_question(question)
# Call the icebreaker function to start the programicebreaker()
icebreaker()
'''

git init 
git status