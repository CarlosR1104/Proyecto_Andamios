from os import close
import os
import re
from flask.helpers import url_for
from flask.templating import render_template_string
from datetime import datetime
from flask import Flask
from flask import Flask, render_template, request,redirect
from controladores.controlador_empresa import Registrar_Empresa,inicio_Secion_Empresa,registrar_Alquiler,ranking, salidaAlquiler
from controladores import controlador_empresa
from controladores.controlador_particular import Registrar_Particular 
from controladores.controlador_administrador import iniciar_sesion_Administrador
from controladores import controlador_administrador

app=Flask(__name__)
@app.route("/")
def index():
        return render_template('maestra.html')

@app.route("/Dos")
def indexDos():
        return render_template('maestra2.html')

@app.route("/Registrarse")
def Registrarse():
        return render_template('registroEmpresa.html')

@app.route("/Registrarse_particular")
def registrar_Particular():
        return render_template('registroParticular.html')

@app.route("/Registrarse_particular", methods=["POST"])
def Registro_particular():
        nombreParticular = request.form["nombreParticular"]
        residenciaParticular = request.form["residenciaParticular"]
        telefonoParticular = request.form["telefonoParticular"]
        cedulaParticular = request.form["cedulaParticular"]
        Registrar_Particular(nombreParticular,residenciaParticular,telefonoParticular,cedulaParticular)
        return redirect("/")

@app.route("/Registro_cliente", methods=["POST"])
def Registro_cliente():
        rut = request.form["RUT"]
        nombreEmpresa= request.form["nombreEmpresa"]
        ubicacion = request.form["Ubicacion"]
        telefonoEmpresa = request.form ["TelefonoEmpresa"]
        añosDeServicio = request.form["Años_Servicios"]
        nombreAdministrador = request.form["Nombre_Administrador"]
        telefonoAdministrador= request.form["Telefono_Administrador"]
        cedulaAdministrador = request.form["cc"]
        correoAdministrador = request.form["email"]
        contraseñaAdministrador = request.form["contraseña"]
        Registrar_Empresa(rut,nombreEmpresa,ubicacion,telefonoEmpresa,añosDeServicio,nombreAdministrador,telefonoAdministrador,cedulaAdministrador,correoAdministrador,contraseñaAdministrador)
        return redirect("/")

@app.route("/iniciarSecion_empresa")
def iniciarSecion_empresa():
        return render_template('iniciar_secionEmpresa.html')

@app.route("/iniciarSesion_particular")
def iniciarSesion_particular():
        return render_template('iniciar_secion_Particular.html')

@app.route("/login_Empresa", methods=["POST"])
def login_Empresa():
        email=request.form['correoAdministrador']
        contraseña=request.form['contraseña']
        empresa=controlador_empresa.inicio_Secion_Empresa(email)
        try:
                if contraseña== empresa[1]:
                        return redirect ("Dos")
                else:
                        return redirect ("iniciarSecion_empresa")

        except Exception as error:
                        return redirect ("login_Empresa")

#alquiler ===================
@app.route("/formato_Alquiler")
def formato_Alquiler():
        resultado=2+2
        print(resultado)
        return render_template("alquiler.html")

@app.route("/formato_alquiler", methods=["POST"])
def formato_alquiler():
        nombreEmpresa= request.form["nombreEmpresa"]
        ubicacion = request.form["Ubicacion"]
        telefonoEmpresa = request.form ["TelefonoEmpresa"]
        hora = request.form["hora"]
        cantidadModulos=request.form["cantidadModulos"]
        tiempoAlquiler=request.form["tiempoAlquiler"]
        transporte=request.form["transporte"]
        RUT=request.form["RUT"]
        registrar_Alquiler(nombreEmpresa,ubicacion,tiempoAlquiler,telefonoEmpresa,cantidadModulos,transporte,hora,RUT)
        return redirect("Dos")

@app.route("/lista_ranking")
def lista_ranking():
        rankings=ranking()
        frecuencias={}
        for rankin in rankings:
                
                if rankin in frecuencias:
                        frecuencias[rankin] +=1
                        
                else:
                        frecuencias[rankin] =1       
        return render_template("lista_alquiler.html",rankings=rankings,frecuencias=frecuencias)

#Listar alquileres 
@app.route("/ingresar_rut")
def ingreso_rut():
        return render_template('listar_alquileres.html')

@app.route("/listar_alquileres", methods=["POST"])
def listar_alquileres():
        rut=request.form['rut']
        rut2=controlador_empresa.ingreso_rut(rut)
        try:
                if rut == rut2[1]:
                        return redirect ("Dos")
                else:
                        return redirect ("ingreso_rut")
        except Exception as error:
                        return redirect ("login_Empresa")

@app.route("/salida_alquiler")
def salida_alquier():
        salida=salidaAlquiler()
        ultimo=salida[len(salida)-1]
        return render_template("salidaAlquiler.html",ultimo=ultimo)

#Iniciar secion administrador
@app.route("/iniciar_administrador")
def iniciar_administrador():
        return render_template("iniciar_sesion_admin.html")

@app.route("/iniciar_sesion_admin", methods=["POST"])
def iniciar_sesion_admin():
        email = request.form["correo"]
        password = request.form["contraseñaAdministrador"]
        administrador = controlador_administrador.iniciar_sesion_Administrador(email)
        try:
                print(password)
                print(administrador[1])
                if password == administrador[1]:
                        return redirect ("Dos")
                else:
                        return redirect ("iniciar_administrador")
        except Exception as error:
                return redirect ("iniciar_administrador")

if __name__ == "__main__":
        app.run(port=7000, debug=True)