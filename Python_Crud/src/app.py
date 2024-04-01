from flask import Flask, render_template, request, redirect, url_for #Framework
import os #Para facilitar el acceso a directorios
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicacion
@app.route('/')
def home():
    cursor = db.base_de_datos.cursor()
    cursor.execute('SELECT * FROM users')
    resultado = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in resultado:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data = insertObject)

#Ruta para guardar usuarios en la base de datos
@app.route('/user', methods = ['POST'])

#Funcion para añardir usuarios (CREATE)
def adduser():
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = db.base_de_datos.cursor()
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        data = (username, name, password)
        cursor.execute(sql, data)
        db.base_de_datos.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.base_de_datos.cursor()
    sql = "DELETE FROM users WHERE id =%s"        
    data = (id,)
    cursor.execute(sql, data)
    db.base_de_datos.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods = ['POST'])

def edit(id):
    username = request.form['username']
    name = request.form['name']
    password = request.form['password']

    if username and name and password:
        cursor = db.base_de_datos.cursor()
        sql = "UPDATE users SET username = %s, name = %s, password = %s WHERE id = %s"
        data = (username, name, password, id)
        cursor.execute(sql, data)
        db.base_de_datos.commit()
    return redirect(url_for('home'))   



if __name__ == '__main__':
    app.run(debug = True, port = 4000)


