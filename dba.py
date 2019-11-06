import mysql.connector
from db import dbconf, queries
from usuario import Usuario

class Database():
    """ Modulo para consultar, modificar y conectarse a la base de datos. """
  
    def __init__(self):
        self.conexion = mysql.connector.connect(**dbconf)
        self.cursor = self.conexion.cursor()

    def crear_usuario(self, usuario):
        val=(usuario.get_nombre(),usuario.get_apellido(),usuario.get_clave(),usuario.get_email(), usuario.get_ciudad(), usuario.get_edad(), usuario.get_sexo(), usuario.get_fecha_nac())
        self.cursor.execute(queries['add_usuario'],val)
        self.conexion.commit()
#este es el nuestro

    def del_usuario(self, EMAIL):
        val=EMAIL
        # val=usuario.get_id()
        self.cursor.execute(queries['del_usuario'], (val,))
        self.conexion.commit()

    def list_posteo_usuario(self, ID_USUARIO):
        val=(ID_USUARIO,)
        self.cursor.execute(queries['list_posteo_usuario'], val)
        reporte = self.cursor.fetchall()
        for i in reporte:
            print(i[1])

    def mod_posteo_usuario(self, MENSAJE, ID_POSTEO):
        val=(MENSAJE, ID_POSTEO)
        self.cursor.execute(queries['mod_posteo_usuario'], val)
        reporte = self.cursor.fetchall()
        self.conexion.commit()


    def list_posteos(self):
        self.cursor.execute(queries['list_posteos'])
        reporte = self.cursor.fetchall()
        for i in reporte:
            print(i[1])

     
    def login (self, EMAIL, CLAVE):
        val=(EMAIL, CLAVE)
        self.cursor.execute(queries['loguearse'], val)
        reporte = self.cursor.fetchall()
        print(reporte)
        if reporte==[]:
            print("Alguno de los valores son incorrectos!")
        else:
            print(f"Bienvenido {reporte[0][1]} {reporte[0][2]}, a la red social Punk!")
            usuario=Usuario(reporte[0][1], reporte[0][2], reporte[0][3], reporte[0][4], reporte[0][5], reporte[0][6], reporte[0][7], reporte[0][8])
            # print(usuario())    
            # menu2()
    
    # def menu2(self):
    #     x=input("1.Postear"/n "2.Eliminar post"/n "3.Listar Amigos"/n "Salir"/n)
    #     if x==1:
    #         mensaje=input("Ingrese posteo: ")
    #         id_usuario
    #         print(mensaje, id_usuario, id_categoria)
    #         Usuario.set_posteo()



    # def crear_hospital(self, hospital):
    #     val=(hospital.GetCodigo(),hospital.GetNombre(),hospital.GetDireccion(),hospital.GetTelefono(),hospital.GetNumCama())
    #     self.cursor.execute(queries['add_hosp'],val)
    #     self.conexion.commit()

    # def eliminar_usuario(self, usuario):
    #     val=usuario.GetCodigo()
    #     self.cursor.execute(queries['del_hosp_id'], (val,))
    #     self.conexion.commit()