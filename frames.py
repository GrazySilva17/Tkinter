import tkinter as tk

janela = tk.Tk()

janela.title("Minha janela")
janela.geometry("600x400")
janela.configure(bg="light cyan")


frame1 = tk.Frame(janela) #Estilo de janela dentro da aplicação
frame1.configure(width=300, height=200, bg="red", bd=5) #Configurações básicas da janela

frame2 = tk.Frame(frame1) 
frame2.configure(width=100, height=108, bg="blue", bd=5)



frame1.pack()
frame2.pack()

botao = tk.Button(frame1, text="oiii", bg="yellow") #Botão
botao.pack()







janela.mainloop()