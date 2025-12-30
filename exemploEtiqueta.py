import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo de etiqueta")

etiqueta = tk.Label(janela, text="Olá, eu sou uma linda etiqueta")
etiqueta.config(fg="#EA25C3", bg="#D4A7FF", font=("Helvetica", 16, "italic"))
etiqueta.pack()

#Função para atualizar o texto da etiqueta a cada segundo
def AtualizarHora():
    from datetime import datetime
    etiqueta.config(text=datetime.now().strftime("%H:%M:%S")) # Atualiza o texto da etiqueta com a hora atual
    etiqueta.after(1000, AtualizarHora)

AtualizarHora()
janela.mainloop()