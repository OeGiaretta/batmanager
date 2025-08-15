import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import subprocess as sp
import json 

global eScript, inScript, app, listbox, atualizar_listbox

eScript = 0
inScript = 0


# Atualiza a listbox na janela principal
def atualizar_listbox():
    global ferramentas
    listbox.delete(0, tk.END)
    for item in ferramentas:
        listbox.insert(tk.END, item["Descrição"])

def Inclusao():

    with open(
    "c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json", 
    encoding="utf-8"
    ) as f:
        ferramentas = json.load(f)

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

    def incluir_script():
    # Verifica se os campos estão preenchidos
        if eDesc.get() and eScript.get():
            nova_ferramenta = {
                "Descrição": eDesc.get(),
                "Script": eScript.get()
            }
            ferramentas.append(nova_ferramenta)
            with open(
                "c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json", 
                "w",  # modo escrita
                encoding="utf-8"
            ) as f:
                json.dump(ferramentas, f, indent=4, ensure_ascii=False)
            
        # Fecha a janela de inclusão
            app.destroy()

    # Botão de inclusão
    inCommand = ctk.CTkButton(app, text="Incluir", command=incluir_script)
    inCommand.place(x=180, y=400)
    inCommand._set_appearance_mode("dark")
    atualizar_listbox()

    app.mainloop()

# Deletar Script
def delScript():
    selecionado = listbox.curselection()
    if selecionado:
        idx = selecionado[0]
        with open("c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json", encoding="utf-8") as f:
            ferramentas = json.load(f)
        ferramentas.pop(idx)
        with open("c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json", "w", encoding="utf-8") as f:
            json.dump(ferramentas, f, indent=4, ensure_ascii=False)
        listbox.delete(idx)
        atualizar_listbox()



