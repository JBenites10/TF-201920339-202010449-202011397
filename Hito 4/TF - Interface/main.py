from doctest import Example
from tkinter import *
from algorithm import *

root = Tk()
root.geometry("800x600")
root.title("Barcelona")


mapping = Canvas(root, width=800, height=450, background="green")

search = Button(root, text="Search", width=10,height=2)
inputSearch = Text(root, height=2, width=70, bg="gray")
inputDestiny = Text(root, height=2, width=70, bg="gray")

scale = 800

x = []
y = []

for i in range(len(lista_lats_lon)):
    if i % 2 == 0:
        x.append(lista_lats_lon[i])
    elif i % 2 != 0:
        y.append(lista_lats_lon[i])

for i in range(len(lista_lats_lon)):
    maximo = max(lista_lats_lon[i])
    minimo = min(lista_lats_lon[i])


x_mayor = maximo[0]
y_mayor = maximo[1]
x_menor = minimo[0]
y_menor = minimo[1]
float(x_mayor)
float(x_menor)
float(y_mayor)
float(y_menor)

# First Version for the connection between nodes
# Doesn't work yet 
#for i in range(len(lista_lats_lon)):
#    mapping.create_oval((x[i]-x_menor)*scale,(y[i]-y_menor)*scale,(x[i]-x_menor)*scale+10,(y[i]-y_menor)*scale+10,outline="#ffffff") 

print(x)

    
search.place(x=10,y=10)
inputSearch.place(x=100,y=15)
inputDestiny.place(x=100,y=60)
mapping.place(x = -2, y = 140)
root.mainloop()