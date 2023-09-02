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
        self.btnEditar = Button(self, text="", command = self.mostrarVentanaEditarCuentaB, bg="#bfdaff", fg="black")
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

        self.btnEditar = Button(self, text="Editar", command = self.mostrarVentanaEditarCliente, bg="#bfdaff", fg="black")
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

        self.btnEliminar = Button(self, text="Eliminar", command = self.eliminarCuentaBancaria, bg="#bfdaff", fg="black")
        self.btnEliminar.place(x=350,y=250,width=170, height=30 )

        self.btnAgregar = Button(self, text="Agregar", command = self.mostrarVentanaAgregarCuenta, bg="#bfdaff", fg="black")
        self.btnAgregar.place(x=100,y=250,width=170, height=30 )

        self.btnEditar = Button(self, text="Editar", command = self.mostrarVentanaEditarCuentaB, bg="#bfdaff", fg="black")
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

        self.btnEditar = Button(self, text="Editar", command = self.mostrarVentanaEditarPronostico, bg="#bfdaff", fg="black")
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
                cantidad = self.datos.eliminar_clienteSP(clave)
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

    def eliminarCuentaBancaria(self):
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
                cantidad = self.datos.eliminar_cuentaBSP(clave)
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
                cantidad = self.datos.eliminar_pronosticoSP(clave)
                if cantidad==1:
                    messagebox.showinfo("Eliminar", 'Pronostico eliminado correctamente')
                    self.limpiarGrid()
                    self.llenarDatosPronosticos()
                    print('Eliminado')
                else:
                    messagebox.showinfo("Eliminar", 'No se ha podido eliminar')
        pass
    

    #Métodos de llenado
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


    #Crear la ventana principal
    def create_widgets(self):        
        frame1 = Frame(self, bg="")
        frame1.place(x=0, y=0, width=880, height=30)

        self.btnCliente = Button(frame1, text="Cliente", command=self.mostrarClientes, bg="#bfdaff", fg="black")
        self.btnCliente.place(x=30, y=2, width=80, height=30)

        self.btnCuentas = Button(frame1, text="Cuentas Bancarias", command=self.mostrarCuentas, bg="#bfdaff",fg="black")
        self.btnCuentas.place(x=130, y=2, width=130, height=30)

        self.btnPronost = Button(frame1, text="Pronosticos", command = self.mostrasPronosticos, bg="#bfdaff", fg="black")
        self.btnPronost.place(x=280,y=2,width=130, height=30)

    #Destruir ventana creada
    def destruirVentana(self, ventana):
        ventana.destroy()


#Luis
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

    #Enviar datos a bd
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

        btn_guardar = Button(ventana_agregar_cuenta, text="Guardar", 
                             command=lambda: [self.guardarNuevaCuenta(entry_numero_cuenta.get(), 
                                                                      entry_tipo_cuenta.get(), 
                                                                      entry_cedula.get(), 
                                                                      entry_banco.get(), 
                                                                      entry_id_usuario.get()),
                                                self.destruirVentana(ventana_agregar_cuenta)])
        btn_guardar.pack()
    
    #Enviar datos a bd
    def guardarNuevaCuenta(self, numero_cuenta, tipo_cuenta, cedula_dueño, banco, id_usuario):
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

    #Enviar datos a bd
    def guardarNuevoPronostico(self,id_pronostico,monto_apuesta,valor_multiplicativo,ganancia,fecha_apuesta,id_usuario,id_enfrentamiento):
        self.datos.insertar_pronostico(id_pronostico,monto_apuesta,valor_multiplicativo,ganancia,fecha_apuesta,id_usuario,id_enfrentamiento)


#Sheyla
    def mostrarVentanaEditarCliente(self):                
        selected = self.grid.focus() 
        if not selected:
            messagebox.showwarning("Guardar Cambios Cliente", "Debes seleccionar un cliente")            
        else:
            ventana_edicionCliente = Toplevel(self.master)
            ventana_edicionCliente.title("Editar Cliente")
            ventana_edicionCliente.geometry("800x800")
            
            valores = self.grid.item(selected, 'values') 

            lbl_nombre = Label(ventana_edicionCliente, text="Nombre:")
            lbl_nombre.pack()
            entry_nombre = Entry(ventana_edicionCliente)
            entry_nombre.insert(0, valores[0])
            entry_nombre.pack()

            lbl_apellido = Label(ventana_edicionCliente, text="Apellido:")
            lbl_apellido.pack()
            entry_apellido = Entry(ventana_edicionCliente)
            entry_apellido.insert(0, valores[1])
            entry_apellido.pack()

            lbl_telefono = Label(ventana_edicionCliente, text="Teléfono:")
            lbl_telefono.pack()
            entry_telefono = Entry(ventana_edicionCliente)
            entry_telefono.insert(0, valores[2])
            entry_telefono.pack()

            lbl_cedula = Label(ventana_edicionCliente, text="Cédula:")
            lbl_cedula.pack()
            entry_cedula = Entry(ventana_edicionCliente)
            entry_cedula.insert(0, valores[3])
            entry_cedula.pack()

            lbl_ciudad = Label(ventana_edicionCliente, text="Ciudad:")
            lbl_ciudad.pack()
            entry_ciudad = Entry(ventana_edicionCliente)
            entry_ciudad.insert(0, valores[5])
            entry_ciudad.pack()

            lbl_provincia = Label(ventana_edicionCliente, text="Provincia:")
            lbl_provincia.pack()
            entry_provincia = Entry(ventana_edicionCliente)
            entry_provincia.insert(0, valores[6])
            entry_provincia.pack()

            lbl_email = Label(ventana_edicionCliente, text="Email:")
            lbl_email.pack()
            entry_email = Entry(ventana_edicionCliente)
            entry_email.insert(0, valores[7])
            entry_email.pack()

            lbl_contraseña = Label(ventana_edicionCliente, text="Contraseña:")
            lbl_contraseña.pack()
            entry_contraseña= Entry(ventana_edicionCliente)
            entry_contraseña.insert(0, valores[8])
            entry_contraseña.pack()

            btnGuardarCambiosCliente = Button(ventana_edicionCliente, text="Guardar Cambios", 
                                       command=lambda: [self.guardarCambiosCliente(entry_nombre.get(),
                                                                                    entry_apellido.get(),
                                                                                    entry_telefono.get(),
                                                                                    entry_cedula.get(), 
                                                                                    entry_ciudad.get(),
                                                                                    entry_provincia.get(),
                                                                                    entry_email.get(),
                                                                                    entry_contraseña.get()), self.destruirVentana(ventana_edicionCliente)], bg="#bfdaff", fg="black")
            btnGuardarCambiosCliente.pack()

    #Enviar datos a bd
    def guardarCambiosCliente(self, nombre, apellido, telefono, cedula, ciudad, provincia, email, contraseña):
        selected = self.grid.focus()                
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
    
    def mostrarVentanaEditarCuentaB(self):        
        selected = self.grid.focus()
        if not selected:
            messagebox.showwarning("Guardar Cambios Cuentas Bancarias", "Debes seleccionar una cuenta bancaria")            
        else:
            ventana_edicionCuenta = Toplevel(self.master)
            ventana_edicionCuenta.title("Editar Cuenta Bancaria")
            ventana_edicionCuenta.geometry("800x800")
            
            valores = self.grid.item(selected, 'values')
            clave = self.grid.item(selected, 'text')

            label_tipoCuenta= Label(ventana_edicionCuenta, text="Tipo de Cuenta:")
            label_tipoCuenta.pack()
            entry_tipoCuenta = Entry(ventana_edicionCuenta)
            entry_tipoCuenta.insert(0, valores[0])
            entry_tipoCuenta.pack()            

            label_cedula= Label(ventana_edicionCuenta, text="Cedula:")
            label_cedula.pack()
            entry_cedula = Entry(ventana_edicionCuenta)
            entry_cedula.insert(0, valores[1])
            entry_cedula.pack()

            label_banco= Label(ventana_edicionCuenta, text="Banco:")
            label_banco.pack()
            entry_banco = Entry(ventana_edicionCuenta)
            entry_banco.insert(0, valores[2])            
            entry_banco.pack()            

            btnGuardarCambiosCuentaB= Button(ventana_edicionCuenta, text="Guardar Cambios", command=lambda: [self.guardarCambiosCuentaB(entry_tipoCuenta.get(),                                                                                                                                        
                                                                                                                                        entry_cedula.get(),                                                                                                                                        
                                                                                                                                        entry_banco.get(),
                                                                                                                                        clave), self.destruirVentana(ventana_edicionCuenta)],bg="#bfdaff", fg="black")
            btnGuardarCambiosCuentaB.pack()                                    

    #Enviar datos a bd
    def guardarCambiosCuentaB(self, tipoCuenta, cedula, banco, cuenta_ac):                     
        datos_cuenta= {
            "tipo de cuenta": tipoCuenta,            
            "cedula": cedula,            
            "banco": banco,            
        }
        
        self.datos.editar_cuentaB(cuenta_ac, datos_cuenta)
        messagebox.showinfo("Actualizar", 'Registro actualizado correctamente')
        self.limpiarGrid()
        self.llenarDatosCuentas()

    def mostrarVentanaEditarPronostico(self):        
        selected = self.grid.focus()
        if not selected:
            messagebox.showwarning("Guardar Cambios Pronostico", "Debes seleccionar un pronostico")            
        else:
            ventana_edicionPronostico = Toplevel(self.master)
            ventana_edicionPronostico.title("Editar Pronostico")
            ventana_edicionPronostico.geometry("800x800")
            
            valores = self.grid.item(selected, 'values')
            clave = self.grid.item(selected, 'text')

            label_monto= Label(ventana_edicionPronostico, text="Monto de apuesta:")
            label_monto.pack()
            entry_monto = Entry(ventana_edicionPronostico)
            entry_monto.insert(0, valores[0])
            entry_monto.pack()            

            label_valorm= Label(ventana_edicionPronostico, text="Valor multiplicativo:")
            label_valorm.pack()
            entry_valorm = Entry(ventana_edicionPronostico)
            entry_valorm.insert(0, valores[1])
            entry_valorm.pack()
    
            btnGuardarCambiosPronostico= Button(ventana_edicionPronostico, text="Guardar Cambios", command=lambda: [self.guardarCambiosPronostico(entry_monto.get(),                                                                                                                                        
                                                                                                                                            entry_valorm.get(),
                                                                                                                                            clave), self.destruirVentana(ventana_edicionPronostico)],bg="#bfdaff", fg="black")
            btnGuardarCambiosPronostico.pack()                                    

    #Enviar datos a bd
    def guardarCambiosPronostico(self, monto, valorm, id_pronostico):                     
        datos_cuenta= {
            "monto": monto,            
            "valorm": valorm,                       
        }
        
        self.datos.editar_pronostico(id_pronostico, datos_cuenta)        
        self.limpiarGrid()
        messagebox.showinfo("Actualizar", 'Registro actualizado correctamente')
        self.llenarDatosPronosticos()
