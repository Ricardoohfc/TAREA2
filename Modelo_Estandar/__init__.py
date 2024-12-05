from .particulas import Particula
from .analisis import crear_dataframe, graficar_masa, graficar_distribucion_tipos
# Importar la GUI solo si se necesita
try:
    from .gui import ModeloEstandarApp
except ImportError:
    pass
