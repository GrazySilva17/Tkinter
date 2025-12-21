import tkinter as tk

janela = tk.Tk()

janela.title("Minha janela")
janela.geometry("600x400")
janela.configure(bg="light cyan")


labelframe = tk.LabelFrame(janela, text="Grupo de widgets", bg="yellow", padx=10, pady=10) #Semelhante ao frame, mas possui titulo próprio
labelframe.configure(width=300, height=200)
labelframe.pack()







janela.mainloop()