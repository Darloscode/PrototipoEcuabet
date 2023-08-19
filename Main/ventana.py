from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from sql import *

class Ventana(Frame):

    datos = Base()

    def __init__(self, master=None):
        super().__init__(master,width=900, height=460)
        self.master = master
        self.pack()
        self.create_widgets()      
        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        
    def eliminarColumnasGrid(self):                  
        self.grid.destroy()         

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

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Telefono", anchor=CENTER)
        self.grid.heading("col4", text="Cedula", anchor=CENTER)
        self.grid.heading("col5", text="Edad", anchor=CENTER)
        self.grid.heading("col6", text="Ciudad", anchor=CENTER)
        self.grid.heading("col7", text="Provincia", anchor=CENTER)
        self.grid.heading("col8", text="Email", anchor=CENTER)

        self.grid.place(x=18, y=35, width=860, height=200)

        self.llenarDatosClientes()

        self.btnCuentas = Button(self, text="Eliminar", command = self.eliminarCliente, bg="#bfdaff", fg="black")
        self.btnCuentas.place(x=350,y=250,width=170, height=30 )

    def mostrarCuentas(self): 

        self.eliminarColumnasGrid()

        self.grid = ttk.Treeview(columns=("col1", "col2", "col3", "col4", "col5"))

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
        self.grid.heading("col5", text="Estado", anchor=CENTER)

        self.grid.place(x=70, y=35, width=760, height=200)

        self.llenarDatosCuentas()

        self.btnEliminar = Button(self, text="Eliminar", command = self.eliminarCuentaB, bg="#bfdaff", fg="black")
        self.btnEliminar.place(x=350,y=250,width=170, height=30 )

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
                self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], 'Inactivo', d[5]))   

    def llenarDatosClientes(self):
        datos = self.datos.consulta_cliente()
        for d in datos:
            self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8]))      

    def create_widgets(self):        
        frame1 = Frame(self, bg="")
        frame1.place(x=0,y=0,width=880, height=30)

        self.btnCliente = Button(frame1, text="Cliente", command = self.mostrarClientes, bg="#bfdaff", fg="black")
        self.btnCliente.place(x=30,y=2,width=80, height=30 )

        self.btnCuentas = Button(frame1, text="Cuentas Bancarias", command = self.mostrarCuentas, bg="#bfdaff", fg="black")
        self.btnCuentas.place(x=130,y=2,width=130, height=30 )

        self.btnPronost = Button(frame1, text="Pronosticos", command = self.mostrasPronosticos, bg="#bfdaff", fg="black")
        self.btnPronost.place(x=280,y=2,width=130, height=30)

    #Sheyla Ventana editar
    #Cliente
    def editarCliente(self):
        # Obtener el ID del cliente seleccionado
        selected_item = self.grid.selection()
        if selected_item:
            id_cliente = self.grid.item(selected_item)["text"]

            # Obtener los detalles del cliente seleccionado
            detalles_cliente = self.datos.obtener_detalle_cliente(id_cliente)

            if detalles_cliente:
                # Se crea una ventana emergente para editar
                ventana_editar = Toplevel(self)
                ventana_editar.title("Editar Cliente")

                # Se agrega campos de entrada para editar detalles
                Label(ventana_editar, text="Nombre:").pack()
                nuevo_nombre = Entry(ventana_editar)
                nuevo_nombre.insert(0, detalles_cliente[1])
                nuevo_nombre.pack()

                Label(ventana_editar, text="Apellido:").pack()
                nuevo_apellido = Entry(ventana_editar)
                nuevo_apellido.insert(0, detalles_cliente[2])
                nuevo_apellido.pack()

                # Botón para guardar los cambios
                boton_guardar = Button(ventana_editar, text="Guardar Cambios",
                                       command=lambda: self.guardarCambiosCliente(id_cliente, nuevo_nombre.get(),nuevo_apellido.get()))
                boton_guardar.pack()

    def guardarCambiosCliente(self, id_cliente, nuevo_nombre, nuevo_apellido):
        # Se realizar la actualización en la base de datos
        self.datos.actualizar_cliente(id_cliente, nuevo_nombre, nuevo_apellido)

        # Se actualiza la vista de la tabla de clientes
        self.mostrarClientes()



    #Cuenta Bancaria
    def editarCuenta(self):
        selected_item = self.grid.selection()
        if selected_item:
            num_cuenta = self.grid.item(selected_item)["text"]
            detalles_cuenta = self.datos.obtener_detalle_cuenta(num_cuenta)

            if detalles_cuenta:
                ventana_editar = Toplevel(self)
                ventana_editar.title("Editar Cuenta Bancaria")

                Label(ventana_editar, text="Tipo de Cuenta:").pack()
                nuevo_tipo = Entry(ventana_editar)
                nuevo_tipo.insert(0, detalles_cuenta[1])
                nuevo_tipo.pack()

                Label(ventana_editar, text="Banco:").pack()
                nuevo_banco = Entry(ventana_editar)
                nuevo_banco.insert(0, detalles_cuenta[3])
                nuevo_banco.pack()

                # ... Agregar campos para otros detalles

                boton_guardar = Button(ventana_editar, text="Guardar Cambios",
                                       command=lambda: self.guardarCambiosCuenta(num_cuenta, nuevo_tipo.get(),
                                                                                 nuevo_banco.get()))
                boton_guardar.pack()

    def guardarCambiosCuenta(self, num_cuenta, nuevo_tipo, nuevo_banco):
        self.datos.actualizar_cuenta(num_cuenta, nuevo_tipo, nuevo_banco)
        self.mostrarCuentas()


    #MOVIMIENTO BANCARIO
    def editarMovimiento(self):
        selected_item = self.grid.selection()
        if selected_item:
            num_movimiento = self.grid.item(selected_item)["text"]
            detalles_movimiento = self.datos.obtener_detalle_movimiento(num_movimiento)

            if detalles_movimiento:
                ventana_editar = Toplevel(self)
                ventana_editar.title("Editar Movimiento Bancario")

                Label(ventana_editar, text="Tipo de Movimiento:").pack()
                nuevo_tipo = Entry(ventana_editar)
                nuevo_tipo.insert(0, detalles_movimiento[1])
                nuevo_tipo.pack()

                Label(ventana_editar, text="Monto:").pack()
                nuevo_monto = Entry(ventana_editar)
                nuevo_monto.insert(0, detalles_movimiento[3])
                nuevo_monto.pack()

                # ... Agregar campos para otros detalles

                boton_guardar = Button(ventana_editar, text="Guardar Cambios",
                                       command=lambda: self.guardarCambiosMovimiento(num_movimiento, nuevo_tipo.get(),
                                                                                     nuevo_monto.get()))
                boton_guardar.pack()

    def guardarCambiosMovimiento(self, num_movimiento, nuevo_tipo, nuevo_monto):
        self.datos.actualizar_movimiento(num_movimiento, nuevo_tipo, nuevo_monto)
        self.mostrarMovimientos()


