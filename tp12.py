import tkinter as tk  
from tkinter import messagebox  

# Datos de la tabla como una lista de diccionarios  
data = [  
    {  
        "alumno": "Alurralde Portela",  
        "Desde el átomo nro": "1 hidrógeno",  
        "Hasta el átomo nro": "9 flúor",  
        "ejercicios": 1  
    },  
    {  
        "alumno": "Alvarado Lacour",  
        "Desde el átomo nro": "10 neón",  
        "Hasta el átomo nro": "18 argón",  
        "ejercicios": "2 y 3"  
    },  
    {  
        "alumno": "Ángel - Villava",  
        "Desde el átomo nro": "19 potasio",  
        "Hasta el átomo nro": "27 cobalto",  
        "ejercicios": "4 y 5"  
    },  
    {  
        "alumno": "Caseres Guzmán J.",  
        "Desde el átomo nro": "28 níquel",  
        "Hasta el átomo nro": "36 kriptón",  
        "ejercicios": "6 y 7"  
    },  
    {  
        "alumno": "Castillo Salem",  
        "Desde el átomo nro": "37 rubidio",  
        "Hasta el átomo nro": "45 rodio",  
        "ejercicios": "8 y 9"  
    },  
    {  
        "alumno": "Correa - Retamal",  
        "Desde el átomo nro": "46 paladio",  
        "Hasta el átomo nro": "54 xenón",  
        "ejercicios": "10 y 11"  
    },  
    {  
        "alumno": "Día - Lezcano",  
        "Desde el átomo nro": "55 cesio",  
        "Hasta el átomo nro": "63 europio",  
        "ejercicios": "2 y 3"  
    },  
    {  
        "alumno": "Flores - Jaime",  
        "Desde el átomo nro": "64 gadolinio",  
        "Hasta el átomo nro": "72 hafnio",  
        "ejercicios": "4 y 5"  
    },  
    {  
        "alumno": "Gerónimo - Martínez",  
        "Desde el átomo nro": "73 tántalo",  
        "Hasta el átomo nro": "81 talio",  
        "ejercicios": "6 y 7"  
    },  
    {  
        "alumno": "Lazcano - Rosales",  
        "Desde el átomo nro": "82 plomo",  
        "Hasta el átomo nro": "90 torio",  
        "ejercicios": "8 y 9"  
    },  
    {  
        "alumno": "Arenas - Guzmán M.",  
        "Desde el átomo nro": "91 protactinio",  
        "Hasta el átomo nro": "99 einstenio",  
        "ejercicios": 1  
    },  
    {  
        "alumno": "Zalazar - Voltolini - Soto",  
        "Desde el átomo nro": "100 fermio",  
        "Hasta el átomo nro": "118 oganesón",  
        "ejercicios": "10 y 11"  
    }  
]  
def download_images(start, end):  
    messagebox.showinfo("Descargar", f"Descargando imágenes desde el átomo {start} hasta {end}.")  
root = tk.Tk()  
root.title("Descargar imágenes de átomos")  
frame = tk.Frame(root)  
frame.pack(padx=10, pady=10)  
headers = ["Alumnos", "Desde el átomo nro", "Hasta el átomo nro", "Ejercicios"]  
for i, header in enumerate(headers):  
    label = tk.Label(frame, text=header, font=('Arial', 10, 'bold'))  
    label.grid(row=0, column=i)   
for i, item in enumerate(data):  
    tk.Label(frame, text=item["alumno"]).grid(row=i + 1, column=0)  
    tk.Label(frame, text=item["Desde el átomo nro"]).grid(row=i + 1, column=1)  
    tk.Label(frame, text=item["Hasta el átomo nro"]).grid(row=i + 1, column=2)  
    tk.Label(frame, text=item["ejercicios"]).grid(row=i + 1, column=3)   
    button = tk.Button(frame, text="Descargar",   
                       command=lambda start=item["Desde el átomo nro"],   
                       end=item["Hasta el átomo nro"]: download_images(start, end))  
    button.grid(row=i + 1, column=len(headers))  
root.mainloop()