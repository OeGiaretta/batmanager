import customtkinter as ctk
import tkinter as tk
import tkinter.font as tkFont
import pandas as pd
import subprocess as sp
import json 

def Inclusao(app, callback=None):

    with open(
    "c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json", 
    encoding="utf-8"
    ) as f:
        ferramentas = json.load(f)

    janela = ctk.CTkToplevel(app)
    janela.title("Inclusão de Script")
    janela.geometry("500x500")
    janela.lift()
    janela.grab_set()

    fontScript = ctk.CTkFont(family="Arial", size=20)

    # Entrada da Descrição
    eDesc = ctk.CTkEntry(
        janela, placeholder_text="Descrição", 
        height=50, 
        width=300, 
        font=fontScript
        )
    eDesc.place(x=100, y=25)
    inDesc = eDesc.get()

    # Entrada do Script
    eScript = ctk.CTkEntry(janela, 
                        placeholder_text="Digite o comando/script", 
                        height=180, 
                        width=300, 
                        font=fontScript
                        )
    eScript.place(x=100, y=180)
    inScript = eScript.get()

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
            janela.destroy()
            
        # Atualiza a Listbox se uma função de callback for fornecida
            if callback:
                callback()

    # Botão de inclusão
    inCommand = ctk.CTkButton(janela, text="Incluir", command=incluir_script)
    inCommand.place(x=180, y=400)


# Deletar Script
def delScript(listbox, ferramentas):
        
    # Obtém o índice do item selecionado
    selected_index = listbox.curselection()
    
    if selected_index:
        # Remove o item da lista de ferramentas
        del ferramentas[selected_index[0]]
        
        # Atualiza o arquivo JSON
        with open(
            "c:/Users/Eduardo/Documents/Learn/dev/batmanager/code/ferramentas.json", 
            "w", 
            encoding="utf-8"
        ) as f:
            json.dump(ferramentas, f, indent=4, ensure_ascii=False)
        