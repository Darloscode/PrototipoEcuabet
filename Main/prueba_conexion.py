import mysql.connector

conexion = mysql.connector.connect(user='root', password='RYWW5lYUTZ04lgZnp8LE',
                                   host='containers-us-west-67.railway.app',
                                   database='proyecto',
                                   port='7749')

print(conexion)