class Ciudad():

    def __init__(self, id_ciudad, nombre_ciudad, id_provincia):
        self.id_ciudad=id_ciudad
        self.nombre_ciudad=nombre_ciudad
        self.id_provincia=id_provincia
    
    #geters
    def get_id_ciudad(self):
        return self.id_ciudad
    def get_nombre_ciudad(self):
        return self.nombre_ciudad
    def get_id_provincia(self):
        return self.id_provincia
    
    #seters
    def set_id_ciudad(self, id_ciudad):
        self.id_ciudad=id_ciudad
    def set_nombre_ciudad(self, nombre_ciudad):
        self.nombre_ciudad=nombre_ciudad
    def set_id_provincia(self, id_provincia):
        self.id_provincia=id_provincia