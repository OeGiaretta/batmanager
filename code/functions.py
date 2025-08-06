import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd

eScript = 0
inScript = 0

def Inclusao():

    app = ctk.CTk()
    app.title("Inclusão de Script")
    app.geometry("500x500")
    app._set_appearance_mode("dark")

    fontScript = ctk.CTkFont(family="Arial", size=20)

    # Entrada da Descrição
    eDesc = ctk.CTkEntry(
        app, placeholder_text="Descrição", 
        height=50, 
        width=300, 
        font=fontScript
        )
    eDesc.place(x=100, y=25)
    inDesc = eDesc.get()

    eDesc._set_appearance_mode("dark")

    # Entrada do Script
    eScript = ctk.CTkEntry(app, 
                        placeholder_text="Digite o comando/script", 
                        height=180, 
                        width=300, 
                        font=fontScript
                        )
    eScript.place(x=100, y=180)
    inScript = eScript.get()
    eScript._set_appearance_mode("dark")

    # Botão de inclusão
    inCommand = ctk.CTkButton(app, text="Incluir", command=0)
    inCommand.place(x=180, y=400)
    inCommand._set_appearance_mode("dark")

    app.mainloop()