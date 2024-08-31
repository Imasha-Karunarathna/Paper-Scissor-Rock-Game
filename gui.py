import tkinter as tk
import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to animate the result
def animate_result(result):
    if result == "You win!":
        result_label.config(text="🎉 You Win! 🎉", fg="lightgreen")
        animate_win()
    elif result == "You lose!":
        result_label.config(text="💥 You Lose! 💥", fg="red")
        animate_loss()
    else:
        result_label.config(text="It's a tie!", fg="white")

# Animation for win
def animate_win():
    for _ in range(3):
        result_label.config(bg="green")
        window.update()
        window.after(200)
        result_label.config(bg="darkblue")
        window.update()
        window.after(200)

# Animation for loss
def animate_loss():
    for _ in range(3):
        result_label.config(bg="darkred")
        window.update()
        window.after(200)
        result_label.config(bg="darkblue")
        window.update()
        window.after(200)

# Function to handle the user's choice
def make_choice(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    update_labels(choice, computer_choice, result)
    
    # Update scores
    if result == "You win!":
        global user_score
        user_score += 1
    elif result == "You lose!":
        global computer_score
        computer_score += 1
    
    # Update score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

# Function to update the result and choices display
def update_labels(user_choice, computer_choice, result):
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    animate_result(result)

# Initialize the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x400")
window.configure(bg="darkblue")

# Configure grid layout to center content
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_rowconfigure(7, weight=1)

window.grid_columnconfigure(0, weight=1)

# Initialize scores
user_score = 0
computer_score = 0

# Create and place the widgets in the center
title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"), bg="darkblue", fg="white")
title_label.grid(row=0, column=0, pady=10)

button_rock = tk.Button(window, text="Rock", command=lambda: make_choice("rock"), width=10, bg="midnightblue", fg="white")
button_rock.grid(row=1, column=0, pady=5)

button_paper = tk.Button(window, text="Paper", command=lambda: make_choice("paper"), width=10, bg="midnightblue", fg="white")
button_paper.grid(row=2, column=0, pady=5)

button_scissors = tk.Button(window, text="Scissors", command=lambda: make_choice("scissors"), width=10, bg="midnightblue", fg="white")
button_scissors.grid(row=3, column=0, pady=5)

user_choice_label = tk.Label(window, text="", font=("Arial", 12), bg="darkblue", fg="white")
user_choice_label.grid(row=4, column=0, pady=5)

computer_choice_label = tk.Label(window, text="", font=("Arial", 12), bg="darkblue", fg="white")
computer_choice_label.grid(row=5, column=0, pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14), bg="darkblue", fg="white", wraplength=300)
result_label.grid(row=6, column=0, pady=10)

score_frame = tk.Frame(window, bg="darkblue")
score_frame.grid(row=7, column=0, pady=5)

user_score_label = tk.Label(score_frame, text="Your Score: 0", font=("Arial", 12), bg="darkblue", fg="white")
user_score_label.pack(side=tk.LEFT, padx=20)

computer_score_label = tk.Label(score_frame, text="Computer's Score: 0", font=("Arial", 12), bg="darkblue", fg="white")
computer_score_label.pack(side=tk.RIGHT, padx=20)

# Run the application
window.mainloop()
import tkinter as tk
import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to animate the result
def animate_result(result):
    if result == "You win!":
        result_label.config(text="🎉 You Win! 🎉", fg="lightgreen")
        animate_win()
    elif result == "You lose!":
        result_label.config(text="💥 You Lose! 💥", fg="red")
        animate_loss()
    else:
        result_label.config(text="It's a tie!", fg="white")

# Animation for win
def animate_win():
    for _ in range(3):
        result_label.config(bg="green")
        window.update()
        window.after(200)
        result_label.config(bg="darkblue")
        window.update()
        window.after(200)

# Animation for loss
def animate_loss():
    for _ in range(3):
        result_label.config(bg="darkred")
        window.update()
        window.after(200)
        result_label.config(bg="darkblue")
        window.update()
        window.after(200)

# Function to handle the user's choice
def make_choice(choice):
    computer_choice = get_computer_choice()
    result = determine_winner(choice, computer_choice)
    update_labels(choice, computer_choice, result)
    
    # Update scores
    if result == "You win!":
        global user_score
        user_score += 1
    elif result == "You lose!":
        global computer_score
        computer_score += 1
    
    # Update score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

# Function to update the result and choices display
def update_labels(user_choice, computer_choice, result):
    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    animate_result(result)

# Initialize the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")
window.geometry("400x400")
window.configure(bg="darkblue")

# Configure grid layout to center content
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)
window.grid_rowconfigure(6, weight=1)
window.grid_rowconfigure(7, weight=1)

window.grid_columnconfigure(0, weight=1)

# Initialize scores
user_score = 0
computer_score = 0

# Create and place the widgets in the center
title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"), bg="darkblue", fg="white")
title_label.grid(row=0, column=0, pady=10)

button_rock = tk.Button(window, text="Rock", command=lambda: make_choice("rock"), width=10, bg="midnightblue", fg="white")
button_rock.grid(row=1, column=0, pady=5)

button_paper = tk.Button(window, text="Paper", command=lambda: make_choice("paper"), width=10, bg="midnightblue", fg="white")
button_paper.grid(row=2, column=0, pady=5)

button_scissors = tk.Button(window, text="Scissors", command=lambda: make_choice("scissors"), width=10, bg="midnightblue", fg="white")
button_scissors.grid(row=3, column=0, pady=5)

user_choice_label = tk.Label(window, text="", font=("Arial", 12), bg="darkblue", fg="white")
user_choice_label.grid(row=4, column=0, pady=5)

computer_choice_label = tk.Label(window, text="", font=("Arial", 12), bg="darkblue", fg="white")
computer_choice_label.grid(row=5, column=0, pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14), bg="darkblue", fg="white", wraplength=300)
result_label.grid(row=6, column=0, pady=10)

score_frame = tk.Frame(window, bg="darkblue")
score_frame.grid(row=7, column=0, pady=5)

user_score_label = tk.Label(score_frame, text="Your Score: 0", font=("Arial", 12), bg="darkblue", fg="white")
user_score_label.pack(side=tk.LEFT, padx=20)

computer_score_label = tk.Label(score_frame, text="Computer's Score: 0", font=("Arial", 12), bg="darkblue", fg="white")
computer_score_label.pack(side=tk.RIGHT, padx=20)

# Run the application
window.mainloop()
