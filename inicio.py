from flask import Flask, render_template, request, redirect, url_for
import modelo.users as model

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/listar")
def listar():
    lista = model.listar()
    return render_template("listar.html", filas=lista)

@app.route("/eliminar")
def eliminar():
    return render_template("eliminar.html")

@app.route("/eliminarUsuario", methods=["POST"])
def eliminarUsuario():
    rut = request.form["txtRut"]
    usu = busca(rut)
    usu.eliminar()
    return redirect(url_for("listar"))

def busca(rut):
    u = model.Usuario()
    u.Rut = rut # u.setRut(rut)
    u.buscar() # verificar si rut is None para el caso que no lo encuentre
    return u

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")

@app.route("/agregarUsuario", methods=["POST"])
def agregarUsuario():
    rut = request.form["agregarRut"]
    nombre = request.form["agregarNombre"]
    apellido = request.form["agregarApellido"]
    correo = request.form["agregarCorreo"]
    u = model.Usuario()
    u.Rut = rut
    u.Nombre = nombre
    u.Apellido = apellido
    u.Correo = correo
    u.agregar()
    return redirect(url_for("listar"))


@app.route("/modificar")
def modificar():
    return render_template("modificar.html")

@app.route("/modificarUsuario", methods=["POST"])
def editarUsuario():
    rut = request.form["editarRut"]
    nombre = request.form["txtNombre"]
    apellido = request.form["txtApellido"]
    correo = request.form["txtCorreo"]
    u = model.Usuario()
    u.Rut = rut
    u.Nombre = nombre
    u.Apellido = apellido
    u.Correo = correo
    u.modificar()
    return redirect(url_for("listar"))

@app.route("/buscar")
def buscar():
    return render_template("buscar.html")

@app.route("/saludo")
def saludo():
    return """
            <html>
                <head></head>
                <body>
                    <h1>¡Hola Mundo!</h1>
                </body>
            </html>"""

app.run(debug = True)