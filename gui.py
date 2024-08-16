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
        result_label.config(text="🎉 You Win! 🎉")
        result_label.config(fg="green")
        animate_win()
    elif result == "You lose!":
        result_label.config(text="💥 You Lose! 💥")
        result_label.config(fg="red")
        animate_loss()
    else:
        result_label.config(text="It's a tie!")
        result_label.config(fg="gray")

# Animation for win
def animate_win():
    for _ in range(3):
        result_label.config(bg="lightgreen")
        window.update()
        window.after(200)
        result_label.config(bg="blue")
        window.update()
        window.after(200)

# Animation for loss
def animate_loss():
    for _ in range(3):
        result_label.config(bg="lightcoral")
        window.update()
        window.after(200)
        result_label.config(bg="blue")
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
window.geometry("300x300")
window.configure(bg="blue")

# Initialize scores
user_score = 0
computer_score = 0

# Create and place the widgets
tk.Label(window, text="Rock-Paper-Scissors Game", font=("Arial", 40), bg="blue").pack(pady=10)

tk.Button(window, text="Rock", command=lambda: make_choice("rock"), width=10).pack(pady=5)
tk.Button(window, text="Paper", command=lambda: make_choice("paper"), width=10).pack(pady=5)
tk.Button(window, text="Scissors", command=lambda: make_choice("scissors"), width=10).pack(pady=5)

user_choice_label = tk.Label(window, text="", font=("Arial", 12), bg="blue")
user_choice_label.pack(pady=5)
computer_choice_label = tk.Label(window, text="", font=("Arial", 12), bg="blue")
computer_choice_label.pack(pady=5)
result_label = tk.Label(window, text="", font=("Arial", 12), bg="blue", wraplength=250)
result_label.pack(pady=10)

user_score_label = tk.Label(window, text="Your Score: 0", font=("Arial", 12), bg="blue")
user_score_label.pack(pady=5)
computer_score_label = tk.Label(window, text="Computer's Score: 0", font=("Arial", 12), bg="blue")
computer_score_label.pack(pady=5)

# Run the application
window.mainloop()
