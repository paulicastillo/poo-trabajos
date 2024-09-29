import tkinter as tk
ventana = tk.Tk()  
ventana.title("Primera Ventana con Tkinter")  
etiqueta_integrantes = tk.Label(ventana, text="Integrantes del trabajo: Castillo Paulina, Salem Mahia")  
etiqueta_integrantes.pack()  
etiqueta_info = tk.Label(ventana, text="Curso: 5° D, Materia: Programación, Colegio: Divina Misericordia")  
etiqueta_info.pack()  
ventana.mainloop()