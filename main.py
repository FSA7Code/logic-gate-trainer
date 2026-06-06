import random
import sys

# --- THE LOGIC GATES ---

def and_gate(input1, input2):
    if input1 == 1 and input2 == 1:
        return 1
    else:
        return 0

def or_gate(input1, input2):
    if input1 == 1 or input2 == 1:
        return 1
    else:
        return 0

def not_gate(input_value):
    if input_value == 1:
        return 0
    else:
        return 1

# --- THE GAME ENGINE ---

# We create variables to hold your score outside the round
score = 0
total_questions = 0

def play_round():
    global score, total_questions  # This lets the function update the score numbers
    
    gate_type = random.choice(["AND", "OR", "NOT"])
    in1 = random.randint(0, 1)
    in2 = random.randint(0, 1)

    if gate_type == "AND":
        correct_answer = and_gate(in1, in2)
        question = f"What is the output of an {gate_type} gate if the inputs are {in1} and {in2}? "
    elif gate_type == "OR":
        correct_answer = or_gate(in1, in2)
        question = f"What is the output of an {gate_type} gate if the inputs are {in1} and {in2}? "
    else:
        correct_answer = not_gate(in1)
        question = f"What is the output of a {gate_type} gate if the input is {in1}? "

    print("\n--- NEW QUESTION ---")
    user_guess = input(question).strip().lower() # Converts to lowercase and removes spaces
    
    # FIX: Check if the user wants to exit first!
    if user_guess == "exit":
        print("\n--- GAME OVER ---")
        print(f"Final Score: {score}/{total_questions}")
        print("Thanks for playing the Logic Gate Trainer!")
        sys.exit() # This closes the program cleanly without a crash error

    # Safe to check the answer now because it isn't "exit"
    try:
        if int(user_guess) == correct_answer:
            print("Correct! Excellent job.")
            score += 1
        else:
            print(f"Wrong. The correct answer was {correct_answer}.")
        
        total_questions += 1
        print(f"Current Score: {score}/{total_questions}")
        
    except ValueError:
        print("Invalid input! Please type 0, 1, or 'exit'.")

# --- RUN THE GAME ---
if __name__ == "__main__":
    print("Welcome to the ECE Logic Gate Trainer!")
    print("Type 'exit' at any time to quit the game.\n")
    
    while True:
        play_round()