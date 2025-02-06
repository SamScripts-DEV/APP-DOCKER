from flask import Flask, render_template, request, redirect, make_response
import mysql.connector
import os

app = Flask(__name__)

# Obtener el nombre del nodo desde una variable de entorno
NODE_NAME = os.getenv("NODE_NAME", "Unknown")

# Configuración de la base de datos
db_config = {
    'host': 'db-master',
    'user': 'root',
    'password': 'root',
    'database': 'mydb'
}

# Función para conectar a la base de datos
def get_db_connection():
    return mysql.connector.connect(**db_config)

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener datos del formulario
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone = request.form['phone']
        email = request.form['email']
        project_idea = request.form['project_idea']

        # Insertar datos en la base de datos
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contact_requests (first_name, last_name, phone, email, project_idea) VALUES (%s, %s, %s, %s, %s)",
            (first_name, last_name, phone, email, project_idea)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/')

    # Obtener todas las solicitudes de contacto de la base de datos
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT first_name, last_name, project_idea FROM contact_requests ORDER BY created_at DESC")
    contact_requests = cursor.fetchall()
    cursor.close()
    conn.close()

    # Renderizar la plantilla y agregar la cabecera personalizada
    response = make_response(render_template('index.html', contact_requests=contact_requests, node_name=NODE_NAME))
    response.headers['X-Node-Name'] = NODE_NAME  # Cabecera personalizada
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)