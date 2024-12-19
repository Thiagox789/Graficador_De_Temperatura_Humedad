from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'mi_secreto_seguro'
db_user = 'DB/user.db'

# Función para conectarse a la base de datos
def connectarse_db_users():
    conn_users = sqlite3.connect(db_user)
    conn_users.row_factory = sqlite3.Row
    return conn_users

@app.route('/')
def index():
    return redirect(url_for('inicio_sesion'))  

@app.route('/Registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obtener los datos del formulario
        usr_nombre = request.form['nombre']
        usr_email = request.form['email']
        usr_contraseña = request.form['contraseña']
        contraseña_hasheada = generate_password_hash(usr_contraseña)

        conn_users = connectarse_db_users()
        cursor = conn_users.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = ?", (usr_nombre,))
        if cursor.fetchone():
            flash('Ese nombre ya está en uso, usa otro :v')
            conn_users.close()
            return redirect(url_for('registro'))

        cursor.execute(
            "INSERT INTO usuarios (nombre_usuario, correo_electronico, contrasena) VALUES (?, ?, ?)",
            (usr_nombre, usr_email, contraseña_hasheada)
        )
        conn_users.commit()
        conn_users.close()

        flash('¡Se ha registrado con éxito! 😊')
        return redirect(url_for('inicio_sesion'))

    return render_template('registro.html')

@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        usr_nombre = request.form['nombre']
        usr_contraseña = request.form['contraseña']

        conn_users = connectarse_db_users()
        cursor = conn_users.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre_usuario = ?", (usr_nombre,))
        user = cursor.fetchone()
        conn_users.close()

        if user and check_password_hash(user['contrasena'], usr_contraseña):
            session['username'] = usr_nombre
            flash('¡Inicio de sesión exitoso! 😊')
            return redirect(url_for('dashboard'))
        else:
            flash('Nombre de usuario o contraseña incorrectos. Intenta de nuevo.')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f"¡Bienvenido, {session['username']}! <a href='/logout'>Cerrar sesión</a>"
    else:
        return redirect(url_for('inicio_sesion'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Sesión cerrada exitosamente.')
    return redirect(url_for('inicio_sesion'))

if __name__ == '__main__':
    # Crear la base de datos y la tabla si no existen
    conn = connectarse_db_users()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_usuario TEXT NOT NULL UNIQUE,
        correo_electronico TEXT NOT NULL,
        contrasena TEXT NOT NULL
    )
    ''')
    conn.close()

    app.run(host="0.0.0.0", debug=True)
