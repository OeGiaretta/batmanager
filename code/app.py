import customtkinter as ctk
import pandas as pd

opcao = ["teste1", "teste2", "teste3"]

app = ctk.CTk()
app.title('BatManager')
app.geometry('900x650')
app._set_appearance_mode('dark')


# BottomBar e botões

bottombar = ctk.CTkFrame(app, height=250, corner_radius=0)
bottombar.pack(side="bottom", fill="x")
bottombar._set_appearance_mode('dark')

buttonIncluir = ctk.CTkButton(bottombar, text="Incluir", command=0 )
buttonIncluir.place(x=715, y=45 )
buttonIncluir._set_appearance_mode('dark')


buttonAlterar = ctk.CTkButton(bottombar, text="Incluir", command=0 )
buttonAlterar.place(x=715, y=90 )
buttonAlterar._set_appearance_mode('dark')


buttonExcluir = ctk.CTkButton(bottombar, text="Incluir", command=0 )
buttonExcluir.place(x=715, y=135 )
buttonExcluir._set_appearance_mode('dark')


buttonExecutar = ctk.CTkButton(bottombar, text="Incluir", command=0 )
buttonExecutar.place(x=715, y=180 )
buttonExecutar._set_appearance_mode('dark')

# List

def ao_selecionar(opcao):
    print(f"Selecionado: {opcao}")
lista = ctk.CTkOptionMenu(bottombar, values=opcao, command=ao_selecionar)
lista.place()


app.mainloop()
