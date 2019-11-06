class Posteo():

    def __init__(self, mensaje, id_usuario, id_categoria):
        # self.id_posteo=id_posteo
        self.mensaje=mensaje
        self.id_usuario=id_usuario
        self.id_categoria=id_categoria
    
    #geters
    def get_id_posteo(self):
        return self.id_posteo
    def get_mensaje(self):
        return self.mensaje
    def get_id_usuario(self):
        return self.id_usuario
    def get_id_categoria(self):
        return self.id_categoria
    
    #seters
    def set_id_posteo(self, id_posteo):
        self.id_posteo=id_posteo
    def set_mensaje(self, mensaje):
        self.mensaje=mensaje
    def set_id_usuario(self, id_usuario):
        self.id_usuario=id_usuario
    def set_id_categoria(self, id_categoria):
        self.id_categoria