from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':

        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidad_tarros'])


        total_sin_descuento = cantidad_tarros * 9000
        descuento = 0

        if 18 <= edad <= 30:
            descuento = total_sin_descuento * 0.15
        elif edad > 30:
            descuento = total_sin_descuento * 0.25

        total_pagar = total_sin_descuento - descuento

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_pagar=total_pagar)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':

        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']


        if usuario == 'juan' and contrasenia == 'admin':
            mensaje = 'Bienvenido Administrador Juan'
        elif usuario == 'pepe' and contrasenia == 'user':
            mensaje = 'Bienvenido Usuario Pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectas'

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)