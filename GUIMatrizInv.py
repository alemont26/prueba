from tkinter import*
from tkinter import messagebox

Arreglo = [[0,0,0],[0,0,0],[0,0,0]]
ArregloInv = [[0,0,0],[0,0,0],[0,0,0]]
MI = [[0,0,0],[0,0,0],[0,0,0]]
MIF = [[0,0,0],[0,0,0],[0,0,0]]
ACop1 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

def vaciarENTTXT():
    for fila in Conjunto:
        for col in fila:
            col.delete(0, END)

def MatrizInversa():
    try:
        for i in range(3):
            for j in range(3):
                Arreglo[i][j] = int(Conjunto[i][j].get())
                ArregloInv[j][i] = Arreglo[i][j]
                ACop1[i][j] = ACop1[i+3][j] = ArregloInv[j][i]

        DP1 = DP2 = 0
        for i in range(3):
            DP1 += (ACop1[0 + i][0] * ACop1[1 + i][1] * ACop1[2 + i][2])
            DP2 += (ACop1[0 + i][2] * ACop1[1 + i][1] * ACop1[2 + i][0])
        Determinante = DP1 - DP2

        if Determinante == 0:
            print(DP1, DP2)
            messagebox.showinfo("Resultado", "La Matriz que se ingresó NO tiene matriz inversa.\nDeterminante: " + str(int(Determinante)))
            return
        

        MI[0][0] = (ArregloInv[1][1] * ArregloInv[2][2]) - (ArregloInv[1][2] * ArregloInv[2][1])
        MI[0][1] = -((ArregloInv[1][0] * ArregloInv[2][2]) - (ArregloInv[1][2] * ArregloInv[2][0]))
        MI[0][2] = (ArregloInv[1][0] * ArregloInv[2][1]) - (ArregloInv[1][1] * ArregloInv[2][0])

        MI[1][0] = -((ArregloInv[0][1] * ArregloInv[2][2]) - (ArregloInv[0][2] * ArregloInv[2][1]))
        MI[1][1] = (ArregloInv[0][0] * ArregloInv[2][2]) - (ArregloInv[0][2] * ArregloInv[2][0])
        MI[1][2] = -((ArregloInv[0][0] * ArregloInv[2][1]) - (ArregloInv[0][1] * ArregloInv[2][0]))

        MI[2][0] = (ArregloInv[0][1] * ArregloInv[1][2]) - (ArregloInv[0][2] * ArregloInv[1][1])
        MI[2][1] = -((ArregloInv[0][0] * ArregloInv[1][2]) - (ArregloInv[0][2] * ArregloInv[1][0]))
        MI[2][2] = (ArregloInv[0][0] * ArregloInv[1][1]) - (ArregloInv[0][1] * ArregloInv[1][0])

        for i in range(3):
            for j in range(3):
                MIF[i][j] = round((MI[i][j] / Determinante), 4)


        resultado = "Determinante: " + str(Determinante) + "\n\n"
        resultado += "Las Determinantes Menores son:\n"
        
        for i in range(3):
            for j in range(3):
                resultado += str(MI[i][j]) +"  "
            resultado += "\n"
        resultado += "\nLa Matriz inversa es:\n"

        for i in range(3):
            for j in range(3):
                resultado += str(MIF[i][j]) + "  "
            resultado += "\n"
        messagebox.showinfo("Resultado", resultado)

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores válidos en la matriz.")

def UsoFunciones():
    MatrizInversa()
    vaciarENTTXT()


Raiz = Tk()
Raiz.title("Calculadora de Matriz Invertida")
Raiz.geometry("800x400")
Raiz.config(bg = "black")
Raiz.resizable(False, False)

Frame1 = Frame(Raiz, bg = "black", width=800, height = 200 )
Frame1.place(relx = 0.0, rely = 0.0)

Frame2 = Frame(Raiz)
Frame2.config(bg = "black")

Frame3 = Frame(Raiz, bg = "black", width=800, height = 100)
Frame3.place(relx=0.5, rely=0.9, anchor="center")

Frame4 = Frame(Raiz,  width=50, height = 50)
Frame4.place(relx = 0.85, rely = 0.305, anchor="center")

ImaBorrar = PhotoImage(file="C:\\Users\\WIN10\\Documents\\Archivos Python\\ArchivosDeApoyo\\icons8-eliminar-32.png")

Titulo = Label(Frame1, text="CALCULADORA DE MATRIZ INVERSA", fg = "white", bg = "black", font = ("Segoe UI", 20, "bold"))
Titulo.place(relx = 0.5, rely = 0.27, anchor = "center")

Conjunto = []

for i in range(3):
    subconjunto = []
    for j in range (3):
        EntTXT = Entry(Frame2, width=5, font=("Arial", 30), justify="center")
        EntTXT.grid(row = i, column = j, padx = 15, pady = 15)
        subconjunto.append(EntTXT)
    Conjunto.append(subconjunto)

Frame2.place(relx=0.5, rely=0.5, anchor="center")

BTNCal = Button(Frame3, text= "CALCULAR MATRIZ INVERSA", font = ("Segoe UI", 13, "bold" ), relief="flat", width=39, height=1,bg = "white", command = UsoFunciones)
BTNCal.place(relx=0.5, rely=0.4, anchor="center")

BTNBorrar = Button(Frame4, image = ImaBorrar, command = vaciarENTTXT, relief="flat")
BTNBorrar.place(relx=0.5, rely=0.5, anchor="center", width=50, height=50 )


Raiz.mainloop()