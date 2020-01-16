
import json
import ctypes
import pyhdb
#import socket
import time
from flask_login import UserMixin
from . import login_manager

lib = ctypes.cdll.LoadLibrary('./EncryptBO.dll')
llave = "pruebas"


@staticmethod
    def valida_user(UserName, Password):
        #consultar parametros para conectarse a la BD
        (Motor, IP_Server, userBD, passBD, BD) = Functions.get_json_param('./encriptado1.json') #funcion q retorna los datos de conexion
        puerto = IP_Server[(IP_Server.find(':')+1):]
        ip = IP_Server[0:IP_Server.find(':')]
        if Motor == "HANA":
            #rutina de reintento de conexión
            for x in range(5):
                time.sleep(1)
                try:
                    connection = pyhdb.connect(ip, puerto, userBD, passBD)
                except AttributeError:
                    pass

                if connection.isconnected():
                    cursor = connection.cursor()
                    cursor.execute("SELECT " + "\"Password\"" + " from \""+ BD + "\".OCRD where " + "\"CardCode\"" + " = '" + UserName + "';")
                    result = cursor.fetchone()
                    for l in result:
                        print('conexion OK')
                        password = l
                    break
                    connection.close()

            if connection.isconnected()== False:
                print('sin conexión')

            if (Functions.desencriptar(llave, password)) == Password:
                return True
            else:
                return False
