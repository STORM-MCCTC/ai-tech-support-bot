import openai
import tkinter as tk
from tkinter import scrolledtext
import random

# Set your OpenAI API key here
openai.api_key = ''  # Replace with your actual API key

# List of bot names to choose from
bot_names = [
    "Alex", "Sam", "Charlie", "Jordan", "Riley", "Taylor",
    "Casey", "Morgan", "Dakota", "Jamie", "Quinn", "Bailey",
    "Jordan", "Avery", "Skyler", "Cameron", "Emerson", "Addison",
    "Hunter", "Dakota", "Peyton", "Blake", "Logan", "Finley",
    "Elliot", "Sage", "Reagan", "Lennox", "Carter", "Emery",
    "Mackenzie", "Jesse", "Sawyer", "Phoenix", "Tatum", "Marley",
    "Rowan", "River", "Dakota", "Sloan", "Stevie", "Reese"
]

# Randomly select a bot name
bot_name = random.choice(bot_names)

# Create a function to handle the chat logic
def get_response():
    user_input = entry.get()
    if user_input.lower() == 'exit':
        window.quit()
        return

    # Display user input in the chat window
    chat_box.config(state=tk.NORMAL)  # Enable chat box for editing
    chat_box.insert(tk.END, "You: " + user_input + '\n')
    chat_box.config(state=tk.DISABLED)  # Disable chat box after update
    
    # Call OpenAI API for chatbot response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": f"you are a Customer Service Chatbot, your name is {bot_name}, you are helping the user with tech issues, user input: {user_input}"}]
    )

    # Display bot response
    bot_reply = response['choices'][0]['message']['content']
    
    # Re-enable the chat box to display the bot's reply
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"{bot_name}: " + bot_reply + '\n')
    chat_box.config(state=tk.DISABLED)  # Disable chat box after update
    
    chat_box.yview(tk.END)  # Scroll to the bottom
    entry.delete(0, tk.END)  # Clear the input box

# Create the main window
window = tk.Tk()
window.title("Chatbot")

# Create a chat display box
chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_box.grid(row=0, column=0, padx=10, pady=10)

# Create an input box for the user
entry = tk.Entry(window, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

# Create a send button
send_button = tk.Button(window, text="Send", width=10, command=get_response)
send_button.grid(row=2, column=0, padx=10, pady=10)

# Run the application
window.mainloop()
