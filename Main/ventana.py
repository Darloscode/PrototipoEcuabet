from distutils.dist import command_re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk 
from sql import *
from tkinter import Toplevel, Label, Entry, Button


class Ventana(Frame):
    
    datos = Base()

    def __init__(self, master=None):
        super().__init__(master,width=900, height=460)
        self.master = master
        self.pack()
        self.create_widgets()      
        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8","col9","col10"))
        self.btnEliminar = Button(self, text="", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnEditar = Button(self, text="", command = self.editarCliente, bg="#bfdaff", fg="black")
        self.btnAgregar = Button(self, text="", command = self.mostrarVentanaAgregarCliente, bg="#bfdaff", fg="black")

        
    def eliminarColumnasGrid(self):                  
        self.grid.destroy()
        self.btnEliminar.destroy()
        self.btnEditar.destroy()
        self.btnAgregar.destroy()

    def limpiarGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)                                                          

    def mostrarClientes(self):  
        self.eliminarColumnasGrid()

        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8","col9","col10"))

        self.grid.column("#0", width=60, anchor=CENTER)
        self.grid.column("col1", width=70, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)
        self.grid.column("col5", width=30, anchor=CENTER)
        self.grid.column("col6", width=90, anchor=CENTER)
        self.grid.column("col7", width=90, anchor=CENTER)
        self.grid.column("col8", width=150, anchor=CENTER)
        self.grid.column("col9", width=90, anchor=CENTER)
        self.grid.column("col10", width=90, anchor=CENTER)
        self.grid.column("#0", width=60, anchor=CENTER)
        self.grid.column("col1", width=70, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)
        self.grid.column("col5", width=30, anchor=CENTER)
        self.grid.column("col6", width=90, anchor=CENTER)
        self.grid.column("col7", width=90, anchor=CENTER)
        self.grid.column("col8", width=150, anchor=CENTER)
        self.grid.column("col9", width=90, anchor=CENTER)
        self.grid.column("col10", width=90, anchor=CENTER)

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Telefono", anchor=CENTER)
        self.grid.heading("col4", text="Cedula", anchor=CENTER)
        self.grid.heading("col5", text="Edad", anchor=CENTER)
        self.grid.heading("col6", text="Ciudad", anchor=CENTER)
        self.grid.heading("col7", text="Provincia", anchor=CENTER)
        self.grid.heading("col8", text="Email", anchor=CENTER)
        self.grid.heading("col9", text="Contraseña", anchor=CENTER)
        self.grid.heading("col10", text="Monto", anchor=CENTER)

        self.grid.place(x=18, y=35, width=860, height=200)

        self.llenarDatosClientes()

        self.btnEliminar = Button(self, text="Eliminar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnEliminar.place(x=350,y=250,width=170, height=30 )

        self.btnAgregar = Button(self, text="Agregar", command = self.mostrarVentanaAgregarCliente, bg="#bfdaff", fg="black")
        self.btnAgregar.place(x=100,y=250,width=170, height=30 )

        self.btnEditar = Button(self, text="Editar", command = self.editarCliente, bg="#bfdaff", fg="black")
        self.btnEditar.place(x=600,y=250,width=170, height=30 )
     
    def mostrarCuentas(self): 

        self.eliminarColumnasGrid()

        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5"))
        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5"))

        self.grid.column("#0", width=3, anchor=CENTER)
        self.grid.column("col1", width=30, anchor=CENTER)
        self.grid.column("col2", width=20, anchor=CENTER)
        self.grid.column("col3", width=10, anchor=CENTER)
        self.grid.column("col4", width=10, anchor=CENTER)
        self.grid.column("col5", width=10, anchor=CENTER)
        self.grid.column("#0", width=3, anchor=CENTER)
        self.grid.column("col1", width=30, anchor=CENTER)
        self.grid.column("col2", width=20, anchor=CENTER)
        self.grid.column("col3", width=10, anchor=CENTER)
        self.grid.column("col4", width=10, anchor=CENTER)
        self.grid.column("col5", width=10, anchor=CENTER)

        self.grid.heading("#0", text="Num_cnta", anchor=CENTER)
        self.grid.heading("col1", text="Tip_cnta", anchor=CENTER)
        self.grid.heading("col2", text="Cedula", anchor=CENTER)
        self.grid.heading("col3", text="Banco", anchor=CENTER)
        self.grid.heading("col4", text="Estado", anchor=CENTER)
        self.grid.heading("col3", text="Banco", anchor=CENTER)
        self.grid.heading("col4", text="Estado", anchor=CENTER)
        self.grid.heading("col5", text="Estado", anchor=CENTER)

        self.grid.place(x=70, y=35, width=760, height=200)

        self.llenarDatosCuentas()

        self.btnEliminar = Button(self, text="Eliminar", command = self.eliminarCuentaB, bg="#bfdaff", fg="black")
        self.btnEliminar.place(x=350,y=250,width=170, height=30 )

        self.btnAgregar = Button(self, text="Agregar", command = self.mostrarVentanaAgregarCuenta, bg="#bfdaff", fg="black")
        self.btnAgregar.place(x=100,y=250,width=170, height=30 )

        self.btnEditar = Button(self, text="Editar", command = self.editarCliente, bg="#bfdaff", fg="black")
        self.btnEditar.place(x=600,y=250,width=170, height=30 )
                
    def mostrasPronosticos(self):

        self.eliminarColumnasGrid()

        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5", "col6"))

        self.grid.column("#0", width=3, anchor=CENTER)
        self.grid.column("col1", width=30, anchor=CENTER)
        self.grid.column("col2", width=20, anchor=CENTER)
        self.grid.column("col3", width=10, anchor=CENTER)
        self.grid.column("col4", width=10, anchor=CENTER)
        self.grid.column("col5", width=10, anchor=CENTER)
        self.grid.column("col6", width=10, anchor=CENTER)

        self.grid.heading("#0", text="Id_Pron", anchor=CENTER)
        self.grid.heading("col1", text="Monto", anchor=CENTER)
        self.grid.heading("col2", text="Valor M.", anchor=CENTER)
        self.grid.heading("col3", text="Ganancia", anchor=CENTER)
        self.grid.heading("col4", text="Fecha", anchor=CENTER)
        self.grid.heading("col5", text="Id_Usuario", anchor=CENTER)
        self.grid.heading("col6", text="Id_Enfrent", anchor=CENTER)

        self.grid.place(x=18, y=35, width=860, height=200)

        self.llenarDatosPronosticos()            

        self.btnEliminar = Button(self, text="Eliminar", command = self.eliminarPronostico, bg="#bfdaff", fg="black")
        self.btnEliminar.place(x=350,y=250,width=170, height=30 )

        self.btnAgregar = Button(self, text="Agregar", command = self.mostrarVentanaAgregarPronostico, bg="#bfdaff", fg="black")
        self.btnAgregar.place(x=100,y=250,width=170, height=30 )

        self.btnEditar = Button(self, text="Editar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnEditar.place(x=600,y=250,width=170, height=30 )

        pass

    def eliminarCliente(self):
        selected = self.grid.focus()                        
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Eliminar",'Debes seleccionar un elemento')            
        else:            
            valores = self.grid.item(selected, 'values')    
            data = str(clave) +", "+ valores[0]+" "+ valores[1]
            print(clave)
            adv = messagebox.askquestion("Eliminar",'¿Deseas eliminar el registro seleccionado?\r'+data) 
            if adv==messagebox.YES:
                cantidad = self.datos.elimina_registro(clave)
                if cantidad==1:
                    messagebox.showinfo("Eliminar", 'Registro eliminado correctamente')
                    self.limpiarGrid()
                    self.llenarDatosClientes()
                    print('Eliminado')
                else:
                    messagebox.showinfo("Eliminar", 'No se ha podido eliminar')                                

        #clave2 = self.grid.item(selected, 'values')        
        #rock = self.grid.item(selected)        
        pass

    def eliminarCuentaB(self):
        selected = self.grid.focus()                        
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Eliminar",'Debes seleccionar un elemento')
        else:            
            valores = self.grid.item(selected, 'values')    
            data = valores[1][6:]
            print(clave)
            adv = messagebox.askquestion("Eliminar",'¿Deseas eliminar la cuenta bancaria?\r'+'Termina en: '+data) 
            if adv==messagebox.YES:
                cantidad = self.datos.elimina_cuenta(clave)
                if cantidad==1:
                    messagebox.showinfo("Eliminar", 'Cuenta bancaria eliminada correctamente')
                    self.limpiarGrid()
                    self.llenarDatosCuentas()
                    print('Eliminado')
                else:
                    messagebox.showinfo("Eliminar", 'No se ha podido eliminar')                                

        #clave2 = self.grid.item(selected, 'values')        
        #rock = self.grid.item(selected)        
        pass

    def eliminarPronostico(self):
        selected = self.grid.focus()                        
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Eliminar",'Debes seleccionar un elemento')
        else:            
            valores = self.grid.item(selected, 'values')    
            data = valores[2]
            print(clave)
            adv = messagebox.askquestion("Eliminar",'¿Deseas eliminar el pronostico?\r'+'Su ganancia es de: '+data)
            if adv==messagebox.YES:
                cantidad = self.datos.elimina_pronostico(clave)
                if cantidad==1:
                    messagebox.showinfo("Eliminar", 'Pronostico eliminado correctamente')
                    self.limpiarGrid()
                    self.llenarDatosPronosticos()
                    print('Eliminado')
                else:
                    messagebox.showinfo("Eliminar", 'No se ha podido eliminar')                                

        pass
    
    def llenarDatosClientes(self):
        datos = self.datos.consulta_cliente()
        for d in datos:
            self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], d[9], d[10]))      

    def llenarDatosPronosticos(self):
        datos = self.datos.consulta_pronostico()
        for d in datos:            
            self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], d[4], d[5], d[6]))

    def llenarDatosCuentas(self):
        datos = self.datos.consulta_cuenta()
        for d in datos:
            if d[4] == 1:
                self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], 'Activo', d[5]))            
            else:
                self.grid.insert("", END, text=d[0], values=(d[1],d[2],d[3],'Inactivo',d[5])) 


    def create_widgets(self):        
        frame1 = Frame(self, bg="")
        frame1.place(x=0, y=0, width=880, height=30)

        self.btnCliente = Button(frame1, text="Cliente", command=self.mostrarClientes, bg="#bfdaff", fg="black")
        self.btnCliente.place(x=30, y=2, width=80, height=30)

        self.btnCuentas = Button(frame1, text="Cuentas Bancarias", command=self.mostrarCuentas, bg="#bfdaff",fg="black")
        self.btnCuentas.place(x=130, y=2, width=130, height=30)

        self.btnPronost = Button(frame1, text="Pronosticos", command = self.mostrasPronosticos, bg="#bfdaff", fg="black")
        self.btnPronost.place(x=280,y=2,width=130, height=30)

#luis
    def mostrarVentanaAgregarCliente(self):
        ventana_agregar = Toplevel(self.master)
        ventana_agregar.title("Agregar Cliente")
        ventana_agregar.geometry("400x600")

        lbl_id = Label(ventana_agregar, text="ID:")        
        lbl_id.pack()
        entry_id = Entry(ventana_agregar)
        entry_id.pack()

        lbl_nombre = Label(ventana_agregar, text="Nombre:")
        lbl_nombre.pack()
        entry_nombre = Entry(ventana_agregar)
        entry_nombre.pack()

        lbl_apellido = Label(ventana_agregar, text="Apellido:")
        lbl_apellido.pack()
        entry_apellido = Entry(ventana_agregar)
        entry_apellido.pack()

        lbl_telefono = Label(ventana_agregar, text="Teléfono:")
        lbl_telefono.pack()
        entry_telefono = Entry(ventana_agregar)
        entry_telefono.pack()

        lbl_cedula = Label(ventana_agregar, text="Cédula:")
        lbl_cedula.pack()
        entry_cedula = Entry(ventana_agregar)
        entry_cedula.pack()

        lbl_edad = Label(ventana_agregar, text="Edad:")
        lbl_edad.pack()
        entry_edad = Entry(ventana_agregar)
        entry_edad.pack()

        lbl_ciudad = Label(ventana_agregar, text="Ciudad:")
        lbl_ciudad.pack()
        entry_ciudad = Entry(ventana_agregar)
        entry_ciudad.pack()

        lbl_provincia = Label(ventana_agregar, text="Provincia:")
        lbl_provincia.pack()
        entry_provincia = Entry(ventana_agregar)
        entry_provincia.pack()

        lbl_email = Label(ventana_agregar, text="Email:")
        lbl_email.pack()
        entry_email = Entry(ventana_agregar)
        entry_email.pack()

        lbl_contrasena = Label(ventana_agregar, text="Contraseña:")
        lbl_contrasena.pack()
        entry_contrasena = Entry(ventana_agregar)
        entry_contrasena.pack()

        lbl_monto = Label(ventana_agregar, text="Monto:")
        lbl_monto.pack()
        entry_monto = Entry(ventana_agregar)
        entry_monto.pack()

        #En el botón también tiene un cambio    
        btn_guardar = Button(ventana_agregar, text="Guardar", 
                             command=lambda: [self.guardarNuevoCliente(entry_id.get(), 
                                                                      entry_nombre.get(), 
                                                                      entry_apellido.get(), 
                                                                      entry_telefono.get(),
                                                                      entry_cedula.get(), 
                                                                      int(entry_edad.get()), 
                                                                      entry_ciudad.get(), 
                                                                      entry_provincia.get(), 
                                                                      entry_email.get(), 
                                                                      entry_contrasena.get(), 
                                                                      float(entry_monto.get())),
                                                self.destruirVentana(ventana_agregar)])
        btn_guardar.pack()

    #Agregué este método para no duplicar codigo 
    def destruirVentana(self, ventana):
        ventana.destroy()

    #Aquí hice cambios
    def guardarNuevoCliente(self, id_usuario, nombre, apellido, telefono, cedula, edad, ciudad, provincia, email, contrasena, monto):            
        self.datos.insertar_cliente(id_usuario, nombre, apellido, telefono, cedula, int(edad), ciudad, provincia, email, contrasena, float(monto))        
                
    def mostrarVentanaAgregarCuenta(self):
        ventana_agregar_cuenta = Toplevel(self.master)
        ventana_agregar_cuenta.title("Agregar Cuenta")
        ventana_agregar_cuenta.geometry("400x300")


        lbl_numero_cuenta = Label(ventana_agregar_cuenta, text="Número de Cuenta:")
        lbl_numero_cuenta.pack()

        entry_numero_cuenta = Entry(ventana_agregar_cuenta)
        entry_numero_cuenta.pack()

        lbl_tipo_cuenta = Label(ventana_agregar_cuenta, text="Tipo de Cuenta:")
        lbl_tipo_cuenta.pack()

        entry_tipo_cuenta = Entry(ventana_agregar_cuenta)
        entry_tipo_cuenta.pack()

        lbl_cedula = Label(ventana_agregar_cuenta, text="Cédula del Cliente:")
        lbl_cedula.pack()

        entry_cedula = Entry(ventana_agregar_cuenta)
        entry_cedula.pack()

        lbl_banco = Label(ventana_agregar_cuenta, text="Banco:")
        lbl_banco.pack()

        entry_banco = Entry(ventana_agregar_cuenta)
        entry_banco.pack()

        lbl_id_usuario = Label(ventana_agregar_cuenta, text="ID de Usuario:")
        lbl_id_usuario.pack()

        entry_id_usuario = Entry(ventana_agregar_cuenta)
        entry_id_usuario.pack()
#cambios en guardar
        btn_guardar = Button(ventana_agregar_cuenta, text="Guardar", 
                             command=lambda: [self.agregarCuenta(entry_numero_cuenta.get(), 
                                                                      entry_tipo_cuenta.get(), 
                                                                      entry_cedula.get(), 
                                                                      entry_banco.get(), 
                                                                      entry_id_usuario.get()),
                                                self.destruirVentana(ventana_agregar_cuenta)])
        btn_guardar.pack()
 
    def agregarCuenta(self, numero_cuenta, tipo_cuenta, cedula_dueño, banco, id_usuario):
        self.datos.insertar_cuenta(numero_cuenta, tipo_cuenta, cedula_dueño, banco, id_usuario)

    def mostrarVentanaAgregarPronostico(self):
        ventana_agregar = Toplevel (self.master)
        ventana_agregar.title("Agregar Pronóstico")
        ventana_agregar.geometry("400x400")

        lbl_id_pronostico = Label(ventana_agregar, text="ID_pron:")        
        lbl_id_pronostico.pack()
        entry_id_pronostico = Entry(ventana_agregar)
        entry_id_pronostico.pack()

        lbl_monto = Label(ventana_agregar, text="Monto:")        
        lbl_monto.pack()
        entry_monto = Entry(ventana_agregar)
        entry_monto.pack()

        lbl_valorM = Label(ventana_agregar, text="Valor Multiplicativo;")        
        lbl_valorM.pack()
        entry_valorM = Entry(ventana_agregar)
        entry_valorM.pack()

        lbl_ganancia = Label(ventana_agregar, text="Ganancia:")        
        lbl_ganancia.pack()
        entry_ganancia = Entry(ventana_agregar)
        entry_ganancia.pack()

        lbl_fecha = Label(ventana_agregar, text="Fecha Apuesta (YYYY/MM/DD):")        
        lbl_fecha.pack()
        entry_fecha = Entry(ventana_agregar)
        entry_fecha.pack()

        lbl_id_usuario = Label(ventana_agregar, text="id_usuario:")        
        lbl_id_usuario.pack()
        entry_id_usuario = Entry(ventana_agregar)
        entry_id_usuario.pack()

        lbl_id_enfrentamiento = Label(ventana_agregar, text="id_enfrentamiento:")        
        lbl_id_enfrentamiento.pack()
        entry_id_enfrentamiento = Entry(ventana_agregar)
        entry_id_enfrentamiento.pack()

        btn_guardar = Button(ventana_agregar, text="Guardar", 
                             command=lambda: [self.guardarNuevoPronostico(entry_id_pronostico.get(), 
                                                                      float(entry_monto.get()), 
                                                                      float(entry_valorM.get()), 
                                                                      float(entry_ganancia.get()),
                                                                      entry_fecha.get(), 
                                                                      entry_id_usuario.get(), 
                                                                      entry_id_enfrentamiento.get(), 
                                                                      ),
                                                self.destruirVentana(ventana_agregar)])
        btn_guardar.pack()

    def guardarNuevoPronostico(self,id_pronostico,monto_apuesta,valor_multiplicativo,ganancia,fecha_apuesta,id_usuario,id_enfrentamiento):
        self.datos.insertar_pronostico(id_pronostico,monto_apuesta,valor_multiplicativo,ganancia,fecha_apuesta,id_usuario,id_enfrentamiento)
    
    #SHEYLA 
    def mostrarVentanaEdicionCliente(self, cliente):
        if cliente == '':
            print("El cliente no se encontró en la base de datos.")
            return

        ventana_edicion = Toplevel(self)
        ventana_edicion.title("Editar Cliente")

        frame_editar= tk.Frame(ventana_edicion)
        frame_editar.pack() 

        label_nombre = Label(ventana_edicion, text="Nombre:")
        entry_nombre = Entry(ventana_edicion)
        entry_nombre.insert(0, cliente[1])
        label_nombre.grid(row=0, column=0)
        entry_nombre.grid(row=0, column=1)

        label_apellido = Label(ventana_edicion, text="Apellido:")
        entry_apellido = Entry(ventana_edicion)
        entry_apellido.insert(0, cliente[2])
        label_apellido.grid(row=1, column=0)
        entry_apellido.grid(row=1, column=1)

        label_telefono = Label(ventana_edicion, text="Teléfono:")
        entry_telefono = Entry(ventana_edicion)
        entry_telefono.insert(0, cliente[3]) 

        label_telefono.grid(row=2, column=0)
        entry_telefono.grid(row=2, column=1)

        label_ciudad = Label(ventana_edicion, text="Ciudad Residencia:")
        entry_ciudad = Entry(ventana_edicion)
        entry_ciudad.insert(0, cliente[6])  # Mostrar valor actual
        label_ciudad.grid(row=3, column=0)
        entry_ciudad.grid(row=3, column=1)

        label_provincia = Label(ventana_edicion, text="Provincia Residencia:")
        entry_provincia = Entry(ventana_edicion)
        entry_provincia.insert(0, cliente[7])  # Mostrar valor actual
        label_provincia.grid(row=4, column=0)
        entry_provincia.grid(row=4, column=1)

        label_email = Label(ventana_edicion, text="Email:")
        entry_email = Entry(ventana_edicion)
        entry_email.insert(0, cliente[8])  # Mostrar valor actual
        label_email.grid(row=5, column=0)
        entry_email.grid(row=5, column=1)
        
        boton_guardar = Button(self.ventana_edicion, text="Guardar cambios",commad= lambda: self.guardar_cambios(cliente[0], ventana_edicion, ))
        boton_guardar.grid(row=6, columnspan=2)

    def editarCliente(self):                
        selected = self.grid.focus()     
        if not selected:
            messagebox.showwarning("Guardar Cambios Cliente", "Debes seleccionar un cliente")            
        else:
            ventana_agregar = Toplevel(self.master)
            ventana_agregar.title("Editar Cliente")
            ventana_agregar.geometry("800x800")

            lbl_nombre = Label(ventana_agregar, text="Nombre:")
            lbl_nombre.pack()
            entry_nombre = Entry(ventana_agregar)
            entry_nombre.pack()

            lbl_apellido = Label(ventana_agregar, text="Apellido:")
            lbl_apellido.pack()
            entry_apellido = Entry(ventana_agregar)
            entry_apellido.pack()

            lbl_telefono = Label(ventana_agregar, text="Teléfono:")
            lbl_telefono.pack()
            entry_telefono = Entry(ventana_agregar)
            entry_telefono.pack()

            lbl_cedula = Label(ventana_agregar, text="Cédula:")
            lbl_cedula.pack()
            entry_cedula = Entry(ventana_agregar)
            entry_cedula.pack()

            lbl_ciudad = Label(ventana_agregar, text="Ciudad:")
            lbl_ciudad.pack()
            entry_ciudad = Entry(ventana_agregar)
            entry_ciudad.pack()

            lbl_provincia = Label(ventana_agregar, text="Provincia:")
            lbl_provincia.pack()
            entry_provincia = Entry(ventana_agregar)
            entry_provincia.pack()

            lbl_email = Label(ventana_agregar, text="Email:")
            lbl_email.pack()

            entry_email = Entry(ventana_agregar)
            entry_email.pack()

            lbl_contraseña = Label(ventana_agregar, text="Contraseña:")
            lbl_contraseña.pack()

            entry_contraseña= Entry(ventana_agregar)
            entry_contraseña.pack()

            btnGuardarCliente = Button(ventana_agregar, text="Guardar Cambios Cliente", 
                                       command=lambda: [self.guardarCambiosCliente(entry_nombre.get(),
                                                                                    entry_apellido.get(),
                                                                                    entry_telefono.get(),
                                                                                    entry_cedula.get(), 
                                                                                    entry_ciudad.get(),
                                                                                    entry_provincia.get(),
                                                                                    entry_email.get(),
                                                                                    entry_contraseña.get()), self.destruirVentana(ventana_agregar)], bg="#bfdaff", fg="black")
        
            btnGuardarCliente.pack()

    def guardarCambiosCliente(self, nombre, apellido, telefono, cedula, ciudad, provincia, email, contraseña):
        selected = self.grid.focus()
        if not selected:
            messagebox.showwarning("Guardar Cambios Cliente", "Debes seleccionar un cliente")
        else:
            cliente_id = self.grid.item(selected, 'text')            
            nuevos_datos = {
                "nombre": nombre,
                "apellido": apellido,
                "telefono": telefono,
                "cedula": cedula,
                "ciudad": ciudad,
                "provincia": provincia,
                "email": email,
                "contraseña": contraseña
                }
            
            self.datos.editar_cliente(cliente_id, nuevos_datos)   
            self.limpiarGrid()
            self.llenarDatosClientes()
    
    def mostrarVentanaEdicionCuentaB(self, id_cuenta):
        if id_cuenta=='':
            print("La cuenta no se encontró en la base de datos.")
            return
        ventana_edicionCuenta= Toplevel(self)
        ventana_edicionCuenta.title("Editar Cuenta Bancaria")

        frame_editarCuenta= tk.Frame(ventana_edicionCuenta)
        frame_editarCuenta.pack()

        label_tipoCuenta= Label(ventana_edicionCuenta, text="Tipo de Cuenta:")
        entry_tipoCuenta = Entry(ventana_edicionCuenta)
        entry_tipoCuenta.insert(0, id_cuenta[1])
        label_tipoCuenta.grid(row=0, column=0)
        entry_tipoCuenta.grid(row=0, column=1)

        label_cedula= Label(ventana_edicionCuenta, text="Cedula:")
        entry_cedula = Entry(ventana_edicionCuenta)
        entry_cedula.insert(0, id_cuenta[2])
        label_cedula.grid(row=1, column=0)
        entry_cedula.grid(row=1, column=1)

        label_banco= Label(ventana_edicionCuenta, text="Banco:")
        entry_banco = Entry(ventana_edicionCuenta)
        entry_banco.insert(0, id_cuenta[3])
        label_banco.grid(row=1, column=0)
        entry_banco.grid(row=1, column=1)

        label_estado= Label(ventana_edicionCuenta, text="Estado:")
        entry_estado = Entry(ventana_edicionCuenta)
        entry_estado.insert(0, id_cuenta[4])
        label_estado.grid(row=2, column=0)
        entry_estado.grid(row=2, column=1)

        boton_guardar_CuentaB= Button(self.ventana_edicionCuenta, text="Guardar Cambios", command=lambda: self.guardar_cambioCuentaB(id_cuenta[0], ventana_edicionCuenta))
        boton_guardar_CuentaB.grid(row=6, columnspan=2)

    def editarCuentaB(self):
        selected= self.grid.focus()
        if not selected:
            messagebox.showwarning("Guardar cambios cuenta", "Debes seleccionar una cuenta")          
        else:
            ventana_agregarCuentaB= Toplevel(self.master)
            ventana_agregarCuentaB.title("Editar Cuenta")
            ventana_agregarCuentaB.geometry("800x800")

            lbl_tipoCuenta= Label(ventana_agregarCuentaB, text="Tipo de cuenta:")
            lbl_tipoCuenta.pack()
            entry_tipoCuenta= Entry(ventana_agregarCuentaB)
            entry_tipoCuenta.pack()

            lbl_cedula= Label(ventana_agregarCuentaB, text="Cedula:")
            lbl_cedula.pack()
            entry_cedula= Entry(ventana_agregarCuentaB)
            entry_cedula.pack()

            lbl_banco= Label(ventana_agregarCuentaB, text="Banco:")
            lbl_banco.pack()
            entry_banco= Entry(ventana_agregarCuentaB)
            entry_banco.pack()

            lbl_estado= Label(ventana_agregarCuentaB, text="Estado:")
            lbl_estado.pack()
            entry_estado= Entry(ventana_agregarCuentaB)
            entry_estado.pack()


            btnGuardarCambiosCuentaB= Button(ventana_agregarCuentaB, text="Guardar cambios cuenta", command=lambda: [self.guardarCambiosCuentaB(entry_tipoCuenta.get(),
                                                                                                                                                entry_cedula.get(),
                                                                                                                                                entry_banco.get(),
                                                                                                                                                entry_estado.get()), self.destruirVentana(ventana_agregarCuentaB)],bg="#bfdaff", fg="black")
            btnGuardarCambiosCuentaB.pack()
    
    def guardarCambiosCuentaB(self, tipoCuenta, cedula, banco, estado):
        selected= self.grid.focus()
        if not selected:
            messagebox.showwarning("Guardar Cambios Cuenta", "Debes seleccionar una Cuenta")
        else:
            id_cuenta= self.grid(selected, 'text')
            datos_cuenta= {
                "tipo de cuenta": tipoCuenta,
                "cedula": cedula,
                "banco": banco,
                "estado": estado
            }
        self.datos.editar_cuenta(id_cuenta, datos_cuenta)
        self.limpiarGrid()
        self.llenarDatosCuentas()

