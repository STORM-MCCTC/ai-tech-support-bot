import openai
import tkinter as tk
from tkinter import scrolledtext
import random

with open('api-key.txt', 'r') as file:
    api_key = file.read().strip()
    openai.api_key = api_key

bot_names = [
    "Alex", "Sam", "Charlie", "Jordan", "Riley", "Taylor",
    "Casey", "Morgan", "Dakota", "Jamie", "Quinn", "Bailey",
    "Jordan", "Avery", "Skyler", "Cameron", "Emerson", "Addison",
    "Hunter", "Dakota", "Peyton", "Blake", "Logan", "Finley",
    "Elliot", "Sage", "Reagan", "Lennox", "Carter", "Emery",
    "Mackenzie", "Jesse", "Sawyer", "Phoenix", "Tatum", "Marley",
    "Rowan", "River", "Dakota", "Sloan", "Stevie", "Reese"
]

bot_name = random.choice(bot_names)

def get_response():
    user_input = entry.get()
    if user_input.lower() == 'exit':
        window.quit()
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + '\n')
    chat_box.config(state=tk.DISABLED)
    
  
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": f"you are a Customer Service Chatbot, your name is {bot_name}, you are helping the user with tech issues, user input: {user_input}"}]
    )

    bot_reply = response['choices'][0]['message']['content']
    
 
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"{bot_name}: " + bot_reply + '\n')
    chat_box.config(state=tk.DISABLED)  
    
    chat_box.yview(tk.END) 
    entry.delete(0, tk.END)

window = tk.Tk()
window.title("Chatbot")

chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_box.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(window, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

send_button = tk.Button(window, text="Send", width=10, command=get_response)
send_button.grid(row=2, column=0, padx=10, pady=10)

window.mainloop()
