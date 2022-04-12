from flask import Flask, render_template, request, redirect, url_for

from departamentos import Departamentos

app=Flask(__name__)

mostrar_lista = False

lista_departamentos = {
    Departamentos('Lima','Ciudad de los reyes'),
    Departamentos('Arequipa','Ciudad blanca'),
    Departamentos('Trujillo','Ciudad de la eterna primavera'),
    Departamentos('Ayacucho','Ciudad heroica')
}

mensaje_lista = "Listado de los Departamentos del Perú"
mensaje_nolista= "No hay nada que mostrar"

@app.route("/")
def index():
    if mostrar_lista:
        return render_template('lista_departamentos.html', departamentos=lista_departamentos, mensaje=mensaje_lista)
    else:
        return render_template('lista_departamentos.html', mensaje=mensaje_nolista)
app.run(debug=True)