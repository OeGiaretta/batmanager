import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import functions as fnc
import json 
from functions import *

with open(
    "c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json", 
    encoding="utf-8"
    ) as f:
    ferramentas = json.load(f)

opcao = []

app = ctk.CTk()
app.title("BatManager")
app.geometry("900x650")
app._set_appearance_mode("dark")

# BottomBar e botões

bottombar = ctk.CTkFrame(app, height=250, corner_radius=0)
bottombar.pack(side="bottom", fill="x")
bottombar._set_appearance_mode("dark")

buttonIncluir = ctk.CTkButton(bottombar, text="Incluir", command=fnc.Inclusao)
buttonIncluir.place(x=715, y=45)
buttonIncluir._set_appearance_mode("dark")

buttonAlterar = ctk.CTkButton(bottombar, text="Alterar", command=0)
buttonAlterar.place(x=715, y=90)
buttonAlterar._set_appearance_mode("dark")


buttonExcluir = ctk.CTkButton(bottombar, text="Excluir", command=0)
buttonExcluir.place(x=715, y=135)
buttonExcluir._set_appearance_mode("dark")


buttonExecutar = ctk.CTkButton(bottombar, text="Executar", command=0)
buttonExecutar.place(x=715, y=180)
buttonExecutar._set_appearance_mode("dark")

# List

fontListbox = tkFont.Font(family="Arial", size=11)
listbox = tk.Listbox(
    bottombar, 
    height=10, 
    width=80, 
    selectmode=tk.SINGLE,
    font=fontListbox
    )
listbox.place(x=30, y=45)

for command in opcao:
    listbox.insert(tk.END, command["Descrição"])

# Adicionando na lista
def selecao(event):
    selecionado = listbox.get(listbox.curselection())
listbox.bind("<<ListboxSelect>>", selecao)

app.mainloop()