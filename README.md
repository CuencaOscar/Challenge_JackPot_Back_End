# Challenge_JackPot_Back_End

Programa realizado con python version 3.10.1

## Instalar los requirements del archivo

pip install -r requirements.txt

## Ejectutamos el comando:
* python manage.py runserver

## Credenciales para el admin 
*  Nombre de usuario: difdesork
*  Contraseña: oscarCuenca1996

# Apis del codigo
*  Devuelve el listado del nombre, el valor en creditos y el url de la imagen de cada una de las frutas
    GET :   http://localhost:8000/JackPot/
*  Devuelve el listado de usuarios
    GET :   http://localhost:8000/JackPot/user/
*  Devuelve la informacion de un usuario, si no existe lo crea
    Post :  http://localhost:8000/JackPot/auth/
    {"email":"oscar@gmail.com"}
*  Devuelve un objeto que contiene el nuevo roll, los creditos totales
    Post : http://localhost:8000/JackPot/new_roll/
    {"current_credits": 10, "user_id": 1}

## Respositorio del Front_End 
*   https://github.com/CuencaOscar/Challenge_JackPot_Front_End

## Ejecucion de Pruebas
*  Utilizamos pytest
*  Colocar pytest para poder ejecutar los scripts

## Modelos
*  El modelo "Fruit", tiene tres parametros (name, value, img)
*  El modelo "CreditUser" tiene dos parametros (user, credit)

## Base de datos
*  sqlite