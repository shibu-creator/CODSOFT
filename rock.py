import tkinter as tk
import random

# Emoji for rock,paper,scissors
choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

# Score counters
user_score = 0
computer_score = 0

# Main logic of the game
def play_game(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(list(choices.keys()))

    # Show choices
    user_choice_label.config(text=f"You picked: {choices[user_choice]} ({user_choice})")
    computer_choice_label.config(text=f"Computer picked: {choices[computer_choice]} ({computer_choice})")

    # Determine winner
    if user_choice == computer_choice:
        result.set("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result.set("You win!")
        user_score += 1
    else:
        result.set("Computer wins!")
        computer_score += 1

    # Update score display
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")

# Setup GUI window
app = tk.Tk()
app.title("Rock Paper Scissors")
app.geometry("400x300")  # 🔧 Set proper window size

# Game title
tk.Label(app, text="Rock Paper Scissors").pack(pady=10)

# Game buttons
tk.Button(app, text="Rock 🪨", width=15, command=lambda: play_game("rock")).pack()
tk.Button(app, text="Paper 📄", width=15, command=lambda: play_game("paper")).pack()
tk.Button(app, text="Scissors ✂️", width=15, command=lambda: play_game("scissors")).pack()

# Labels for choices
user_choice_label = tk.Label(app, text="You picked:")
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(app, text="Computer picked:")
computer_choice_label.pack(pady=5)

# Result label
result = tk.StringVar()
tk.Label(app, textvariable=result).pack(pady=5)

# Score label
score_label = tk.Label(app, text="You: 0 | Computer: 0")
score_label.pack(pady=5)

# Start GUI loop
app.mainloop()
