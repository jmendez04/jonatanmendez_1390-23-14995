from flask import Flask, render_template

app = Flask(__name__)


#Pagina principal
@app.route('/')
def index():
    return render_template('index.html')

#Pagina 1
@app.route('/pagina1')
def pagina1():
    return render_template('pagina1.html')

#Pagina 2
@app.route('/pagina2')
def pagina2():
    return render_template('pagina2.html')

#Pagina 3
@app.route('/pagina3')
def pagina3():
    return render_template('pagina3.html')

#Pagina 4
@app.route('/pagina4')
def pagina4():
    return render_template('pagina4.html')

#Ruta con parametro dinamico
@app.route('/estudiante/<nombre>')
def estudiante(nombre):
    return f"Bienvenido, {nombre}"

#Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)