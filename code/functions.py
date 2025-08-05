import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd

# def Inclusao():
app = ctk.CTk()
app.title("Inclusão de Script")
app.geometry("500x500")
app._set_appearance_mode("dark")

eDesc = ctk.CTkEntry(app, placeholder_text="Descrição", height=50, width=300)
eDesc.place(x=100, y=25)
eDesc._set_appearance_mode("dark")




fontScript = tkFont.Font(family="Arial", size=20)
eScript = ctk.CTkEntry(app, 
                       placeholder_text="Digite o comando/script", 
                       height=180, 
                       width=300, 
                       font=fontScript
                       )
eScript.place(x=100, y=180)
eScript._set_appearance_mode("dark")











def mosResposta():
    mostrarTeste = print(eDesc, eScript)

teste = ctk.CTkButton(app, text="Incluir", command=mosResposta)
teste.place(x=180, y=400)
teste._set_appearance_mode("dark")





app.mainloop()