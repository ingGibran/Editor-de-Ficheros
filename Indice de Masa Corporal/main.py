from tkinter import *
from tkinter import font

def calcular():
    global hayError
    global lbl_error
    try:
        imc = int(ent_peso.get()) / int(ent_altura.get())
        print("Tu IMC es: {}".format(imc))
        hayError = False
        lbl_error.destroy()
        lbl_imc = Label()
    except:
        if not hayError:
            lbl_error = Label(frame_datos, text="Error", fg="red").grid(row=4, column=2)
            hayError = True

# Raíz
root = Tk()
root.title("IMC")
root.resizable(False, False)

hayError = False
lbl_error = Label()
lbl_imc = Label()

# Frame 
frame = Frame(root)
frame.config(width=500, height=100)
frame.pack_propagate(False)
frame.pack()

Label(frame, text="Calcular IMC", font=("Kayak", 30)).pack()

# Frame Datos
frame_datos = Frame(root)
frame_datos.config(width=500, height=300)
frame_datos.pack_propagate(False)
frame_datos.grid_propagate(False)
for i in range(3+1):
    frame_datos.columnconfigure(i, weight=2)
frame_datos.pack()

# Entrys
Label(frame_datos, text="Ingresar Peso", font=("Sequel", 20), justify="right").grid(row=0, column=1)
ent_peso = Entry(frame_datos, width=15)
ent_peso.grid(row=0, column=2)
Label(frame_datos, text="Ingresar Altura", font=("Sequel", 20), justify="right").grid(row=1, column=1)
ent_altura = Entry(frame_datos, width=15)
ent_altura.grid(row=1, column=2)

# Button
Button(frame_datos, text="Calcular", command=lambda : calcular(), width=15, height=3).grid(row=5, column=2)

root.mainloop()