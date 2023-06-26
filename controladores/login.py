from controladores.conexion import buscar_log

def f_login(user, passw):
  users = buscar_log(user, passw)
  return users

