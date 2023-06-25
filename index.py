from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Aquí puedes agregar la lógica de autenticación
    # Por ahora, simplemente redireccionaremos a una página de bienvenida
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True, port=5017)
