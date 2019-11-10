import mysql.connector

class Usuario():
    def __init__(self, nombre, apellido, clave, email, ciudad, edad, sexo, fecha_nac):
        # self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.clave=clave
        self.email=email
        self.ciudad=ciudad
        self.edad=edad
        self.sexo=sexo
        self.fecha_nac=fecha_nac
        self.posteo=[]
        self.amistad=[]
    
    # def get_id(self):
    #    return self.id
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_clave(self):
        return self.clave
    def get_email(self):
        return self.email
    def get_ciudad(self):
        return self.ciudad
    def get_edad(self):
        return self.edad
    def get_sexo(self):
        return self.sexo
    def get_fecha_nac(self):
        return self.fecha_nac
    def get_posteo(self):
        return self.posteo
    def get_amistad(self):
        return self.amistad

    # def set_id(self, id):
    #    self.id=id
    def set_nombre(self, nombre):
        self.nombre=nombre
    def set_apellido(self, apellido):
        self.apellido=apellido
    def set_clave(self, clave):
        self.clave=clave        #encriptar!!
    def set_email(self, email):
        self.email=email
    def set_ciudad(self, ciudad):
        self.ciudad=ciudad
    def set_edad(self, edad):
        self.edad=edad
    def set_sexo(self, sexo):
        self.sexo=sexo
    def set_fecha_nac(self, fecha_nac):
        self.fecha_nac=fecha_nac
    def set_posteo(self, posteo): #está agregando posteo
        self.posteo.append(posteo)
    def set_amistad(self, amistad): #está agregando amistades
        self.amistad.append(amistad)
    

