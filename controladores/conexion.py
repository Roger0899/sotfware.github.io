import mysql.connector

# Configuración de la conexión
host = "sql10.freesqldatabase.com"
port = "3306"
database = "sql10628556"
user = "sql10628556"
password = "mii6wEcrui"

def conec():
  # Establecer la conexión
  conn = mysql.connector.connect(
      host=host,
      port=port,
      database=database,
      user=user,
      password=password
  )
  return conn

def buscar_log(user, passw):
  conn = conec()
  cursor = conn.cursor()
  consulta = "SELECT * FROM usuarios WHERE {} = %s AND {} = %s".format("nombre", "password")
  valores = (user, passw)
  cursor.execute(consulta, valores)
  rows = cursor.fetchall()
  cursor.close()
  conn.close()
  return bool(rows)

def insertar(new_user):
  conn = conec()
  # Crear un cursor para ejecutar consultas
  cursor = conn.cursor()
  # Ejemplo: Insertar un registro en una tabla llamada 'users'
  insert_query = "INSERT INTO usuarios (nombre , email ) VALUES (%s, %s)"
  values = ("John Doe", "johndoe@example.com")
  cursor.execute(insert_query, values)
  # Confirmar los cambios en la base de datos
  conn.commit()
  # Cerrar el cursor y la conexión
  cursor.close()
  conn.close()


# Ejemplo Imprimir los registros obtenidos
# rows = buscar_log("admin","123456")
# rows = buscar_log("Usuario 2","usuario2@example.com")

# print()
# for row in rows:
# insertar("new_user")




