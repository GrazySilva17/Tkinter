import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de botão")

botao = tk.Button(janela, text="Pressione-me, por favor, estou implorando!")
botao.config(fg="#FFFFFF", bg="#000000", font=("Arial", 12, "bold"))
botao.pack()

etiqueta = tk.Label(janela, text="Ainda não fui pressionado.")
etiqueta.pack()
def BotaoPressionado():
    etiqueta.config(text="Obrigado por me pressionar!")

botao.config(command=BotaoPressionado)

janela.mainloop()