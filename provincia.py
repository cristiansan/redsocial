class Provincia():

    def __init__(self, id_provincia, nombre_provincia, id_pais):
        self.id_provincia=id_provincia
        self.nombre_provincia=nombre_provincia
        self.id_pais=id_pais
    
    #geters
    def get_id_provincia(self):
        return self.id_provincia
    def get_nombre_provincia(self):
        return self.nombre_provincia
    def get_id_pais(self):
        return self.id_pais
    
    #seters
    def set_id_provincia(self, id_provincia):
        self.id_provincia=id_provincia
    def set_nombre_provincia(self, nombre_provincia):
        self.nombre_provincia=nombre_provincia
    def set_id_pais(self, id_pais):
        self.id_pais=id_pais