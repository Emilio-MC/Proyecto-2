import tkinter as tk
from tkinter import *
from tkinter import messagebox



ventana = tk.Tk()
ventana.title("Sistema de reservación de boletos2")
ventana.geometry("300x300")
num = StringVar()

def borrar():
    num.set("")

def accesoAdmin():
    ventana.iconify()
    ventana2 = tk.Toplevel(ventana)
    ventana2.geometry("300x300")
    Mensaje = Label(ventana2,text="Digite la clave de administrador", font = ("Century Schoolbook", 10)).place(x=60, y=30)
    cajaTexto = Entry(ventana2, textvariable=num).place(x=85,y=60)
    boton4 = Button(ventana2, text = "Ingresar", font = ("Century Schoolbook", 10), command = lambda: administrador(ventana2)).place(x=110,y=90)
    borrar()
    
def administrador(pestaña):
    clave = num.get()
    if(clave != "2626"):
        num.set("")
        return messagebox.showinfo("Error", message ="clave incorrecta")
    elif(clave == "2626"):
        pestaña.destroy()
        return MenuAdministrador()
    elif(clave == ""):
        return messagebox.showinfo("Aviso", message ="La contraseña esta en blanco")
        

def MenuAdministrador():
    ventana3 = tk.Toplevel(ventana)
    ventana3.geometry("300x300")
    boton5 = Button(ventana3, text = "Gestión de empresas", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=80,y=10)
    boton6 = Button(ventana3, text = "Gestión de transporte por empresa", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=45,y=45)
    boton7 = Button(ventana3, text = "Gestión de viaje", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=85,y=80)
    boton8 = Button(ventana3, text = "Consultar historial de reservaciones", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=35,y=115)
    boton9 = Button(ventana3, text = "Estadísticas de viaje", font = ("Century Schoolbook", 10), command = lambda: Mensaje()).place(x=75,y=150)
    boton10 = Button(ventana3, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana2(ventana3)).place(x=120,y=185)

def MenuUsuario():
    ventana.iconify()
    ventana4 = tk.Toplevel(ventana)
    ventana4.geometry("300x300")
    boton11 = Button(ventana4, text = "Consulta de viajes", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=80,y=10)
    boton12 = Button(ventana4, text = "Reservación de viaje", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=75,y=45)
    boton13 = Button(ventana4, text = "Cancelación de reservación ", font = ("Century Schoolbook", 10),command = lambda: Mensaje()).place(x=50,y=80)
    boton14 = Button(ventana4, text = "Salir", font = ("Century Schoolbook", 10),command = lambda: CerrarVentana2(ventana4)).place(x=110,y=150)

    
    
    
    
def Mensaje():
    messagebox.showinfo("Aviso", message ="Esta función aun esta en construcción")
    

        
def CerrarVentana(pestaña):
    pestaña.destroy()

def CerrarVentana2(pestaña):
    ventana.deiconify()
    pestaña.destroy()   
    
    


boton1 = Button(ventana, text = "Opciones administrativas", font = ("Century Schoolbook", 10), command = lambda: accesoAdmin()).place(x=60,y=30)
boton2 = Button(ventana, text = "Opciones de usuario normal", font = ("Century Schoolbook", 10), command = lambda: MenuUsuario()).place(x=55,y=60)
boton3 = Button(ventana, text = "Salir", font = ("Century Schoolbook", 10), command = lambda: CerrarVentana(ventana)).place(x=120,y=90)

ventana.mainloop()
#------------------------------------------------------------------------------------------------
#Nombre: Consultar Viajes
#Salidas: Retorna todas los viajes ya ingresados
def ConsultaViajes():
    f = open ("viajes.txt",'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()         
     
#--------------------------------------------------------------------------------------------
#Nombre: Buscar por empresa
#Entradas: Buscar viaje por el nombre de la empresa
#Salidas: Los viajes que tiene esa empresa
#Restricciones: No debe permitir valores en blanco y debe ingresar una empresa ya antes ingresada
def BuscarEmpresa():
    contactos = "viajes.txt"
    nombre = input("Digite el nombre de la empresa: ")
    NumeroLinea = 0
    if(nombre == ""):
        return print("El nombre no puede estar en blanco")
    with open("viajes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                return BuscarNombre_aux(NumeroLinea)

        else:

            return print("El nombre no fue encontrado")
        
def BuscarNombre_aux(NumeroLinea):
    with open("viajes.txt") as f:
        data = f.readlines()[NumeroLinea-1]     
    print(data)
#------------------------------------------------------------------------------------------------------------------
#Nombre: Buscar por fecha de salida
#Entradas: Buscar viaje por el lugar de salida
#Salidas: Los viajes que tienen el mismo lugar de salida
#Restricciones: No debe permitir valores en blanco y debe ingresar una fecha ya antes ingresada
def BuscarLugarSalida():
    contactos = "viajes.txt"
    nombre = input("Digite el lugar de salida: ")
    NumeroLinea = 0
    if(nombre == ""):
        return print("El lugar de salida no puede estar en blanco")
    with open("viajes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                return BuscarSalida_aux(NumeroLinea)

        else:

            return print("El lugar no fue encontrado")
        
def BuscarSalida_aux(NumeroLinea):
    with open("viajes.txt") as f:
        data = f.readlines()[NumeroLinea-1]     
    print(data)
#----------------------------------------------------------------------------------------------
#Nombre: Buscar por fecha de llegada
#Entradas: Buscar viaje por el lugar de llegada
#Salidas: Los viajes que tienen el mismo lugar de llegada
#Restricciones: No debe permitir valores en blanco y debe ingresar una fecha ya antes ingresada
def BuscarLugarLlegada():
    contactos = "viajes.txt"
    nombre = input("Digite el lugar de llegada: ")
    NumeroLinea = 0
    if(nombre == ""):
        return print("El lugar de llegada no puede estar en blanco")
    with open("viajes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                return BuscarLlegada_aux(NumeroLinea)

        else:

            return print("El lugar no fue encontrado")
        
def BuscarLlegada_aux(NumeroLinea):
    with open("viajes.txt") as f:
        data = f.readlines()[NumeroLinea-1]     
    print(data)
#---------------------------------------------------------------------------------------------
#Nombre: Buscar por fecha de salida
#Entradas: Buscar viaje por la fecha de salida
#Salidas: Los viajes que tiene la misma fecha de salida
#Restricciones: No debe permitir valores en blanco y debe ingresar una fecha ya antes ingresada
def BuscarFechaSalida():
    contactos = "viajes.txt"
    nombre = input("Digite la fecha de salida: ")
    NumeroLinea = 0
    if(nombre == ""):
        return print("La fecha no puede estar en blanco")
    with open("viajes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                return BuscarFechaSalida_aux(NumeroLinea)

        else:

            return print("La fecha no fue encontrado")
        
def BuscarFechaSalida_aux(NumeroLinea):
    with open("viajes.txt") as f:
        data = f.readlines()[NumeroLinea-1]     
    print(data)
#----------------------------------------------------------------------------------------------
#Nombre: Buscar por fecha de llegada
#Entradas: Buscar viaje por la fecha de llegada
#Salidas: Los viajes que tiene la misma fecha de llegada
#Restricciones: No debe permitir valores en blanco y debe ingresar una fecha ya antes ingresada
def BuscarFechaSalida():
    contactos = "viajes.txt"
    nombre = input("Digite la fecha de llegada: ")
    NumeroLinea = 0
    if(nombre == ""):
        return print("La fecha no puede estar en blanco")
    with open("viajes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                return BuscarFechaLlegada_aux(NumeroLinea)

        else:

            return print("La fecha no fue encontrado")
        
def BuscarFechaLlegada_aux(NumeroLinea):
    with open("viajes.txt") as f:
        data = f.readlines()[NumeroLinea-1]     
    print(data)
#-----------------------------------------------------------------------------------------------
#Nombre: Menu de Consulta de Viajes
#Entradas: Selecciona una de las opciones a mostras con los signos solicitados
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
#Restricciones: Solo puede poner los signos que se le solicitan
def MenuConsultaViajes():
     print ("(%)  Consulta de viajes")
     
     print ("(&)  Buscar viaje por empresa")

     print ("(//)  Buscar viaje por lugar de salida")

     print ("(?)  Buscar viaje por lugar de llegada")

     print ("(¿)  Buscar viaje por fecha de salida")

     print ("(¡)  Buscar viaje por fecha de llegada")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='%'):
              return ConsultaViajes()
            
          elif (opcion=='&'):
              return BuscarEmpresa()
                           
          elif (opcion=='//'):
              return BuscarLugarSalida()
          
          elif (opcion=='?'):
              return BuscarLugarLlegada()

          elif (opcion=='¿'):
              return BuscarFechaSalida()

          elif (opcion=='¡'):
              return BuscarFechaLlegada()
          
          
          else:
               print("Error, opcion incorrecta")

            
#----------------------------------------------------------------------------------------------
#Nombre: Menu de opciones generales
#Entradas: Selecciona una de las opciones a mostras con los signos solicitados
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
#Restricciones: Solo puede poner los signos que se le solicitan
def OpcionesGenerales():
     print ("(/)  Consulta de viajes")
     
     print ("(*)  Reservación de viaje")

     print ("(=)  Cancelación de reservación")

     print ("(F)  Atras")

     print ("(3)  Salir")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='/'):
              return MenuConsultaViajes()
            
          elif (opcion=='*'):
              return ReservaciónViaje()
                           
          elif (opcion=='='):
              return CancelaciónRervación()
          
          elif (opcion=='F'):
              return OpcionesAdministrativas()
            
                           
          elif (opcion=='3'):
              return print("Hasta luego")
          
          else:
               print("Error, opcion incorrecta")
#-------------------------------------------------------------------------------------------------
#Nombre: Incluir Empresas
#Entradas: Debe ingresar los siguientes parametros cedula, nombre, direccion
#Salidas: Una vez completado se guarda la empresa en el archivo
#Restricciones: La cedula debe tener 9 digitos y no se debe repetir cedulas
def IncluirEmpresas():
    if(0==0):
                pass
    print("Debe de tener 9 digitos")
    cedula = (input("Ingrese la cedula: "))
    contador = len(str(cedula))
    contador = str(contador)
    nombre = input("Ingrese el nombre: ")
    Direccion = input("Ubicación de la empresa: ")
    proyecto = "gestionEmpresa.txt"

    anexarContenidoArchivoEmpresas(proyecto, cedula, nombre, Direccion, contador)

def anexarContenidoArchivoEmpresas(proyecto, cedula, nombre, Direccion, contador):
    f = open (proyecto,'a')
    if(contador<"9"):
         return print("La cedula no puede tener menos de 9 digitos")
    elif(contador>"9"):
         return print("La cedula no puede tener más de 9 digitos")
    elif(0==0):
         return ContinuarIncluirEmpresa(proyecto, cedula, nombre, Direccion, contador)

def ContinuarIncluirEmpresa(proyecto, cedula, nombre, Direccion, contador):
        if(0==0):
                f = open (proyecto,'a')

                unregistro = cedula + "," + nombre + ',' + Direccion + '\n'
                f.write(unregistro)
                f.close()
                print("Guardado con exito en gestionEmpresa.txt")
#-----------------------------------------------------------------------------------------------
#Nombre: Eliminar Empresas
#Entradas: Debe de ingresar el nombre de la empresa
#Salidas: La empresa se habra borrado con exito de archvo
#Restricciones: Debe poner un nombre de una empresa ya antes creada, no puede dejar espacios en blanco
def EliminarEmpresas():
    proyecto = "gestionEmpresa.txt"
    nombre = input("Digite el nombre: ")
    NumeroLinea = 0
    with open("gestionEmpresa.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(nombre)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return EliminarEmpresas_aux(NumeroLinea)
        else:
            return print("No existe empresa con el nombre que pusiste")
            
def EliminarEmpresas_aux(NumeroLinea):
    initial_line = 1
    file_lines = {}
    with open("gestionEmpresa.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("gestionEmpresa.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    print("Empresa eliminada con exito")
#-----------------------------------------------------------------------------------------------
#Nombre: iniciar Modificar Empresas
#Esta funcion mas que todo es un complemento de la de modificar empresas
def iniciarModificarEmpresas(cedula):
    if(0==0):
        pass 
    contador = len(str(cedula))
    contador = str(contador)
    nombre = input("Ingrese el nombre: ")
    Contador = str(Contador)
    Direccion = input("Ubicación de la empresa: ")
    proyecto = "gestionEmpresa.txt"

    ContinuarModificarEmpresa(proyecto, cedula, nombre, Direccion ,contador, Contador)
                

def ContinuarModificarEmpresa(proyecto, nombre, Direccion ,contador, Contador):
    if(0==0):
        f = open (proyecto,'a')

        unregistro =cedula + "," + nombre + ',' + Direccion + '\n'
        f.write(unregistro)
        f.close()
        print("Modificado con exito en gestionEmpresa.txt")
#-------------------------------------------------------------------------------------------------
#Nombre: Modificar Empresas
#Entradas: Ingresar el nombre de la empresa a modificar
#Salidas: La empresa a buscar encontrada y lista para modificar
#Restricciones: Nose puede dejar espacios en blanco, debe ingresar el nombre de la empresa ya ingresado con anterioridad
def ModificarEmpresas():
    print("Recordatorio: Si al modificar un empresa y falla al modificarlo, su empresa sera eliminada y debera ingresarla de nuevo en incluir empresa")
    proyecto = "gestionEmpresa.txt"
    nombre = input("Digite la cedula de la empresa: ")
    NumeroLinea = 0
    with open("gestionEmpresa.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(cedula)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return ModificarEmpresas_aux(NumeroLinea, cedula)
        else:
            return print("Cedula no encontrado")
            
def ModificarEmpresas_aux(NumeroLinea,cedula):
    initial_line = 1
    file_lines = {}
    with open("gestionEmpresa.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("gestionEmpresa.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    return iniciarModificarEmpresas(cedula)
#----------------------------------------------------------------------------------------------
#Nombre: Ver Empresas
#Salidas: Retorna todas las empresas ya ingresadas
def VerEmpresas():
    f = open ("gestionEmpresa.txt",'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()
#-----------------------------------------------------------------------------------------------
#Nombre: Menu de gestion de empresas
#Entradas: Selecciona una de las opciones a mostras con las letras solicitadas
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
#Restricciones: Solo puede poner las letras que se le solicitan
def GestiónEmpresas():
     print ("(G)  Incluir Empresas")
     
     print ("(H)  Eliminar Empresas")

     print ("(I)  Modificar Empresas")

     print ("(J)  Ver Empresas")

     print ("(F)  Atras")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='G'):
              return IncluirEmpresas()
            
          elif (opcion=='H'):
              return EliminarEmpresas()
            
            
          elif (opcion=='I'):
              return ModificarEmpresas()
            
                           
          elif (opcion=='J'):
              return VerEmpresas()

          elif (opcion=='F'):
               return OpcionesAdministrativas()
            
#--------------------------------------------------------------------------------------------------
#Nombre: Incluir Transporte
#Entradas: Debe ingresar los siguientes parametros placa, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco
#Salidas: Una vez completado se guarda el transporte en el archivo
#Restricciones: La placa debe tener 6 digitos y no se pueden repetir
def IncluirTransporte():
    if(0==0):
                pass
    print("Debe de tener 6 digitos y no puede haber 2 placas iguales")
    placa = (input("Ingrese la placa: "))
    contador = len(str(placa))
    contador = str(contador)
    print("Los tipos de vehiculos son busetas y/o limosinas")
    Tipo = input("Ingrese el tipo de vehiculo: ")
    Contador = len (str(Tipo))
    Contador = str(Contador)
    marca = input("Ingrese el marca: ")
    CONTADOR = len (str(marca))
    CONTADOR = str(CONTADOR)
    modelo = input("Ingrese el modelo del vehiculo: ")
    año = input("Ingrese el año del vehiculo:")
    print("El vehiculo debe de ser de las empresas ingresadas anteriormente")
    empresa = input("A que emprese pertenece el vehiculo:")
    asientosvip = input("Cantidad de asientos de clase vip: ")
    asientosnormales = input("Cantidad de asientos normales: ")
    asientoseco = input("Cantidad de asientos de clase económica: ")
    proyecto = "transportes.txt"

    anexarContenidoArchivoTransporte(proyecto, placa,Tipo, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador,CONTADOR, Contador)

def anexarContenidoArchivoTransporte(proyecto, placa,Tipo, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador,CONTADOR, Contador):
        f = open (proyecto,'a')
        if(contador<"6"):
                return print("La placa no puede tener menos de 6 digitos")
        elif(contador>"6"):
                return print("La placa no puede tener más de 6 digitos")
        elif(0==0):
                return ContinuarIncluirTransporte(proyecto, placa,Tipo, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador,CONTADOR, Contador)

def ContinuarIncluirTransporte(proyecto, placa,Tipo, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador,CONTADOR, Contador):
        if(0==0):
                f = open (proyecto,'a')

                unregistro = placa + "," + marca + ',' + Tipo + ',' + modelo + ','+ año + ','+ empresa + ','+ asientosvip + ','+ asientosnormales + ','+ asientoseco +'\n'
                f.write(unregistro)
                f.close()
                print("Guardado con exito en transportes.txt")
#---------------------------------------------------------------------------------------------------
#Nombre: Eliminar Transporte
#Entradas: Debe de ingresar la placa de un vehiculo antes ingresado
#Salidas: El transporte se habra borrado con exito de archvo
#Restricciones: Debe poner una placa ya antes creada, no puede dejar espacios en blanco
def EliminarTransporte():
    proyecto = "transportes.txt"
    placa = input("Digite la placa: ")
    NumeroLinea = 0
    with open("transportes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(placa)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return EliminarTransporte_aux(NumeroLinea)
        else:
            return print("Numero de placa no encontrado")
            
def EliminarTransporte_aux(NumeroLinea):
    initial_line = 1
    file_lines = {}
    with open("transportes.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("transportes.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    print("Transporte eliminado con exito")
#---------------------------------------------------------------------------------------------------
#Nombre: iniciar Modificar Transporte
#Esta funcion mas que todo es un complemento de la de modificar transporte
def iniciaModificarTransporte(placa):
    if(0==0):
        pass 
    contador = len(str(placa))
    contador = str(contador)
    Tipo = input("Ingrese el tipo: ")
    CONTADOR = len (str(Tipo))
    CONTADOR = str(CONTADOR)
    modelo = input("Ingrese el modelo: ")
    Contador = len (str(modelo))
    Contador = str(Contador)
    modelo = input("Ingrese el modelo del vehiculo: ")
    año = input("Ingrese el año del vehiculo:")
    print("El vehiculo debe de ser de las empresas ingresadas anteriormente")
    empresa = input("A que empresa pertenece el vehiculo:")
    asientosvip = input("Cantidad de asientos de clase vip: ")
    asientosnormales = input("Cantidad de asientos normales: ")
    asientoseco = input("Cantidad de asientos de clase económica: ")
    proyecto = "transportes.txt"

    ContinuarModificarTransporte(proyecto, placa,Tipo, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador, CONTADOR, Contador)


def ContinuarModificarTransporte(proyecto, placa,Tipo, modelo, año, empresa, asientosvip, asientosnormales, asientoseco, contador, CONTADOR, Contador):
        if(0==0):
                f = open (proyecto,'a')

                unregistro = placa + "," + marca + ',' + Tipo + ',' + modelo + ','+ año + ','+ empresa + ','+ asientosvip + ','+ asientosnormales + ','+ asientoseco +'\n'
                f.write(unregistro)
                f.close()
                print("Guardado con exito en transportes.txt")
#-------------------------------------------------------------------------------------------------
#Nombre: Modificar Transporte
#Entradas: Ingresar la placa del transporte a modificar
#Salidas: El transporte a buscar encontrada y lista para modificar
#Restricciones: Nose puede dejar espacios en blanco, debe ingresar la placa del transporte ya ingresado con anterioridad
def ModificarTransporte():
    print("Recordatorio: Si al modificar un transpote y falla al modificarlo, su empresa sera eliminada y debera ingresarla de nuevo en incluir empresa")
    proyecto = "transportes.txt"
    placa = input("Digite la placa del vehiculo: ")
    NumeroLinea = 0
    with open("transportes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(placa)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return ModificarTransporte_aux(NumeroLinea, placa)
        else:
            return print("Nombre no encontrado")
            
def ModificarTransporte_aux(NumeroLinea,placa):
    initial_line = 1
    file_lines = {}
    with open("transportes.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("transportes.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    return iniciaModificarTransporte(placa)
#--------------------------------------------------------------------------------------------------
#Nombre: Ver Transporte
#Salidas: Retorna todas los transportes ya ingresados
def VerTransporte():
    f = open ("transportes.txt",'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()
    
#---------------------------------------------------------------------------------------------------
#Nombre: Menu de gestion de transportes
#Entradas: Selecciona una de las opciones a mostras con las letras solicitadas
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
#Restricciones: Solo puede poner las letras que se le solicitan
def GestiónTransporteEmpresas():
     print ("(K)  Incluir Transporte")
     
     print ("(L)  Eliminar Transporte")

     print ("(M)  Modificar Transporte")

     print ("(N)  Ver Transporte")

     print ("(F)  Atras")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='K'):
              return IncluirTransporte()
            
          elif (opcion=='L'):
              return EliminarTransporte()
            
            
          elif (opcion=='M'):
              return ModificarTransporte()
            
                           
          elif (opcion=='N'):
              return VerTransporte()

          elif (opcion=='F'):
               return OpcionesAdministrativas()
#---------------------------------------------------------------------------------------------
#Nombre: Incluir Transporte
#Entradas: Debe ingresar los siguientes parametros placa, marca, modelo, año, empresa, asientosvip, asientosnormales, asientoseco
#Salidas: Una vez completado se guarda el transporte en el archivo
#Restricciones: La placa debe tener 6 digitos y no se pueden repetir
def IncluirViaje():
    if(0==0):
                pass
    import random

    for i in range(5):
         print(random.uniform(100,1000))
    print("De los numeros anteriores ingrese uno como numero de viaje")
    numeroviaje=(input("Ingrese un numero de viaje"))
    CONTADOR= len(str(numeroviaje))
    CONTADOR = str(CONTADOR)
    Cuidadsalida = (input("Ingrese la provincia y cuidad de salida: "))
    Contador = len(str(Cuidadsalida))
    Contador = str(Contador)
    Fechahorasalida = input("Ingrese la fecha y la hora de salida:  , ")
    conTador= len(str(Fechahorasalida))
    conTador = str(conTador)
    Cuidadllegada = input("Ingrese la provincia y cuidad de llegada:")
    ContaDor = len(str(Cuidadllegada))
    ContaDor = str(ContaDor)
    Fechahorallegada = input("Ingrese la fecha y hora de llegada:  , ")
    contador = len(str(Fechahorallegada))
    contador = str(contador)
    print("La empresa debe de ser de las ingresadas anteriormente ")
    empresa = input("Ingrese la empresa encargada de su viaje: ")
    print("El transporte debe de ser de los ingresados anteriormente")
    transporte = input("Ingrese el transporte: ")
    print("El monto del asiento clase vip es de 15.000 colones")
    asientosvip = input("Cantidad de asientos de clase vip: ")
    print("El monto del asiento clase normal es de 5.000 colones")
    asientosnormales = input("Cantidad de asientos normales: ")
    print("El monto del asiento clase económica es de 2.000 colones")
    asientoseco = input("Cantidad de asientos de clase económica: ")
    proyecto = "viajes.txt"

    ContinuarIncluirViaje(proyecto, numeroviaje, Cuidadsalida, Fechahorasalida, Cuidadllegada, Fechahorallegada, empresa, transporte, asientosvip, asientosnormales, asientoseco, CONTADOR,Contador, conTador,ContaDor,contador)

def ContinuarIncluirViaje(proyecto, numeroviaje, Cuidadsalida, Fechahorasalida, Cuidadllegada, Fechahorallegada, empresa, transporte, asientosvip, asientosnormales, asientoseco, CONTADOR,Contador, conTador,ContaDor,contador):
        if(0==0):
                f = open (proyecto,'a')

                unregistro = numeroviaje + ',' + Cuidadsalida + "," + Fechahorasalida + ',' + Cuidadllegada + ','+ Fechahorallegada + ','+ empresa + ',' + transporte + ','+ asientosvip+ ','+ asientosnormales + ','+ asientoseco +'\n'
                f.write(unregistro)
                f.close()
                print("Guardado con exito en viajes.txt")          
#-----------------------------------------------------------------------------------------------
#Nombre: Eliminar Viaje
#Entradas: Debe de ingresar el numero de viaje antes dado
#Salidas: El viaje se habra borrado con exito de archvo
#Restricciones: Debe ingresar el numeroya antes dado, no puede dejar espacios en blanco
def EliminarViaje():
    proyecto = "viajes.txt"
    numero = input("Digite el numero de viaje: ")
    NumeroLinea = 0
    with open("viajes.txt", "r") as ObjFichero:
        for line in ObjFichero:
            NumeroLinea = NumeroLinea + 1
            PosicionTexto = line.find(numero)
            if PosicionTexto >= 0:
                NumeroLinea = int(NumeroLinea)
                return EliminarViaje_aux(NumeroLinea)
        else:
            return print("Numero de viaje no encontrado")
            
def EliminarViaje_aux(NumeroLinea):
    initial_line = 1
    file_lines = {}
    with open("viajes.txt") as f:
        content = f.readlines()
    for line in content:
        file_lines[initial_line] = line.strip()
        initial_line += 1
    f = open("viajes.txt", "w")
    for line_number, line_content in file_lines.items():
        if line_number != NumeroLinea:
            f.write('{}\n'.format(line_content))
    f.close()
    print("Viaje eliminado con exito")
#------------------------------------------------------------------------------------------------
#Nombre: Ver Viajes
#Salidas: Retorna todas los viajes ya ingresados
def VerViajes():
    f = open ("viajes.txt",'r')
    for mensaje in f.readlines():
        print(mensaje)
    f.close()           
#--------------------------------------------------------------------------------------------------
#Nombre: Menu de gestion de viajes
#Entradas: Selecciona una de las opciones a mostras con las letras solicitadas
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
#Restricciones: Solo puede poner las letras que se le solicitan
def GestionarViaje():
     print ("(Ñ)  Incluir Viaje")
     
     print ("(O)  Eliminar Viaje")

     print ("(P)  Ver Viajes")

     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='Ñ'):
              return IncluirViaje()
            
          elif (opcion=='O'):
              return EliminarViaje()
                            
          elif (opcion=='P'):
              return VerViajes()
#--------------------------------------------------------------------------------------------------
#Nombre: Menu de opciones administrativas
#Entradas: Selecciona una de las opciones a mostras con las letras solicitadas
#Salidas: A la hora de seleccionar una de las opciones lo va a enviar a la opcion solicitada
#Restricciones: Solo puede poner las letras que se le solicitan
def OpcionesAdministrativas():
     print ("(A)  Gestión de empresas")
     
     print ("(B)  Gestión de transporte por empresa")

     print ("(C)  Gestión de viaje")

     print ("(D)  Consultar historial de reservaciones")

     print ("(E)  Estadísticas de viaje")

     print ("(F)  Atras")

    
     opcion = input("Cual opcion selecciona: ")
     if isinstance(opcion,str):
          if (opcion=='A'):
              return GestiónEmpresas()
            
          elif (opcion=='B'):
              return GestiónTransporteEmpresas()
            
            
          elif (opcion=='C'):
              return GestionarViaje()
            
                           
          elif (opcion=='D'):
              return ConsultarHistorialReservaciones()
          
          elif (opcion=='E'):
              return EstadísticasViaje()
            
                           
          elif (opcion=='F'):
              return reservacionBoletos()
          
          else:
               print("Error, opcion incorrecta")

          print("\n")
          reservacionBoletos()  


#----------------------------------------------------------------------------------------------------------------
#Nombre: clave
#Entradas: Ingresar la clave de invitados
#Salidas: Una vez ingresada la clave lo enviara al menu de opciones administrativas
#Restricciones: Solo puede ingresar la clave de invitados
def clave():
     print("La clave de acceso para invitados es 2003070324")

     if(0==0):
                pass     
     clave = input("Ingrese la clave : ")
     proyecto = "claves.txt"

     anexarclave(proyecto,clave)

def anexarclave(proyecto,clave):
    f = open ('claves.txt','r')
    if (clave==''):
        print ("Error: ingrese una clave")
    for mensaje in f.readlines():
        return OpcionesAdministrativas()   
    f.close()    
#--------------------------------------------------------------------------------------------------------------
#Nombre: Reservacion de boletos
#Entradas: Selecciona una de las opciones a mostras con los numeros que le solicitan
#Salidas: A la hora de seleccionar una de las opciones te va a mandar a otro menu
#Restricciones: Solo puede poner los numeros que se le solicitan
def reservacionBoletos():
    print ("Seleccione una de las opciones a mostrar")
    print ("(1)    Opciones administrativas")
    print ("(2)    Opciones de usuario normal")
    print ("\n")
    print ("(3)     Salir")
    opcion = input("\nCual opcion selecciona: ")

    if (opcion=='3'):
            return print("Hasta luego")

    if (isinstance(opcion,str)):
           if(opcion=='1'):
                    clave()
            
           elif(opcion=='2'):
                   OpcionesGenerales()
            
           else:
               print("Error, opcion incorrecta")


    print("\n")
    reservacionBoletos()         

      
reservacionBoletos()
