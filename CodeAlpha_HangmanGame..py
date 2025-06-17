import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random

# --------------------------
# Game Logic Setup
# --------------------------
words = ["apple", "banana", "grape", "orange", "melon"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts_left = 6
guessed_letters = []

# --------------------------
# GUI Setup
# --------------------------
window = tk.Tk()
window.title("🎯 Hangman Game")
window.geometry("500x450")
window.configure(bg="#2b2d42")

# --------------------------
# Styling
# --------------------------
style = ttk.Style()
style.configure("Guess.TButton",
                font=("Arial", 12, "bold"),
                padding=6,
                background="#d90429",   # Red
                foreground="white")

style.map("Guess.TButton",
          background=[("active", "#a60f1f")],  # Darker red on hover
          foreground=[("active", "white")])

# --------------------------
# Widgets
# --------------------------

# Title
title_label = tk.Label(window, text="✨ Hangman Game ✨",
                       font=("Courier New", 24, "bold"),
                       bg="#2b2d42", fg="#edf2f4")
title_label.pack(pady=20)

# Word Display
word_frame = tk.Frame(window, bg="#2b2d42")
word_frame.pack(pady=10)
word_label = tk.Label(word_frame, text=" ".join(guessed_word),
                      font=("Consolas", 22, "bold"),
                      bg="#2b2d42", fg="#f8f32b")
word_label.pack()

# Guessed Letters
letters_label = tk.Label(window, text="Guessed Letters: ",
                         font=("Arial", 12),
                         bg="#2b2d42", fg="#ffffff")
letters_label.pack(pady=5)

# Attempts Left
attempts_label = tk.Label(window, text=f"Attempts Left: {attempts_left}",
                          font=("Arial", 12),
                          bg="#2b2d42", fg="#ffffff")
attempts_label.pack(pady=5)

# Input Frame
input_frame = tk.Frame(window, bg="#2b2d42")
input_frame.pack(pady=15)

letter_entry = ttk.Entry(input_frame, font=("Arial", 14), width=5)
letter_entry.grid(row=0, column=0, padx=10)

def guess_letter():
    global attempts_left
    guess = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)

    if not guess.isalpha() or len(guess) != 1:
        messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter.")
        return

    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'.")
        return

    guessed_letters.append(guess)

    if guess in word:
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed_word[idx] = guess
        word_label.config(text=" ".join(guessed_word))
        letters_label.config(text="Guessed Letters: " + ", ".join(guessed_letters))
        if "_" not in guessed_word:
            messagebox.showinfo("🎉 You Win!", f"Congratulations! You guessed the word: {word}")
            window.destroy()
    else:
        attempts_left -= 1
        attempts_label.config(text=f"Attempts Left: {attempts_left}")
        letters_label.config(text="Guessed Letters: " + ", ".join(guessed_letters))
        if attempts_left == 0:
            messagebox.showerror("💀 Game Over", f"You're out of attempts. The word was: {word}")
            window.destroy()

# Red Guess Button
guess_button = ttk.Button(input_frame, text="Guess", command=guess_letter, style="Guess.TButton")
guess_button.grid(row=0, column=1, padx=5)

# Footer
footer = tk.Label(window, text="Made with ❤️ in Python",
                  font=("Arial", 10),
                  bg="#2b2d42", fg="#8d99ae")
footer.pack(side="bottom", pady=10)

# --------------------------
# Run App
# --------------------------
window.mainloop()
