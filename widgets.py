import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Etiqueta")


etiqueta = tk.Label(janela, text="Olá, sou uma etiqueta")
etiqueta.config(fg="blue", bg="yellow", font=("Arial", 12, "bold"))
etiqueta.pack()
janela.mainloop()