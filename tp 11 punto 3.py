import tkinter as tk  
from tkinter import PhotoImage  
import os  

def ingresar():  
    print("Botón 'Ingresar' presionado.")  
def registrarse():  
    print("Botón 'Registrarse' presionado.")  
root = tk.Tk()  
root.title("Ventana de Inicio")  
root.geometry("400x400")  
image_path = 'C:\Usuarios\totio\Descargas\imagen_colegioo.png'
if os.path.exists(image_path):  
    img = PhotoImage(file=image_path)
    img_label = tk.Label(root, image=img)  
    img_label.pack(pady=20)  
else:  
    print(f"Error: no se pudo encontrar la imagen en la ruta '{image_path}'.")  
btn_ingresar = tk.Button(root, text="Ingresar", command=ingresar)  
btn_ingresar.pack(pady=10)  

btn_registrarse = tk.Button(root, text="Registrarse", command=registrarse)  
btn_registrarse.pack(pady=10)  
root.mainloop()