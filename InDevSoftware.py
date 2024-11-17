#This is a copy of the open source project OGPTC (Offline Generative Pre-Trained Chatbot)
#You can modify the file without any restriction!
#Be sure to know what are you doing because it is very difficult to understand and modify this file by yourself
#You can ask a friend or an expert before modifying the file

#Imports
import tkinter as tk
from tkinter import messagebox
import time

#Build software
print("Building Software...")
time.sleep(6.5)
print("[Done]")
print("Debuging...")
time.sleep(5.25)
print("[Done]")
print("Starting program...")

# Database
intents = {
    "greeting": ["ChatBot: Hi! How can I help?","ChatBot: Oh hello, how can I assist you today? :)"],
    "farewell": ["ChatBot: Bye, see you later!","ChatBot: GoodBye, take care!"],
}

# Main window
def create_window():
    window = tk.Tk()
    window.title("ChatBot based on The OGPTC Open Source Project")
    window.geometry("700x200")
    window.configure(bg='#2d3640')

    label = tk.Label(window, text="This Chatbot is based on the OGPTC Open source project",font=("Calibri",12, "bold"), fg="White")
    label.configure(bg='#2d3640')
    label.pack(side="bottom")

    line = tk.Frame(window)
    line.configure(bg='White')
    line.pack(side="bottom", fill="x", padx=10, pady=10)
    
    # Calculate expressions
    def calculate_expression(expression):
        try:
            result = eval(expression)
            return f"ChatBot: {expression} = {result}"
        except Exception as e:
            return f"ChatBot: Sorry, I don't understand. Can you repeat please ?"

    # Press Enter / Send button Function 
    def handle_button():
        user_input = entry.get()
        intent = get_intent(user_input)
        if intent:
            print("Results found in 0.14 seconds")
            print("Giving answer token 0.14 seconds")
            response = intents.get(intent, ["ChatBot: Sorry, I don't understand. Can you repeat please?"])[0]
            entry.delete(0, tk.END)
        else:
            print("Results found in 0.15 seconds")
            print("Giving answer token 0.15 seconds")
            response = calculate_expression(user_input)
        output_label.config(text=response)
        entry.delete(0, tk.END)

    #ChatBot Version
    def info_button():
        messagebox.showinfo("About", "ChatBot of the future. Version 1.0")

    #Close window
    def close_window():
        window.destroy()

    #Light mode
    def light_mode():
        window.configure(bg='white')
        frame.configure(bg='white')
        entry.configure(bg='Light Blue')
        entry.configure(font=("Calibri",12, "bold"), fg="Black")
        evaluate_button.configure(bg="Orange")
        evaluate_button.configure(fg="Black")
        output_label.configure(bg='White')
        output_label.configure(fg="Black")
        label.configure(bg='White')
        label.configure(fg='red')
        line.configure(bg='black')
        info.configure(bg='White')
    #Dark mode
    def dark_mode():
        window.configure(bg='#2d3640')
        frame.configure(bg='#2d3640')
        entry.configure(bg='gray')
        entry.configure(font=("Calibri",12, "bold"), fg="white")
        evaluate_button.configure(bg="Orange")
        evaluate_button.configure(fg="white")
        output_label.configure(bg='#2d3640')
        output_label.configure(fg="white")
        label.configure(bg='#2d3640')
        label.configure(fg='White')
        line.configure(bg='white')
        info.configure(bg='white')

    #Accessibility settings
    def show_frames():
        label.configure(bg='Orange')
        frame.configure(bg='Orange')
        output_label.configure(bg="Orange")
        info.configure(bg='Orange')
    
    def strange_colors():
        window.configure(bg='Black')
        frame.configure(bg='Orange')
        entry.configure(bg='Blue')
        evaluate_button.configure(bg="Blue")
        output_label.configure(bg='Orange')
        label.configure(bg='Orange')
        line.configure(bg='Red')
        info.configure(bg='Orange')

    #Paramètres
    def settings():
        root = tk.Tk()
        root.title("Settings")
        root.geometry('253x254')
        root.configure(bg='#2d3640')
        root.resizable(False, False)
        root.mainloop
        
        #Main settings
        settings = tk.Label(root, text="Main settings")
        settings.configure(bg='#2d3640', fg="Dark Gray")
        settings.pack(side="top")
        
        p = tk.Frame(root)
        p.pack(side="top", fill = "x", padx=10, pady=10)
        p.configure(bg='#2d3640')
        p.grid_columnconfigure(0, weight=1)
    
        s = tk.Frame(root)
        s.configure(bg='#2d3640')
        s.pack(side="top", fill="x", padx=10, pady=10)
        s4 = tk.Label(s, text="Change theme")
        s4.configure(bg='#2d3640', fg='White')
        s4.pack(side="left")
        b = tk.Button(s, text="Light mode", command=light_mode, relief="flat", highlightthickness=0,borderwidth=0)
        b.pack(side="right")
        b2 = tk.Label(s, text="I")
        b2.configure(bg='#2d3640', fg='White')
        b2.pack(side="right") 
        b2 = tk.Button(s, text="Dark mode", command=dark_mode, relief="flat", highlightthickness=0, borderwidth=0)
        b2.pack(side="right")

        label=tk.Frame(root)
        label.configure(bg='#2d3640')
        label.configure(bg='black')
        label.pack(side="top", fill="x", padx=10, pady=10)

        Accessibility_settings = tk.Label(root, text="Accessibility settings")
        Accessibility_settings.configure(bg='#2d3640', fg='White')
        Accessibility_settings.configure(fg="Dark Gray")
        Accessibility_settings.pack(side="top")

        fr = tk.Frame(root)
        fr.configure(bg='#2d3640')
        fr.pack(side='top', fill="x", padx=10, pady=10)
        a1 = tk.Label(fr, text="Show frames")
        a1.configure(bg='#2d3640', fg='White')
        a1.pack(side="left")
        a1_button = tk.Button(fr, text="Show", command=show_frames, relief='flat', highlightthickness=0, borderwidth=0)
        a1_button.pack(side='right')

        fra = tk.Frame(root)
        fra.configure(bg='#2d3640')
        fra.pack(side='top', fill="x", padx=10, pady=10)
        ac1 = tk.Label(fra, text="Enable strange colors")
        ac1.configure(bg='#2d3640', fg='White')
        ac1.pack(side="left")
        ac1_button = tk.Button(fra, text="Activate", command=strange_colors, relief='flat', highlightthickness=0, borderwidth=0)
        ac1_button.pack(side='right')
        
    #Un cadre pour contenir la barre de saisie et le boutton
    frame = tk.Frame(window)
    frame.configure(bg='#2d3640')
    frame.pack(side= "bottom", fill="x", padx=10, pady=10) #Padding pour l'esthétique de la fenêtre
    frame.grid_columnconfigure(0, weight=1)

    #Cadre pour un boutton informateur
    info = tk.Frame(window)
    info.configure(bg='white')
    info.pack(side='top', fill="x")
    info.grid_columnconfigure(0, weight=1)

    #Informations
    information = tk.Button(info, text = "About ChatBot", command=info_button, relief="flat", highlightthickness=0, borderwidth=0)
    information.configure(bg='white')
    information.pack(side="left")

    #Settings
    settings = tk.Button(info, text="  Settings  ", command=settings, relief="flat", highlightthickness=0, borderwidth=0)
    settings.configure(bg='white')
    settings.pack(side="left")
    
    #Close button
    close_button = tk.Button(info, text = "  Close ChatBot  ", command=close_window, relief="flat", highlightthickness=0, borderwidth=0)
    close_button.configure(bg='white')
    close_button.pack(side="left")
    
    show = tk.Label(info, text="The OGPTC Open source project", font=("Calibri", 13, "bold"), fg='Gray')
    show.configure(bg="White")
    show.pack(side="right")
    
    # Entry for questions
    entry = tk.Entry(frame, relief="flat", borderwidth=0)
    entry.grid(row=0, column=0, sticky="ew", ipady=3.4)
    entry.focus
    entry.configure(bg="Gray")
    entry.configure(font=("Calibri",12, "bold"), fg='White')

    # Button to submit question
    evaluate_button = tk.Button(frame, text="Submit", command=handle_button, relief="flat", highlightthickness=0, borderwidth=0)
    evaluate_button.grid(row=0, column=1, ipady=1.4, pady=10, padx=10)
    evaluate_button.configure(bg='Orange')
    evaluate_button.configure(font=("Calibri",12,"bold"), fg='White')
    
    #Label for answer/Result
    output_label = tk.Label(window, text="ChatBot: Hello there! How can I assist you today ?", font=("Calibri", 12, "bold"), fg="white", wraplength=950)
    output_label.configure(bg='#2d3640')
    output_label.pack(side="top")
    
   # Boucle pour la fenêtre
    window.mainloop()
    
# Trouver la réponse à la question
def get_intent(query):
    query = query.lower()
    if "hello" in query:
        print("ChatBot answered.")
        print("Waiting for user's request")
        return "greeting"
    
    if "bye" in query:
        print("ChatBot answered")
        print("Waiting for user's request")
        return "farewell"

    else:
        return None

if __name__ == "__main__":
    create_window()
