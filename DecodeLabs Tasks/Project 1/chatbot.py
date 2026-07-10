import tkinter as tk
from tkinter import scrolledtext

                                            # Chatbot Function

def chatbot():

    user = entry.get().lower().strip()

    if user == "":
        return

    if user == "hi":
        reply = "Hello! 👋"

    elif user == "hello":
        reply = "Hi! 😊"

    elif user == "how are you":
        reply = "I am fine. 😊"

    elif user == "what is your name":
        reply = "I am DecodeBot. 🤖"

    elif user == "who made you":
        reply = "Arooj made me. 👩‍💻"

    elif user == "exit":
        reply = "Goodbye! 👋"
        
    elif user == "good morning":
        reply= "☀️Good Morning! Have a wonderful day."
        
    elif user == "good afternoon":
       reply= "🌞Good Afternoon!"

    else:
        reply = "Sorry! I don't understand."

    # Show Conversation
    chat.insert(tk.END, "👤 You : " + user + "\n")
    chat.insert(tk.END, "🤖 Bot : " + reply + "\n\n")

# Automatically scroll to the latest message
    chat.see(tk.END)

    entry.delete(0, tk.END)

    if user == "exit":
        window.after(1500, window.destroy)

                                                   
                                                   # Window

window = tk.Tk()
window.title("DecodeBot")
window.geometry("500x500")
window.configure(bg="lightblue")

# Heading
heading = tk.Label(
    window,
    text="🤖 DecodeBot",
    font=("Arial",20,"bold"),
    bg="navy",
    fg="white"
)
heading.pack(fill="x")

                                                  # Chat Area

chat = scrolledtext.ScrolledText(
    window,
    width=50,
    height=15,
    font=("Arial",12),
    wrap=tk.WORD
)

chat.pack(pady=15)

                                                    # Entry
                                                    
entry = tk.Entry(
    window,
    font=("Arial",14),
    width=30
)
entry.pack()

entry.bind("<Return>", lambda event: chatbot())

                                                    # Button

button = tk.Button(
    window,
    text="Send",
    font=("Arial",13),
    bg="green",
    fg="white",
    command=chatbot
)
button.pack(pady=15)

window.mainloop()