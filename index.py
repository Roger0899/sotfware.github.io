from flask import Flask, render_template, request, redirect
from controladores.login import f_login


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', est=True)

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    passw = request.form['pass']
    f_login(user, passw)
    est = f_login(user, passw)
    print(est)
    if (est==True):
        return redirect('/estudiante')
    else:
        mensaje = "Credenciales incorectas"
        return render_template('login.html', mensaje=mensaje ,est=est)


@app.route('/estudiante')
def welcome():
    return render_template('estudiante.html')

@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos ingresados en el formulario
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        fecha_nacimiento = request.form['fecha_nacimiento']
        carrera = request.form['carrera']

        # Insertar los datos en la base de datos
        cursor = db.cursor()
        sql = "INSERT INTO usuarios (nombre, cedula, fecha_nacimiento, carrera) VALUES (%s, %s, %s, %s)"
        values = (nombre, cedula, fecha_nacimiento, carrera)
        cursor.execute(sql, values)
        db.commit()

        # Redirigir a una página de éxito o mostrar un mensaje
        return "Registro exitoso"

    return render_template('registro.html')

@app.route('/administrador')
def administrador():
    # Datos del administrador (puedes reemplazarlos con datos reales)
    admin_data = {
        'nombre': 'Nombre del Administrador',
        'rol': 'Rol del Administrador',
        'correo': 'correo@example.com',
        'telefono': '+XX XXXXXXXXX',
        'usuarios': [
            {'nombre': 'Usuario 1', 'correo': 'usuario1@example.com'},
            {'nombre': 'Usuario 2', 'correo': 'usuario2@example.com'},
            {'nombre': 'Usuario 3', 'correo': 'usuario3@example.com'}
        ]
    }
    return render_template('administrador.html', admin=admin_data)

@app.route('/docente')
def docente():
    # Datos del docente (puedes reemplazarlos con datos reales)
    teacher_data = {
        'nombre': 'Nombre del Docente',
        'asignatura': 'Nombre de la Asignatura',
        'universidad': 'Nombre de la Universidad',
        'correo': 'correo@example.com',
        'telefono': '+XX XXXXXXXXX',
        'cursos': [
            {'nombre': 'Curso 1', 'seccion': 'Sección A'},
            {'nombre': 'Curso 2', 'seccion': 'Sección B'},
            {'nombre': 'Curso 3', 'seccion': 'Sección C'}
        ]
    }
    return render_template('docente.html', teacher=teacher_data)

@app.route('/estudiante')
def estudiante():
    # Datos del estudiante (puedes reemplazarlos con datos reales)
    student_data = {
        'nombre': 'Nombre del Estudiante',
        'edad': 20,
        'carrera': 'Nombre de la Carrera',
        'universidad': 'Nombre de la Universidad',
        'correo': 'correo@example.com',
        'telefono': '+XX XXXXXXXXX',
        'historial': [
            {'materia': 'Materia 1', 'calificacion': 8.5},
            {'materia': 'Materia 2', 'calificacion': 9.0},
            {'materia': 'Materia 3', 'calificacion': 7.8}
        ]
    }
    return render_template('estudiante.html', student=student_data)

@app.route('/user')
def user():
    # Datos del usuario externo (puedes reemplazarlos con datos reales)
    user_data = {
        'nombre': 'Nombre del Usuario Externo',
        'empresa': 'Nombre de la Empresa',
        'correo': 'correo@example.com',
        'telefono': '+XX XXXXXXXXX',
    }
    return render_template('user.html', user=user_data)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Aquí puedes agregar la lógica de autenticación
    
    # Ejemplo de lógica de redireccionamiento basado en el correo electrónico
    if username.endswith('@estudiante.com'):
        return redirect('/estudiante')
    elif username.endswith('@docente.com'):
        return redirect('/docente')
    elif username.endswith('@administrador.com'):
        return redirect('/administrador')
    else:
        return redirect('/error')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
