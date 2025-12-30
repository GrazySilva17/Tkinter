#Cadastro de Usuário com Tkinter

import tkinter as tk

janela = tk.Tk()
janela.title("Cadastro Simples de Usuário")
janela.configure(bg="hot pink")
janela.geometry("400x300+725+334")

fonte = ("Helvetica", 12, "bold")

cadastroUsuario = tk.LabelFrame(janela, text="Cadastro de Usuário", bg="misty rose", padx=10, pady=10)
cadastroUsuario.configure(width=350, height=250)
cadastroUsuario.pack()

nomeUsuario = tk.Label(cadastroUsuario, text="Nome usuário")
nomeUsuario.config(fg="gray11", bg="misty rose", font=fonte)
nomeUsuario.pack(pady=5)

entradaNome = tk.Entry(cadastroUsuario, font=fonte)
entradaNome.pack(pady=5)

entradaNome.insert(0, "")
texto= entradaNome.get()
print(texto)

def aplicarNome():
    texto = entradaNome.get()
    nomeUsuario.config(text=texto)

botaoAplicarNome = tk.Button(cadastroUsuario, text="Enviar", command=aplicarNome, font=fonte, bg="violet red", fg="white", relief="flat", cursor="hand2")
botaoAplicarNome.pack(pady=10)
janela.mainloop()