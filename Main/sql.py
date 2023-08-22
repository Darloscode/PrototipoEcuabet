import mysql.connector

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
    
    def elimina_pronostico(self, id):
        sql = self.cnn.cursor()
        sql.execute("DELETE FROM pronostico_deportivo WHERE id_pronostico = " +"'" + id + "'")
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

    def elimina_cuenta(self, cuenta):
        sql = self.cnn.cursor()

        sql.execute("DELETE FROM movimiento_bancario WHERE num_cuenta = " +"'" + cuenta + "'")
        sql.execute("DELETE FROM cuenta_bancaria WHERE num_cuenta = " +"'" + cuenta + "'")                        

        cantidad = sql.rowcount
        self.cnn.commit()     
        sql.close()        
        return cantidad

    def consulta_pronostico(self):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM pronostico_deportivo")
        datos = sql.fetchall()
        sql.close()    
        return datos

    #SHEYLA
    def obtener_cliente(self, id_usuario):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM cliente WHERE id_usuario =" + "'" + id_usuario + "'")
        cliente = sql.fetchone()
        sql.close()
        return cliente

    def editar_cliente(self, id_usuario, nuevos_datos):
        sql = self.cnn.cursor()
        query = "UPDATE cliente SET nombre = %s, apellido = %s, telefono = %s, cedula = %s, ciudad_residencia = %s, provincia_residencia = %s, email = %s, Contraseña = %s WHERE id_usuario = %s"
        valores = (nuevos_datos["nombre"], nuevos_datos["apellido"], nuevos_datos["telefono"], nuevos_datos["cedula"],
                   nuevos_datos["ciudad"], nuevos_datos["provincia"], nuevos_datos["email"], nuevos_datos["Contraseña"],
                   id_usuario)
        sql.execute(query, valores)
        self.cnn.commit()
        sql.close()

    def guardar_cambios(self, id_usuario, nuevos_datos):
        self.editar_cliente(id_usuario, nuevos_datos)
        print("Cambios guardados exitosamente.")

        
    #LUIS
    def insertar_cliente(self, id_usuario ,nombre, apellido, telefono, cedula, edad, ciudad, provincia, email, contrasena, monto):
        #Aquí hice cambios
        try:
            sql = self.cnn.cursor()
            values = "\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\", \"{}\", {}".format(id_usuario, nombre, apellido, telefono, cedula, edad, ciudad, provincia, email, contrasena, monto)
            insert_query = "INSERT INTO cliente (id_usuario ,nombre, apellido, telefono, cedula, edad, ciudad_residencia, provincia_residencia, email, password, monto) VALUES ("+values+")"            
            print(insert_query)
            sql.execute(insert_query)
            self.cnn.commit()
            sql.close()
            print("Cliente agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar el cliente: {err}")


    def insertar_cuenta(self, tipo, cedula, banco, estado):
        try:
            sql = self.cnn.cursor()
            insert_query = "INSERT INTO cuenta_bancaria (tipo, cedula, banco, estado) VALUES (%s, %s, %s, %s)"
            values = (tipo, cedula, banco, estado)
            sql.execute(insert_query, values)
            self.cnn.commit()
            sql.close()
            print("Cuenta bancaria agregada exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar la cuenta bancaria: {err}")

    def insertar_pronostico(self, monto, valor_mercado, ganancia, fecha, id_usuario, id_enfrentamiento):
        try:
            sql = self.cnn.cursor()
            insert_query = "INSERT INTO pronostico_deportivo (monto, valor_mercado, ganancia, fecha, id_usuario, id_enfrentamiento) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (monto, valor_mercado, ganancia, fecha, id_usuario, id_enfrentamiento)
            sql.execute(insert_query, values)
            self.cnn.commit()
            sql.close()
            print("Pronóstico agregado exitosamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar el pronóstico: {err}")

