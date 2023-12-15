
import numpy as np
from flask import Flask
from flask_cors import CORS
app=Flask(__name__)
CORS(app)

@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1> <hr>"


@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=round((nota1*30)/100+(nota2*30)/100+(nota3*40)/100,2)
    return f"<h1> El resultado es: {resultado}</h1> <hr>"


@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad=60):
    if edad<18:
        R="Menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1>La persona es: {R}</h1> <hr>"

import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>") 
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores=0,columnas=0,filas=0):
    if filas==0:
        arreglo=np.random.randint(valores, size=columnas)
    else:
        arreglo=np.random.randint(valores, size=(filas,columnas))
        
    return f"<h1> El arreglo aleatorio es: {arreglo} </h1> <hr>"


##Haga un programa que calcule la siguiente ecuación: Y = X * Z + Z + X

@app.route("/ecuaciones")
def ecuaciones():
    global request
    x = float(request.args.get('x'))
    z = float(request.args.get('z'))
    y = x * z + z + x
    return f'El resultado de la ecuación es {y}'

    
##Realizar programa que, capturado un número, realice la tabla de multiplicar de ese número
##hasta el 10

@app.route('/tabla')
def tabla():
    global request
    numero = int(request.args.get('numero'))
    resultado = ''
    for i in range(1, 11):
        producto = numero * i
        resultado += f'{numero} x {i} = {producto}\n'
    return resultado

##Realizar el programa que calcule las areas de un circulo, cuadrado y triangulo

@app.route('/area')
def area():
    global request

    figura = request.args.get('figura')
    if figura == 'circulo':
        radio = float(request.args.get('radio'))
        area = 3.14 * radio ** 2
        return f'El área del círculo es {area}'
    elif figura == 'cuadrado':
        lado = float(request.args.get('lado'))
        area = lado ** 2
        return f'El área del cuadrado es {area}'
    elif figura == 'triangulo':
        base = float(request.args.get('base'))
        altura = float(request.args.get('altura'))
        area = base * altura / 2
        return f'El área del triángulo es {area}'
    else:
        return 'Figura no válida'


if __name__=='__main__':
    app.run(debug=True)