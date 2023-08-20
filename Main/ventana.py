from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sql import *
from tkinter import Toplevel, Label, Entry, Button


class Ventana(Frame):
    datos = Base()

    def __init__(self, master=None):
        super().__init__(master,width=900, height=460)
        self.master = master
        self.pack()
        self.create_widgets()      
        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.btnEliminar = Button(self, text="", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnEditar = Button(self, text="", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnAgregar = Button(self, text="", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        
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

        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))

        self.grid.column("#0", width=60, anchor=CENTER)
        self.grid.column("col1", width=70, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)
        self.grid.column("col5", width=30, anchor=CENTER)
        self.grid.column("col6", width=90, anchor=CENTER)
        self.grid.column("col7", width=90, anchor=CENTER)
        self.grid.column("col8", width=150, anchor=CENTER)
        self.grid.column("#0", width=60, anchor=CENTER)
        self.grid.column("col1", width=70, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)
        self.grid.column("col5", width=30, anchor=CENTER)
        self.grid.column("col6", width=90, anchor=CENTER)
        self.grid.column("col7", width=90, anchor=CENTER)
        self.grid.column("col8", width=150, anchor=CENTER)

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Telefono", anchor=CENTER)
        self.grid.heading("col4", text="Cedula", anchor=CENTER)
        self.grid.heading("col5", text="Edad", anchor=CENTER)
        self.grid.heading("col6", text="Ciudad", anchor=CENTER)
        self.grid.heading("col7", text="Provincia", anchor=CENTER)
        self.grid.heading("col8", text="Email", anchor=CENTER)
        self.grid.heading("col4", text="Cedula", anchor=CENTER)
        self.grid.heading("col5", text="Edad", anchor=CENTER)
        self.grid.heading("col6", text="Ciudad", anchor=CENTER)
        self.grid.heading("col7", text="Provincia", anchor=CENTER)
        self.grid.heading("col8", text="Email", anchor=CENTER)

        self.grid.place(x=18, y=35, width=860, height=200)

        self.llenarDatosClientes()

        self.btnEliminar = Button(self, text="Eliminar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnEliminar.place(x=350,y=250,width=170, height=30 )

        self.btnAgregar = Button(self, text="Agregar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnAgregar.place(x=100,y=250,width=170, height=30 )

        self.btnEditar = Button(self, text="Editar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
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

        self.btnAgregar = Button(self, text="Agregar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnAgregar.place(x=100,y=250,width=170, height=30 )

        self.btnEditar = Button(self, text="Editar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
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

        self.btnAgregar = Button(self, text="Agregar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
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
            self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8]))      

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
""""
        # sheyla
        self.btnEditarCliente = Button(frame1, text="Editar Cliente", command=self.editarCliente, bg="#bfdaff",
                                       fg="black")
        self.btnEditarCliente.place(x=450, y=2, width=100, height=30)

        # -- Se agrega los campos de edición para clientes
        self.entry_nombre = Entry(self)
        self.entry_nombre.place(x=30, y=250, width=100, height=25)

        self.entry_apellido = Entry(self)
        self.entry_apellido.place(x=150, y=250, width=100, height=25)

        self.entry_telefono = Entry(self)
        self.entry_telefono.place(x=270, y=250, width=100, height=25)

        self.entry_cedula = Entry(self)
        self.entry_cedula.place(x=390, y=250, width=100, height=25)

        self.entry_edad = Entry(self)
        self.entry_edad.place(x=510, y=250, width=50, height=25)

        self.entry_ciudad = Entry(self)
        self.entry_ciudad.place(x=580, y=250, width=100, height=25)

        self.entry_provincia = Entry(self)
        self.entry_provincia.place(x=700, y=250, width=100, height=25)

        self.entry_email = Entry(self)
        self.entry_email.place(x=820, y=250, width=150, height=25)

        # Botón para guardar los cambios en cliente
        self.btnGuardarCliente = Button(self, text="Guardar Cambios Cliente", command=self.guardarCambiosCliente,
                                        bg="#bfdaff", fg="black")
        self.btnGuardarCliente.place(x=30, y=290, width=200, height=30)
"""
"""
        # Sheyla
        self.btnEditarCuenta = Button(frame1, text="Editar Cuenta", command=self.editarCuenta, bg="#bfdaff", fg="black")
        self.btnEditarCuenta.place(x=570, y=2, width=100, height=30)

        # -- Se agrega los campos de edición para Cuenta
        self.entry_tipo_cuenta = Entry(self)
        self.entry_tipo_cuenta.place(x=700, y=250, width=100, height=25)

    def editarCliente(self):
        seleccion = self.grid.selection()
        if seleccion:
            id_usuario = seleccion[0]
            cliente = self.datos.obtener_cliente(id_usuario)
            self.mostrarVentanaEdicionCliente(id_usuario, cliente)

    def mostrarVentanaEdicionCliente(self, id_usuario, cliente):
        if cliente is None:
            print("El cliente no se encontró en la base de datos.")
            return

        ventana_edicion = Toplevel(self)
        ventana_edicion.title("Editar Cliente")

        label_nombre = Label(ventana_edicion, text="Nombre:")
        entry_nombre = Entry(ventana_edicion)
        entry_nombre.insert(0, cliente["nombre"])
        label_nombre.grid(row=0, column=0)
        entry_nombre.grid(row=0, column=1)

        label_apellido = Label(ventana_edicion, text="Apellido:")
        entry_apellido = Entry(ventana_edicion)
        entry_apellido.insert(0, cliente["apellido"])
        label_apellido.grid(row=1, column=0)
        entry_apellido.grid(row=1, column=1)

        label_telefono = Label(ventana_edicion, text="Teléfono:")
        entry_telefono = Entry(ventana_edicion)
        entry_telefono.insert(0, cliente["telefono"])  # Mostrar valor actual
        label_telefono.grid(row=2, column=0)
        entry_telefono.grid(row=2, column=1)

        label_ciudad = Label(ventana_edicion, text="Ciudad Residencia:")
        entry_ciudad = Entry(ventana_edicion)
        entry_ciudad.insert(0, cliente["ciudad_residencia"])  # Mostrar valor actual
        label_ciudad.grid(row=3, column=0)
        entry_ciudad.grid(row=3, column=1)

        label_provincia = Label(ventana_edicion, text="Provincia Residencia:")
        entry_provincia = Entry(ventana_edicion)
        entry_provincia.insert(0, cliente["provincia_residencia"])  # Mostrar valor actual
        label_provincia.grid(row=4, column=0)
        entry_provincia.grid(row=4, column=1)

        label_email = Label(ventana_edicion, text="Email:")
        entry_email = Entry(ventana_edicion)
        entry_email.insert(0, cliente["email"])  # Mostrar valor actual
        label_email.grid(row=5, column=0)
        entry_email.grid(row=5, column=1)

    def guardar_cambios(self, id_usuario=None, ventana_edicion=None):
        if self.editando_cliente:
            nuevos_datos = {
                "nombre": self.entry_nombre.get(),
                "apellido": self.entry_apellido.get(),
                "telefono": self.entry_telefono.get(),
                "ciudad_residencia": self.entry_ciudad.get(),
                "provincia_residencia": self.entry_provincia.get(),
                "email": self.entry_email.get()
            }
            self.datos.editar_cliente(id_usuario, nuevos_datos)
            ventana_edicion.destroy()

    boton_guardar = Button(self.ventana_edicion, text="Guardar cambios", command=self.guardar_cambios)
    boton_guardar.grid(row=6, columnspan=2)

    self.ventana_edicion.mainloop()

    def editarCuenta(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if clave == '':
            messagebox.showwarning("Editar Cuenta", 'Debes seleccionar un elemento')
        else:
            valores = self.grid.item(selected, 'values')
            self.editando_cuenta = clave
            self.entry_tipo_cuenta.delete(0, END)
            self.entry_tipo_cuenta.insert(0, valores[1])
            self.entry_cedula.delete(0, END)
            self.entry_cedula.insert(0, valores[2])

    def guardarCambiosCuenta(self):
        if self.editando_cuenta:
            nuevos_datos_cuenta = {
                "tipo_cuenta": self.entry_tipo_cuenta.get(),
                "cedula": self.entry_cedula.get(),
                # Agrega más atributos de la cuenta bancaria
            }
            self.datos.editar_cuenta(self.editando_cuenta, nuevos_datos_cuenta)
            self.editando_cuenta = None
            self.limpiarGrid()  # Actualiza la vista de cuentas bancarias
            self.mostrarCuentas()

"""