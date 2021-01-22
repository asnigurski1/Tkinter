#Artur Snigurski
#KT ÜLESANNE 10

from tkinter import *

#akna seaded
aken = Tk()
aken.title('Kontrolltöö')
aken.iconbitmap('gang1.ico')
aken.geometry("300x300")

#funktsioon
def MIILID():
    summa = float(sisestus.get())
    to_mile = summa / 1.61
    vastus4.config(text=to_mile)
    
#funktsioon2
def KILOMEETRID():
    summa1 = float(sisestus1.get())
    to_km = summa1 * 1.61
    vastus6.config(text=to_km)
#silt
silt = Label(aken, text="Sisesta kilomeetrid:")
silt.grid(row=0,column=0)


#silt2
silt = Label(aken, text="Sisesta miilid:")
silt.grid(row=6,column=0)

#sisestusväli
sisestus = Entry(aken)
sisestus.grid(row=0,column=1)


#sisestuväli2
sisestus1 = Entry(aken)
sisestus1.grid(row=6,column=1)

#nupp
nupp1 = Button(aken, text="Teisenda", width=10, command=MIILID)
nupp1.grid(row=1, column=1)

#nupp2
nupp2 = Button(aken, text="Teisenda", width=10, command=KILOMEETRID)
nupp2.grid(row=7, column=1)

#silt3

vastus3 = Label(aken, text="Miilides :")
vastus3.grid(row=4,column=0)

#silt4
vastus4 = Label(aken, text="  ")
vastus4.grid(row=4, column=1)

#silt5
vastus5 = Label(aken, text="Kilomeetrites :")
vastus5.grid(row=8,column=0)

#silt6
vastus6 = Label(aken, text="  ")
vastus6.grid(row=8, column=1)

aken.mainloop()
