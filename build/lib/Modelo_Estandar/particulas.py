#Clase Particula para representar las partículas del Modelo Estándar
class Particula:
    def __init__(self, nombre, tipo, carga, masa, carga_color=None, sabor=None):
        self.nombre = nombre
        self.tipo = tipo
        self.carga = carga
        self.masa = masa
        self.carga_color = carga_color
        self.sabor = sabor

    def mostrar_info(self):
        info = (f"Partícula: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Carga: {self.carga} e\n"
                f"Masa: {self.masa} MeV/c^2\n")
        if self.carga_color:
            info += f"Carga de color: {self.carga_color}\n"
        if self.sabor:
            info += f"Sabor: {self.sabor}\n"
        return info
