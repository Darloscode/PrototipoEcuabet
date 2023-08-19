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

    #Sheyla
    def obtener_detalle_cliente(self, id_cliente):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM cliente WHERE id_usuario = %s", (id_cliente,))
        detalles = sql.fetchone()
        sql.close()
        return detalles

    def actualizar_cliente(self, id_cliente, nuevo_nombre, nuevo_apellido):
        sql = self.cnn.cursor()
        sql.execute("UPDATE cliente SET nombre = %s, apellido = %s WHERE id_usuario = %s",
                    (nuevo_nombre, nuevo_apellido, id_cliente))
        self.cnn.commit()
        sql.close()

    #Cuenta Bancaria
    def obtener_detalle_cuenta(self, num_cuenta):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM cuenta_bancaria WHERE num_cuenta = %s", (num_cuenta,))
        detalles = sql.fetchone()
        sql.close()
        return detalles

    def actualizar_cuenta(self, num_cuenta, nuevo_tipo, nuevo_banco):
        sql = self.cnn.cursor()
        sql.execute("UPDATE cuenta_bancaria SET tipo_cuenta = %s, banco = %s WHERE num_cuenta = %s",
                    (nuevo_tipo, nuevo_banco, num_cuenta))
        self.cnn.commit()
        sql.close()

    #MOVIMIENTO BANCARIO
    def obtener_detalle_movimiento(self, num_movimiento):
        sql = self.cnn.cursor()
        sql.execute("SELECT * FROM movimiento_bancario WHERE num_movimiento = %s", (num_movimiento,))
        detalles = sql.fetchone()
        sql.close()
        return detalles

    def actualizar_movimiento(self, num_movimiento, nuevo_tipo, nuevo_monto):
        sql = self.cnn.cursor()
        sql.execute("UPDATE movimiento_bancario SET tipo_movimiento = %s, monto = %s WHERE num_movimiento = %s",
                    (nuevo_tipo, nuevo_monto, num_movimiento))
        self.cnn.commit()
        sql.close()
