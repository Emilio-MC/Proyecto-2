import tkinter as tk
from tkinter import *
from tkinter import messagebox



ventana = tk.Tk()
ventana.title("Sistema de reservación de boletos2")
ventana.geometry("300x300")
num = StringVar()

def borrar():
    num.set("")
#Nombre: Acceso del administador
#Salidas: Una vez ingresada la clave lo enviara al menu de opciones administrativas
def accesoAdmin():
    ventana.iconify()
    ventana2 = tk.Toplevel(ventana)
    ventana2.geometry("300x300")
    Mensaje = Label(ventana2,text="Digite la clave de administrador", font = ("Century Schoolbook", 10)).place(x=60, y=30)
    cajaTexto = Entry(ventana2, textvariable=num).place(x=85,y=60)
    boton4 = Button(ventana2, text = "Ingresar", font = ("Century Schoolbook", 10), command = lambda: clave(ventana2)).place(x=110,y=90)
    borrar()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nombre: clave
#Entradas: Ingresar la clave
#Salidas: Una vez ingresada la clave lo enviara al menu de opciones administrativas
def clave(pestaña):
    clave = num.get()
    if(clave != "20032403"):
        num.set("")
        return messagebox.showinfo("Error", message ="clave incorrecta")
    elif(clave == "20032403"):
        pestaña.destroy()
        return MenuAdministrativo()
    elif(clave == ""):
        return messagebox.showinfo("Aviso", message ="La contraseña esta en blanco")
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
#Nombre: Menu de opciones administrativas
#Entradas: Selecciona una de las opciones a mostras 
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
def MenuAdministrativo():
    ventana3 = tk.Toplevel(ventana)
    ventana3.geometry("300x300")
    boton5 = Button(ventana3, text = "Gestión de empresas", font = ("Century Schoolbook", 10),command = lambda: MenuGestionEmpresas()).place(x=80,y=10)
    boton6 = Button(ventana3, text = "Gestión de transporte por empresa", font = ("Century Schoolbook", 10),command = lambda: GestiónTransporte()).place(x=45,y=45)
    boton7 = Button(ventana3, text = "Gestión de viaje", font = ("Century Schoolbook", 10),command = lambda: GestionarViaje()).place(x=85,y=80)
    boton8 = Button(ventana3, text = "Consultar historial de reservaciones", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=35,y=115)
    boton9 = Button(ventana3, text = "Estadísticas de viaje", font = ("Century Schoolbook", 10), command = lambda: Mensaje()).place(x=75,y=150)
    boton10 = Button(ventana3, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana2(ventana3)).place(x=120,y=185)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nombre: Menu de gestion de viajes
#Entradas: Selecciona una de las opciones a mostras 
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada

def GestionarViaje():
    ventana7 = tk.Toplevel(ventana)
    ventana7.geometry("300x300")
    boton25 = Button(ventana7, text = "Incluir Viaje", font = ("Century Schoolbook", 10),command = lambda: IncluirViaje()).place(x=75,y=45)
    boton26 = Button(ventana7, text = "Eliminar Viaje", font = ("Century Schoolbook", 10),command = lambda:Mensaje()).place(x=75,y=80)
    boton27 = Button(ventana7, text = "Ver Viajes", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=120)
    boton28 = Button(ventana7, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana2(ventana7)).place(x=110,y=150)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nombre: Incluir Transporte
#Entradas: Debe ingresar los siguientes parametros placa, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco
#Salidas: Una vez completado se guarda el transporte en el archivo
#Restricciones: La placa debe tener 6 digitos y no se pueden repetir
def IncluirViaje():
    ventana11 = tk.Toplevel(ventana)
    ventana11.geometry("500x500")
    Mensaje = Label(ventana11,text="Digite el numero de viaje", font = ("Century Schoolbook", 10)).place(x=60, y=30)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=50)
    Mensaje = Label(ventana11,text="Digite la provincia y cuidad de salida", font = ("Century Schoolbook", 10)).place(x=30, y=70)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=90)
    Mensaje = Label(ventana11,text="Digite la fecha y hora de llegada", font = ("Century Schoolbook", 10)).place(x=60, y=110)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=130)
    Mensaje = Label(ventana11,text="Digite la provincia y cuidad de llegada", font = ("Century Schoolbook", 10)).place(x=60, y=150)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=170)
    Mensaje = Label(ventana11,text="Digite la fecha y hora de llegada", font = ("Century Schoolbook", 10)).place(x=60, y=190)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=210)
    Mensaje = Label(ventana11,text="Digite la empresa a cargo del viaje", font = ("Century Schoolbook", 10)).place(x=60, y=230)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=260)
    Mensaje = Label(ventana11,text="Digite el transporte que va a usar ", font = ("Century Schoolbook", 10)).place(x=30, y=280)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=310)
    Mensaje = Label(ventana11,text="Digite la cantidad de asientos vip que quiere ", font = ("Century Schoolbook", 10)).place(x=20, y=330)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=350)
    Mensaje = Label(ventana11,text="Digite la cantidad de asientos normales que quiere", font = ("Century Schoolbook", 10)).place(x=20, y=370)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=390)
    Mensaje = Label(ventana11,text="Digite la cantidad de asientos economicos que quiere", font = ("Century Schoolbook", 10)).place(x=20, y=410)
    cajaTexto = Entry(ventana11, textvariable=num).place(x=85,y=430)
    boton37 = Button(ventana11, text = "Ingresar", font = ("Century Schoolbook", 10), command = lambda: Mensaje(ventana10)).place(x=110,y=450)
    

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nombre: Menu de gestion de transportes
#Entradas: Selecciona una de las opciones a mostras
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
def GestiónTransporte():
    ventana6 = tk.Toplevel(ventana)
    ventana6.geometry("300x300")
    boton20 = Button(ventana6, text = "Incluir Transporte", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=80,y=10)
    boton21 = Button(ventana6, text = "Eliminar Transporte", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=45)
    boton22 = Button(ventana6, text = "Modificar Transporte", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=80)
    boton23 = Button(ventana6, text = "Ver Transporte", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=120)
    boton24 = Button(ventana6, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana2(ventana6)).place(x=110,y=150)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nombre: Incluir Transporte
#Entradas: Debe ingresar los siguientes parametros placa,tipo, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco
#Salidas: Una vez completado se guarda el transporte en el archivo
#Restricciones: La placa debe tener 6 digitos y no se pueden repetir
def IncluirTransporte():
    ventana10 = tk.Toplevel(ventana)
    ventana10.geometry("300x500")
    Mensaje = Label(ventana10,text="Digite la placa del transporte", font = ("Century Schoolbook", 10)).place(x=60, y=30)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=50)
    Mensaje = Label(ventana10,text="Digite el tipo del vehiculo; buseta o limosina", font = ("Century Schoolbook", 10)).place(x=30, y=70)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=90)
    Mensaje = Label(ventana10,text="Digite la marca del vehiculo", font = ("Century Schoolbook", 10)).place(x=60, y=110)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=130)
    Mensaje = Label(ventana10,text="Digite el modelo del vehiculo", font = ("Century Schoolbook", 10)).place(x=60, y=150)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=170)
    Mensaje = Label(ventana10,text="Digite el año del vehiculo", font = ("Century Schoolbook", 10)).place(x=60, y=190)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=210)
    Mensaje = Label(ventana10,text="Digite la empresa del vehiculo", font = ("Century Schoolbook", 10)).place(x=60, y=230)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=260)
    Mensaje = Label(ventana10,text="Digite los asientos vip del vehiculo", font = ("Century Schoolbook", 10)).place(x=30, y=280)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=310)
    Mensaje = Label(ventana10,text="Digite los asientos normales del vehiculo", font = ("Century Schoolbook", 10)).place(x=30, y=330)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=350)
    Mensaje = Label(ventana10,text="Digite los asientos economicos del vehiculo", font = ("Century Schoolbook", 10)).place(x=30, y=370)
    cajaTexto = Entry(ventana10, textvariable=num).place(x=85,y=390)
    boton37 = Button(ventana10, text = "Ingresar", font = ("Century Schoolbook", 10), command = lambda: Mensaje(ventana10)).place(x=110,y=410)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nombre: Menu de gestion de empresas
#Entradas: Selecciona una de las opciones a mostras
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
def MenuGestionEmpresas():
    ventana5 = tk.Toplevel(ventana)
    ventana5.geometry("300x300")
    boton15 = Button(ventana5, text = "Incluir Empresas", font = ("Century Schoolbook", 10),command = lambda: IncluirEmpresas()).place(x=80,y=10)
    boton16 = Button(ventana5, text = "Eliminar Empresas", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=45)
    boton17 = Button(ventana5, text = "Modificar Empresas", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=80)
    boton18 = Button(ventana5, text = "Ver Empresas", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=120)
    boton19 = Button(ventana5, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana2(ventana5)).place(x=110,y=150)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Nombre: Incluir Empresas
#Entradas: Debe ingresar los siguientes parametros cedula, nombre, direccion
#Salidas: Una vez completado se guarda la empresa en el archivo
#Restricciones: La cedula debe tener 9 digitos y no se debe repetir cedulas
def IncluirEmpresas():
    ventana9 = tk.Toplevel(ventana)
    ventana9.geometry("300x300")
    Mensaje = Label(ventana9,text="Digite el nombre de la empresa", font = ("Century Schoolbook", 10)).place(x=60, y=30)
    cajaTexto = Entry(ventana9, textvariable=num).place(x=85,y=50)
    Mensaje = Label(ventana9,text="Digite la cedula de la empresa", font = ("Century Schoolbook", 10)).place(x=60, y=70)
    cajaTexto = Entry(ventana9, textvariable=num).place(x=85,y=90)
    Mensaje = Label(ventana9,text="Digite la direccion de la empresa", font = ("Century Schoolbook", 10)).place(x=60, y=110)
    cajaTexto = Entry(ventana9, textvariable=num).place(x=85,y=130)
    boton36 = Button(ventana9, text = "Ingresar", font = ("Century Schoolbook", 10), command = lambda: Mensaje(ventana9)).place(x=110,y=170)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#Nombre: Menu de opciones generales
#Entradas: Selecciona una de las opciones a mostras 
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
def MenuOpcionesGenerales():
    ventana.iconify()
    ventana4 = tk.Toplevel(ventana)
    ventana4.geometry("300x300")
    boton11 = Button(ventana4, text = "Consulta de viajes", font = ("Century Schoolbook", 10),command = lambda: MenuConsultaViajes()).place(x=80,y=10)
    boton12 = Button(ventana4, text = "Reservación de viaje", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=45)
    boton13 = Button(ventana4, text = "Cancelación de reservación ", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=50,y=80)
    boton14 = Button(ventana4, text = "Salir", font = ("Century Schoolbook", 10),command = lambda: CerrarVentana2(ventana4)).place(x=110,y=150)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 #Nombre: Menu de Consulta de Viajes
#Entradas: Selecciona una de las opciones a mostras 
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
def MenuConsultaViajes():
    ventana8 = tk.Toplevel(ventana)
    ventana8.geometry("300x300")
    boton29 = Button(ventana8, text = "Consulta de viajes", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=80,y=10)
    boton30 = Button(ventana8, text = "Buscar viaje por empresa", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=50,y=45)
    boton31 = Button(ventana8, text = "Buscar viaje por lugar de salida", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=80)
    boton32 = Button(ventana8, text = "Buscar viaje por lugar de llegada", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=35,y=115)
    boton33 = Button(ventana8, text = "Buscar viaje por fecha de salida", font = ("Century Schoolbook", 10), command = lambda: Mensaje()).place(x=75,y=150)
    boton34 = Button(ventana8, text = "Buscar viaje por fecha de llegada", font = ("Century Schoolbook", 10), command = lambda: Mensaje(ventana8)).place(x=80,y=180)
    boton35 = Button(ventana8, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana2(ventana8)).place(x=160,y=210)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    
    
def Mensaje():
    messagebox.showinfo("Aviso", message ="Esta función aun esta en construcción")
    

        
def CerrarVentana(pestaña):
    pestaña.destroy()

def CerrarVentana2(pestaña):
    ventana.deiconify()
    pestaña.destroy()   
    
    
#Nombre: Reservacion de boletos
#Entradas: Selecciona una de las opciones a mostras 
#Salidas: A la hora de seleccionar una de las opciones te va a mandar a otro menu
boton1 = Button(ventana, text = "Opciones administrativas", font = ("Century Schoolbook", 10), command = lambda: accesoAdmin()).place(x=60,y=30)
boton2 = Button(ventana, text = "Opciones de usuario normal", font = ("Century Schoolbook", 10), command = lambda: MenuOpcionesGenerales()).place(x=55,y=60)
boton3 = Button(ventana, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana(ventana)).place(x=120,y=90)

ventana.mainloop()
#------------------------------------------------------------------------------------------------

