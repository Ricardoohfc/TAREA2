from Modelo_Estandar.particulas import Particula
from Modelo_Estandar.analisis import crear_dataframe
from Modelo_Estandar.gui import ModeloEstandarApp
from PyQt5.QtWidgets import QApplication
import sys

# Crear partículas de ejemplo
particles = {  # Cambia 'Particles' a 'particles'
    'electron': Particula("Electrón", "lepton", -1, 0.511),
    'muon': Particula("Muón", "lepton", -1, 105.66),
    'tau': Particula("Tau", "lepton", -1, 1776.86),
    'photon': Particula("Fotón", "boson", 0, 0),
    'higgs_boson': Particula("Bosón de Higgs", "boson", 0, 125090)
}

# Crear y ejecutar la aplicación GUI
app = QApplication(sys.argv)
window = ModeloEstandarApp(particles) 
window.show()
sys.exit(app.exec_())
