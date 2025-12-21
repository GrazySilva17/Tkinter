import tkinter as tk
import pyautogui
import time
janela = tk.Tk() #Cria a janela

janela.title("Primeira janela") #Define o título da janela
janela.geometry("450x550+725+334") #Define o tamanho da janela (verticalxhorizontal). Obs: quando eu coloco o somatório, siginifca que será a posição que a janela vai abrir. São coordenadas de x e y (vertical+horizontal)
janela.minsize(30, 100) #Tamanho mínimo que eu desejo para a janela (vertical, horizontal)
janela.maxsize(480, 550) #Tamanho máximo da janela (vertical, horizontal)
janela.iconbitmap("dedo_para_cima.ico") #Define o icone da janela
janela.configure(bg="navajo white") #Define a cor de fundo da janela
janela.resizable(False, False) #Define se pode ou não mudar o tamanho da janela (vertical, horizontal)
janela.attributes("-alpha", 1) #Nível de transparência do aplicativo, entre 0 e 1. Quanto menor, mais transparente é
janela.mainloop() #Executa a janela