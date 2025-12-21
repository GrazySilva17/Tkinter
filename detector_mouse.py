import pyautogui
import time

time.sleep(3) # Dá tempo para mover o mouse
x, y = pyautogui.position() # Pega a posição atual
print(f"Coordenadas: X={x}, Y={y}")
