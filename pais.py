class Pais():

    def __init__(self, id_pais, nombre_pais):
        self.id_pais=id_pais
        self.nombre_pais=nombre_pais
    
    #geters
    def get_id_pais(self):
        return self.id_pais
    def get_nombre_pais(self):
        return self.nombre_pais
    #seters
    def set_id_pais(self, id_pais):
        self.id_pais=id_pais
    def set_nombre_pais(self, nombre_pais):
        self.nombre_pais=nombre_pais