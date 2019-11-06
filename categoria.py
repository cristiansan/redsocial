class Categoria():

    def __init__(self, id_categoria, nombre_categoria):
        self.id_categoria=id_categoria
        self.nombre_categoria=nombre_categoria
    
    #geters
    def get_id_categoria(self):
        return self.id_categoria
    def get_nombre_categoria(self):
        return self.nombre_categoria
    
    #seters
    def set_id_categoria(self, id_categoria):
        self.id_categoria=id_categoria
    def set_nombre_categoria(self, nombre_categoria):
        self.nombre_categoria=nombre_categoria