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
        sql.execute("SELECT * FROM cliente WHERE id_usuario = %s", id_usuario)
        cliente = sql.fetchone()
        sql.close()
        return cliente

    def editar_cliente(self, id_usuario, nuevos_datos):
        sql = self.cnn.cursor()
        query = "UPDATE cliente SET nombre = %s, apellido = %s, telefono = %s, cedula = %s, edad = %s, ciudad_residencia = %s, provincia_residencia = %s, email = %s WHERE id_usuario = %s"
        valores = (nuevos_datos["nombre"], nuevos_datos["apellido"], nuevos_datos["telefono"], nuevos_datos["cedula"],
                   nuevos_datos["edad"], nuevos_datos["ciudad"], nuevos_datos["provincia"], nuevos_datos["email"],
                   id_usuario)
        sql.execute(query, valores)
        self.cnn.commit()
        sql.close()