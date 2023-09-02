import mysql.connector
from datetime import date

class Base:
    def __init__(self):
        self.cnn = mysql.connector.connect(user='root', password='RYWW5lYUTZ04lgZnp8LE',
                                   host='containers-us-west-67.railway.app',
                                   database='proyecto',
                                   port='7749')

    def __str__(self):
        datos = self.consulta_cliente()
        aux = ""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux

    #Carlos 
    def consulta_cliente(self):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM cliente")
        datos = sql.fetchall()
        sql.close()    
        return datos
    
    def consulta_cuenta(self):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM cuenta_bancaria")
        datos = sql.fetchall()
        sql.close()    
        return datos
    
    def consulta_pronostico(self):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM pronostico_deportivo")
        datos = sql.fetchall()
        sql.close()    
        return datos

    def elimina_pronostico(self, idPronostico):
        sql = self.cnn.cursor()
        sql.execute("DELETE FROM pronostico_deportivo WHERE id_pronostico = " +"'" + idPronostico + "'")
        cantidad = sql.rowcount
        self.cnn.commit()     
        sql.close()
        return cantidad
    
    def elimina_registro(self, id_cliente):
        sql = self.cnn.cursor()
        sql.execute("DELETE FROM movimiento_bancario WHERE id_usuario = "+id_cliente)
        sql.execute("DELETE FROM cuenta_bancaria WHERE id_usuario = "+id_cliente)        
        sql.execute("DELETE FROM pronostico_deportivo WHERE id_usuario = "+id_cliente)

        sql.execute( "SELECT id_cupon FROM cupones WHERE nombreDeUsuario = "+id_cliente)
        datos = sql.fetchall()
        for i in datos:
            elemento = str(i[0])
            sql.execute("DELETE FROM paradas WHERE cupon_ganador = "+elemento)

        sql.execute("DELETE FROM cupones WHERE nombreDeUsuario = "+id_cliente)
        sql.execute("DELETE FROM cliente WHERE id_usuario = "+id_cliente)

        cantidad = sql.rowcount
        self.cnn.commit()     
        sql.close()
        return cantidad

    def eliminar_cuenta(self, cuenta):
        sql = self.cnn.cursor()

        sql.execute("DELETE FROM movimiento_bancario WHERE num_cuenta = " +"'" + cuenta + "'")
        sql.execute("DELETE FROM cuenta_bancaria WHERE num_cuenta = " +"'" + cuenta + "'")                        

        cantidad = sql.rowcount
        self.cnn.commit()     
        sql.close()        
        return cantidad

    def eliminar_clienteSP(self, idCliente):        
        sql = self.cnn.cursor()        
        sql.execute("call eliminarCliente(" + "\"" + idCliente + "\");")
        cantidad = sql.rowcount
        self.cnn.commit()     
        sql.close()
        return cantidad
    
    def eliminar_cuentaBSP(self, idCliente):
        sql = self.cnn.cursor()        
        sql.execute("call eliminarCuentaBancaria(" + "\"" + idCliente + "\");")
        cantidad = sql.rowcount
        self.cnn.commit()     
        sql.close()
        return cantidad
    
    def eliminar_pronosticoSP(self, idCliente):
        sql = self.cnn.cursor()        
        sql.execute("call eliminarPronostico(" + "\"" + idCliente + "\");")
        cantidad = sql.rowcount
        self.cnn.commit()     
        sql.close()
        return cantidad        

    #SHEYLA
    def obtener_cliente(self, id_usuario):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM cliente WHERE id_usuario =" + "'" + id_usuario + "'")
        cliente = sql.fetchone()
        sql.close()
        return cliente

    def editar_cliente(self, id_usuario, nuevos_datos):
        try:
            sql = self.cnn.cursor() 
            update_query = "UPDATE cliente SET nombre = %s, apellido = %s, telefono = %s, cedula = %s, ciudad_residencia = %s, provincia_residencia = %s, email = %s, password = %s WHERE id_usuario = %s"
            valores = (
                nuevos_datos["nombre"],
                nuevos_datos["apellido"],
                nuevos_datos["telefono"],
                nuevos_datos["cedula"],
                nuevos_datos["ciudad"],
                nuevos_datos["provincia"],
                nuevos_datos["email"],
                nuevos_datos["contraseña"],
                id_usuario
            )
            sql.execute(update_query, valores)
            self.cnn.commit()
            sql.close()
            print("Cambios guardados exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al actualizar el cliente: {err}")
   
    def obtener_cuentaB(self, id_cuenta):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM cuenta_bancaria WHERE num_cuenta =" + "'" + id_cuenta + "'")
        cuenta = sql.fetchone()
        sql.close()
        return cuenta
    
    def editar_cuentaB(self, cuenta_ac, datos_cuenta):
        try:
            sql = self.cnn.cursor()

            update_query = "UPDATE cuenta_bancaria SET tipo_cuenta = %s, cedula_dueño = %s, banco = %s WHERE num_cuenta = %s"
            valores_cuentaB = (
                datos_cuenta["tipo de cuenta"],                
                datos_cuenta["cedula"],
                datos_cuenta["banco"],
                cuenta_ac
            )
            sql.execute(update_query, valores_cuentaB)
            self.cnn.commit()
            sql.close()
            print("Cambios en la cuenta bancaria guardados exitosamente")
        except mysql.connector.Error as err:
            print(f"Error al actualizar la cuenta bancaria: {err}")   

    def editar_pronostico(self, id_pronostico, datos_cuenta):
        try:
            sql = self.cnn.cursor()

            update_query = "UPDATE pronostico_deportivo SET monto_apuesta = %s, valor_multiplicativo = %s WHERE id_pronostico = %s"
            valores_cuentaB = (
                datos_cuenta["monto"],                
                datos_cuenta["valorm"],
                id_pronostico
            )
            sql.execute(update_query, valores_cuentaB)
            self.cnn.commit()            
            sql.close()
            print("Cambios en el pronostico guardados exitosamente")
        except mysql.connector.Error as err:
            print(f"Error al actualizar la cuenta bancaria: {err}")

    def editar_clienteSP(self, nombre, apellido, telefono, cedula, ciudad_resisdencia, provincia_residencia, email, password):
        sql = self.cnn.cursor()
        sql.execute("call agregarCliente(" + "\"" + nombre + "\", \"" + apellido + "\", \"" + telefono + "\", \"" + cedula + "\", \"" + ciudad_resisdencia + "\", \"" + provincia_residencia + "\", \"" + email + "\", \"" + password + "\");")
        self.cnn.commit()
        sql.close()

    def editar_cuentaBSP(self, tipoCuenta, cedula, banco, estado):
        sql = self.cnn.cursor()
        sql.execute("call agregarCuentaBancaria(" + tipoCuenta + ", \"" + cedula + "\", " + banco + ", " + estado + ");")
        self.cnn.commit()
        sql.close()

    #def agregar_pronosticoSP(self, idCliente, descripcion, fechaPronostico):
        #sql = self.cnn.cursor()
        #sql.execute("call agregarPronostico(" + str(idCliente) + ", \"" + descripcion + "\", \"" + fechaPronostico + "\");")
        #self.cnn.commit()
        #sql.close()

    
    #LUIS
    def insertar_cliente(self, id_usuario ,nombre, apellido, telefono, cedula, edad, ciudad, provincia, email, contrasena, monto):
        #Aquí hice cambios
        try:
            sql = self.cnn.cursor()
            values = "\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\", \"{}\", {}".format(id_usuario, nombre, apellido, telefono, cedula, edad, ciudad, provincia, email, contrasena, monto)
            insert_query = "CALL AgregarCliente("+values+")"            
            print(insert_query)
            sql.execute(insert_query)
            self.cnn.commit()
            sql.close()
            print("Cliente agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar el cliente: {err}")


    def insertar_cuenta(self, num_cuenta, tipo, cedula, banco, id_usuario):
        try:
            sql = self.cnn.cursor()
            values = "\"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}\"".format(num_cuenta, tipo, cedula, banco, 1, id_usuario)
            insert_query = insert_query = "CALL AgregarCuentaBancaria("+values+")"
            print(insert_query)
            sql.execute(insert_query)
            self.cnn.commit()
            sql.close()
            print("Cuenta bancaria agregada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar la cuenta bancaria: {err}")

    def insertar_pronostico(self,id_pronostico,monto_apuesta,valor_multiplicativo,ganancia,fecha_apuesta,id_usuario,id_enfrentamiento):
        x=[int(part) for part in fecha_apuesta.split("/")]
        fecha=date(x[0],x[1],x[2])
        try:
            sql = self.cnn.cursor()
            insert_query = "CALL AgregarPronostico(%s, %s, %s, %s, %s, %s, %s)"
            values = (id_pronostico, monto_apuesta, valor_multiplicativo, ganancia, fecha, id_usuario, id_enfrentamiento)
            sql.execute(insert_query, values)
            self.cnn.commit()
            sql.close()
            print("Pronóstico agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar el pronóstico: {err}")

