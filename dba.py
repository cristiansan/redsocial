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
    def mostrar_categoria(self):
        self.cursor.execute(queries['mostrar_categoria'])
        # self.conexion.commit()
        return self.cursor.fetchall()
        

    def del_usuario(self, EMAIL):
        val=EMAIL
        # val=usuario.get_id()
        self.cursor.execute(queries['del_usuario'], (val,))
        self.conexion.commit()

    def del_posteo(self, ID_POSTEO):
        # val=ID_POSTEO
        # self.cursor.execute(queries['del_posteo'], (val,))
        val=ID_POSTEO
        self.cursor.execute(queries['del_posteo'], (val,))
        self.conexion.commit()

    def add_posteo(self, MENSAJE, ID_USUARIO, ID_CATEGORIA):
        val=(MENSAJE, ID_USUARIO, ID_CATEGORIA)
        self.cursor.execute(queries['add_posteo'], val)
        self.conexion.commit()

    def consultar_id(self, EMAIL):
        val=EMAIL
        self.cursor.execute(queries['consultar_id'], (val,))
        return self.cursor.fetchall()

    def list_posteo_usuario(self, ID_USUARIO):
        val=(ID_USUARIO)
        self.cursor.execute(queries['list_posteo_usuario'], (val,))
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

    def agregar_amigo(self, usuario, EMAIL):
        user=self.consultar_id(usuario.get_email())
        amigo=self.consultar_id(EMAIL)
        val=(user[0][0],amigo[0][0])
        self.cursor.execute(queries['add_amigo'],val)
        self.conexion.commit()
             
    def login (self, EMAIL, CLAVE):
        val=(EMAIL, CLAVE)
        self.cursor.execute(queries['loguearse'], val)
        reporte = self.cursor.fetchall()
        return reporte