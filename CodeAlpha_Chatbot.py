import tkinter as tk
from tkinter import scrolledtext
import random

# Define bot responses
def get_bot_response(user_input):
    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey", "good morning", "good evening"]
    how_are_you = ["how are you", "how are you doing"]
    farewells = ["bye", "goodbye", "see you", "exit"]
    thanks = ["thank you", "thanks", "thx"]

    if any(word in user_input for word in greetings):
        return random.choice(["Hi there!", "Hello!", "Hey!"])

    elif any(phrase in user_input for phrase in how_are_you):
        return random.choice(["I'm doing well, thanks!", "Feeling great!", "All systems go!"])

    elif any(word in user_input for word in farewells):
        return random.choice(["Goodbye!", "See you later!", "Take care!"])

    elif any(word in user_input for word in thanks):
        return "You're welcome!"

    elif "your name" in user_input:
        return "I'm ChatPy, your GUI chatbot."

    elif "help" in user_input:
        return "Say 'hello', 'how are you', 'bye', or ask 'what's your name'."

    else:
        return random.choice([
            "Sorry, I didn't get that.",
            "Can you rephrase that?",
            "I'm still learning. Try again!"
        ])

# GUI Setup
def send_message():
    user_msg = user_input.get()
    if user_msg.strip() == "":
        return

    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {user_msg}\n")
    response = get_bot_response(user_msg)
    chat_area.insert(tk.END, f"ChatPy: {response}\n\n")
    chat_area.config(state='disabled')
    chat_area.yview(tk.END)
    user_input.delete(0, tk.END)

# Main window
root = tk.Tk()
root.title("ChatPy - GUI Chatbot")
root.geometry("400x500")
root.resizable(False, False)

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 10))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input field
user_input = tk.Entry(root, font=("Arial", 12))
user_input.pack(padx=10, pady=10, fill=tk.X)
user_input.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_button.pack(pady=5)

# Start GUI loop
root.mainloop()
