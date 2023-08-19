from tkinter import *
from tkinter import ttk
from sql import *
from tkinter import Toplevel, Label, Entry, Button


class Ventana(Frame):
    datos = Base()

    def __init__(self, master=None):
        super().__init__(master, width=900, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        self.grid = None  # inicializo el atributo grid

    def eliminarColumnasGrid(self):
        self.grid.destroy()

    def mostrarClientes(self):

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
        datos = self.datos.consulta_cliente()
        for d in datos:
            self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8]))

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

        datos = self.datos.consulta_cuenta()
        for d in datos:
            if d[4] == 1:
                self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], 'Activo', d[5]))
            else:
                self.grid.insert("", END, text=d[0], values=(d[1], d[2], d[3], 'Inactivo', d[5]))
    #Sheyla
    def guardarEdicionCliente(self, id_usuario, nuevos_datos, ventana):
        self.datos.editar_cliente(id_usuario, nuevos_datos)  # Llamada al método editar_cliente de Base
        self.mostrarClientes()  # Actualizar la tabla de clientes
        ventana.destroy()
    #
    def create_widgets(self):
        frame1 = Frame(self, bg="")
        frame1.place(x=0, y=0, width=880, height=30)

        self.btnCliente = Button(frame1, text="Cliente", command=self.mostrarClientes, bg="#bfdaff", fg="black")
        self.btnCliente.place(x=30, y=2, width=80, height=30)

        self.btnCuentas = Button(frame1, text="Cuentas Bancarias", command=self.mostrarCuentas, bg="#bfdaff",
                                 fg="black")
        self.btnCuentas.place(x=130, y=2, width=130, height=30)

        # Agregar un botón para editar cliente
        self.btnEditarCliente = Button(frame1, text="Editar Cliente", command=self.editarCliente, bg="#bfdaff",
                                       fg="black")
        self.btnEditarCliente.place(x=280, y=2, width=100, height=30)

        # Agregar un botón para editar cuenta
        #self.btnEditarCuenta = Button(frame1, text="Editar Cuenta", command=self.editarCuenta, bg="#bfdaff", fg="black")
        #self.btnEditarCuenta.place(x=400, y=2, width=100, height=30)


    # sheyla
    # EDITAR CLIENTES
    def editarCliente(self):
        seleccion = self.grid.selection()
        if seleccion:
            id_usuario = seleccion[0]
            cliente = self.datos.obtener_cliente(id_usuario)
            self.mostrarVentanaEdicionCliente(id_usuario, cliente)

    def mostrarVentanaEdicionCliente(self, id_usuario, cliente):
        if cliente == None:
            print("El cliente no se encontró en la base de datos.")
            return

        ventana_edicion = Toplevel(self.master)
        ventana_edicion.title("Editar Cliente")
        ventana_edicion.geometry("400x300")

        lbl_nombre = Label(ventana_edicion, text="Nombre:")
        lbl_nombre.pack()
        entry_nombre = Entry(ventana_edicion)
        entry_nombre.pack()
        entry_nombre.insert(0, cliente["nombre"])  # Cargar nombre actual

        lbl_apellido = Label(ventana_edicion, text="Apellido:")
        lbl_apellido.pack()
        entry_apellido = Entry(ventana_edicion)
        entry_apellido.pack()
        entry_apellido.insert(0, cliente["apellido"])  # Carga el apellido actual

        btn_guardar = Button(ventana_edicion, text="Guardar", command=lambda: self.guardarEdicionCliente(id_usuario, {
            "nombre": entry_nombre.get(),
            "apellido": entry_apellido.get(),
        }, ventana_edicion))
        btn_guardar.pack()