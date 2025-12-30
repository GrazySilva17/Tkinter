import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de entrada")

etiqueta = tk.Label(janela, text="Em busca de um sonho...")
etiqueta.pack()

entrada = tk.Entry(janela)
entrada.config(fg="#0000FF", bg="#FFFF00", font=("Verdana", 14))
entrada.pack()

entrada.insert(0, "Nome")
texto = entrada.get()
print(texto)

def aplicarTexto():
    texto = entrada.get()
    etiqueta.config(text=texto)

botaoAplicar = tk.Button(janela, text="Aplicar texto", command=aplicarTexto)
botaoAplicar.pack()
janela.mainloop()