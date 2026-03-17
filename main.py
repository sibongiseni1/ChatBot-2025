import tkinter as tk
from tkinter import scrolledtext


responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "Hi chat": "Heyy",
    "how are you": "I am just a chatbot, but I am doing good!",

    "bye": "Goodbye! Have a good day"
}

def send_message():
    user_input = user_entry.get().lower()
    if not user_input:
        return  
    chat_window.insert(tk.END, f"You: {user_input}\n")
    
    if user_input == "exit":
        chat_window.insert(tk.END, "Chatbot: Goodbye\n")
        root.after(1000, root.destroy)
        return

    response = responses.get(user_input, "Sorry, I don't understand you.")
    chat_window.insert(tk.END, f"Chatbot: {response}\n")
    user_entry.delete(0, tk.END)
    chat_window.yview(tk.END)  


root = tk.Tk()
root.title("Chatbot GUI")


chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_window.pack(padx=10, pady=10)
chat_window.config(state=tk.NORMAL)


user_entry = tk.Entry(root, width=40)
user_entry.pack(side=tk.LEFT, padx=(10,0), pady=(0,10))
user_entry.focus()


send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(5,10), pady=(0,10))

root.bind('<Return>', lambda event: send_message())

root.mainloop()
