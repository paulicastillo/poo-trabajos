import tkinter as tk
import random as rd
class Adivinanzas:
  def __init__(self, ventana):
    self.__numero_secreto = rd.randint(1, 10)
    self.__posible_numero = tk.Entry(ventana)
    self.__posible_numero.pack(pady = 20)
    self.__boton = tk.Button(ventana, text = "Adivina", command =
self.chequear_adivinanzas)
    self.__boton.pack(pady = 10)
    self.__label = tk.Label(ventana, text = "")
    self.__label.pack(pady = 20)
  def chequear_adivinanzas(self):
      adivinanza = self.__posible_numero.get()
      if adivinanza:
         if int(adivinanza) == self.__numero_secreto:
            self.__label.config(text = "Felicitacines, acertaste el numero")
         else:
            self.__label.config(text = "Ups... vuelve a intentarlo")
ventana = tk.Tk()
ventana.title("Juego de adivinanza")
ventana.geometry("300x200")
juego = Adivinanzas(ventana)
ventana.mainloop()