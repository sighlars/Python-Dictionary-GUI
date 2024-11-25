import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch the definition
def get_definition():
    word = word_entry.get().strip()
    if not word:
        messagebox.showerror("Input Error", "Please enter a word to search.")
        return
    
    try:
        # Fetch definition using a dictionary API
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        if response.status_code == 200:
            data = response.json()
            definition = data[0]['meanings'][0]['definitions'][0]['definition']
            definition_label.config(text=f"Definition:\n{definition}", fg="black")
        else:
            definition_label.config(text="Word not found. Please try again.", fg="red")
    except Exception as e:
        definition_label.config(text=f"Error: {str(e)}", fg="red")

# Create the main window
root = tk.Tk()
root.title("Smart Dictionary")
root.geometry("500x300")
root.configure(bg="#f7f7f7")

# GUI components
title_label = tk.Label(root, text="Smart Dictionary", font=("Helvetica", 18, "bold"), bg="#f7f7f7", fg="#333")
title_label.pack(pady=10)

word_label = tk.Label(root, text="Enter a word:", font=("Arial", 14), bg="#f7f7f7", fg="#555")
word_label.pack(pady=5)

word_entry = tk.Entry(root, width=30, font=("Arial", 14), bd=2, relief="groove", justify="center")
word_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=get_definition, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", bd=0, relief="flat", padx=10, pady=5)
search_button.pack(pady=10)

definition_label = tk.Label(root, text="", wraplength=450, font=("Arial", 12), justify="left", bg="#f7f7f7", fg="#333")
definition_label.pack(pady=20)

# Run the main loop
root.mainloop()
