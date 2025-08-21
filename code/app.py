import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import functions as fnc
import json

opcao = []

with open(
    "c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json",
    encoding="utf-8",
) as f:
    ferramentas = json.load(f)

# Função para atualizar a Listbox
def atualizar_listbox():
    listbox.delete(0, tk.END)
    with open(
        "c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json",
        encoding="utf-8",
    ) as f:
        ferramentas_atualizadas = json.load(f)
    for item in ferramentas_atualizadas:
        listbox.insert(tk.END, item["Descrição"])

# Função para selecionar o item da Listbox
def selecao(event):
    selecionado = listbox.get(listbox.curselection())

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Inicia o programa
app = ctk.CTk()
app.title("BatManager")
app.geometry("900x650")

# BottomBar e botões
bottombar = ctk.CTkFrame(app, height=250, corner_radius=0)
bottombar.pack(side="bottom", fill="x")

buttonIncluir = ctk.CTkButton(
    bottombar, 
    text="Incluir", 
    command=lambda: fnc.Inclusao(app, atualizar_listbox)
)

buttonIncluir.place(x=715, y=45)

buttonAlterar = ctk.CTkButton(
    bottombar, 
    text="Alterar", 
    command=0
    )
buttonAlterar.place(x=715, y=90)


buttonExcluir = ctk.CTkButton(
    bottombar, 
    text="Excluir", 
    command=lambda: fnc.delScript(listbox, ferramentas)
    )
buttonExcluir.place(x=715, y=135)

buttonExecutar = ctk.CTkButton(
    bottombar, 
    text="Executar", 
    command=0
    )
buttonExecutar.place(x=715, y=180)

# List

fontListbox = tkFont.Font(family="Arial", size=11)
listbox = tk.Listbox(
    bottombar, 
    height=10, 
    width=73, 
    selectmode=tk.SINGLE, 
    font=fontListbox
)
listbox.place(x=30, y=45)
for item in ferramentas:
    listbox.insert(tk.END, item["Descrição"])

listbox.bind("<<ListboxSelect>>", selecao)






app.mainloop()
