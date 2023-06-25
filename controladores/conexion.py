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

def buscar(selec):
  conn = conec()
  # Crear un cursor para ejecutar consultas
  cursor = conn.cursor()
  # Ejemplo: Obtener todos los registros de una tabla llamada 'users'
  cursor.execute(selec)
  rows = cursor.fetchall()
  # Cerrar el cursor y la conexión
  cursor.close()
  conn.close()
  return rows

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
# rows = buscar("SELECT * FROM usuarios where nombre ='Usuario 4'")
# for row in rows:
#     print(row[1])
insertar("new_user")




