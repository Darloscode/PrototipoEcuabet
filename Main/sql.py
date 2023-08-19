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