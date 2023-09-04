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
        sql.execute("SELECT * FROM cliente ORDER BY id_usuario ASC")
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

    def consulta_movimiento(self):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM movimiento_bancario")
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
    
    def eliminar_cliente(self, id_cliente):
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
   
    def editar_cuentaB(self, cuenta_ac, nuevos_datos):
        try:
            sql = self.cnn.cursor()

            update_query = "UPDATE cuenta_bancaria SET tipo_cuenta = %s, cedula_dueño = %s, banco = %s WHERE num_cuenta = %s"
            valores_cuentaB = (
                nuevos_datos["tipo de cuenta"],                
                nuevos_datos["cedula"],
                nuevos_datos["banco"],
                cuenta_ac
            )
            sql.execute(update_query, valores_cuentaB)
            self.cnn.commit()
            sql.close()
            print("Cambios en la cuenta bancaria guardados exitosamente")
        except mysql.connector.Error as err:
            print(f"Error al actualizar la cuenta bancaria: {err}")   

    def editar_pronostico(self, id_pronostico, nuevos_datos):
        try:
            sql = self.cnn.cursor()

            update_query = "UPDATE pronostico_deportivo SET monto_apuesta = %s, valor_multiplicativo = %s WHERE id_pronostico = %s"
            valores_cuentaB = (
                nuevos_datos["monto"],                
                nuevos_datos["valorm"],
                id_pronostico
            )
            sql.execute(update_query, valores_cuentaB)
            self.cnn.commit()            
            sql.close()
            print("Cambios en el pronostico guardados exitosamente")
        except mysql.connector.Error as err:
            print(f"Error al actualizar la cuenta bancaria: {err}")

    def editar_clienteSP(self, cliente_id, nuevos_datos):
        sql = self.cnn.cursor()            
        values = "\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\"".format(cliente_id, nuevos_datos["nombre"], nuevos_datos["apellido"], nuevos_datos["telefono"], nuevos_datos["cedula"], nuevos_datos["ciudad"], nuevos_datos["provincia"], nuevos_datos["email"], nuevos_datos["contraseña"])
        insert_query = "call editarCliente(" +values+ ")"        
        sql.execute(insert_query)
        cantidad = sql.rowcount        
        self.cnn.commit()
        sql.close()
        return cantidad

    def editar_cuentaBSP(self, num_cuenta, nuevos_datos):
        sql = self.cnn.cursor()
        values = "\"{}\", \"{}\", \"{}\", \"{}\"".format(num_cuenta, nuevos_datos["tipo de cuenta"], nuevos_datos["cedula"], nuevos_datos["banco"])
        insert_query = insert_query = "call editarCuentaBancaria("+values+")"            
        sql.execute(insert_query)
        cantidad = sql.rowcount  
        self.cnn.commit()
        sql.close()
        return cantidad

    def editar_pronosticoSP(self, id_pronostico, nuevos_datos):
        sql = self.cnn.cursor()
        values = "\"{}\", \"{}\", \"{}\"".format(id_pronostico, nuevos_datos["monto"], nuevos_datos["valormul"])
        insert_query = insert_query = "call editarPronostico("+values+")"            
        sql.execute(insert_query)
        cantidad = sql.rowcount  
        self.cnn.commit()
        sql.close()
        return cantidad
    
    #LUIS
    def insertar_cliente(self, id_usuario , nombre, apellido, telefono, cedula, edad, ciudad, provincia, email, contrasena):        
        try:
            sql = self.cnn.cursor()
            values = "\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\", \"{}\"".format(id_usuario, nombre, apellido, telefono, cedula, edad, ciudad, provincia, email, contrasena)
            insert_query = "CALL AgregarCliente("+values+")"
            sql.execute(insert_query)
            cantidad = sql.rowcount            
            self.cnn.commit()
            sql.close()
            print("Cliente agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar el cliente: {err}")        
        return cantidad

    def insertar_cuenta(self, num_cuenta, tipo, cedula, banco, id_usuario):
        try:
            sql = self.cnn.cursor()
            values = "\"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}\"".format(num_cuenta, tipo, cedula, banco, 1, id_usuario)
            insert_query = insert_query = "CALL AgregarCuentaBancaria("+values+")"            
            sql.execute(insert_query)
            cantidad = sql.rowcount 
            self.cnn.commit()
            sql.close()
            print("Cuenta bancaria agregada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar la cuenta bancaria: {err}")
        return cantidad

    def insertar_pronostico(self,id_pronostico,monto_apuesta,valor_multiplicativo,ganancia,fecha_apuesta,id_usuario,id_enfrentamiento):
        x=[int(part) for part in fecha_apuesta.split("/")]
        fecha=date(x[0],x[1],x[2])
        try:
            sql = self.cnn.cursor()
            insert_query = "CALL AgregarPronostico(%s, %s, %s, %s, %s, %s, %s)"
            values = (id_pronostico, monto_apuesta, valor_multiplicativo, ganancia, fecha, id_usuario, id_enfrentamiento)            
            sql.execute(insert_query, values)
            cantidad = sql.rowcount 
            self.cnn.commit()
            sql.close()
            print("Pronóstico agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar el pronóstico: {err}")
        return cantidad

    def insertar_movimiento(self, id_mov, tipo, monto, usuario, cuenta):
        try:
            sql = self.cnn.cursor()
            values = "\"{}\", \"{}\", {}, \"{}\", \"{}\"".format(id_mov, tipo, int(monto), usuario, cuenta)
            insert_query = "call agregarMovimiento("+ values+")"
            sql.execute(insert_query)
            cantidad = sql.rowcount 
            self.cnn.commit()
            sql.close()
            print("Movimiento bancario agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar el movimiento bancario: {err}")
        return cantidad


    #def obtener_cliente(self, id_usuario):
     #   sql = self.cnn.cursor()
      #  sql.execute("SELECT * FROM cliente WHERE id_usuario =" + "'" + id_usuario + "'")
       # cliente = sql.fetchone()
        #sql.close()
        #return cliente
    
#    def obtener_cuentaB(self, id_cuenta):
 #       sql = self.cnn.cursor()
  #      sql.execute("SELECT * FROM cuenta_bancaria WHERE num_cuenta =" + "'" + id_cuenta + "'")
   #     cuenta = sql.fetchone()
    #    sql.close()
     #   return cuenta

    #def agregar_pronosticoSP(self, idCliente, descripcion, fechaPronostico):
        #sql = self.cnn.cursor()
        #sql.execute("call agregarPronostico(" + str(idCliente) + ", \"" + descripcion + "\", \"" + fechaPronostico + "\");")
        #self.cnn.commit()
        #sql.close()
