from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget
from PyQt5.QtGui import QPixmap
from .analisis import crear_dataframe, graficar_masa, graficar_distribucion_tipos

class ModeloEstandarApp(QWidget):
    def __init__(self, particles):
        super().__init__()
        self.particles = particles
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Modelo Estándar de Partículas')
        layout = QVBoxLayout()

        # Display Logo
        logo = QLabel(self)
        pixmap = QPixmap('path_to_logo.png')  # Replace with your logo path
        logo.setPixmap(pixmap)
        layout.addWidget(logo)

        # Particle Selection Menu
        self.particle_list = QListWidget()
        for particle in self.particles.values():
            self.particle_list.addItem(particle.nombre)
        self.particle_list.currentItemChanged.connect(self.display_particle_info)
        layout.addWidget(self.particle_list)

        # Particle Information Display
        self.info_label = QLabel('Seleccione una partícula para ver su información.')
        layout.addWidget(self.info_label)

        # Buttons for Plotting
        mass_button = QPushButton('Graficar Masa')
        mass_button.clicked.connect(self.plot_mass)
        layout.addWidget(mass_button)

        distribution_button = QPushButton('Graficar Distribución de Tipos')
        distribution_button.clicked.connect(self.plot_distribution)
        layout.addWidget(distribution_button)

        self.setLayout(layout)

    def display_particle_info(self):
        selected_particle = self.particle_list.currentItem().text()
        particle = next((p for p in self.particles.values() if p.nombre == selected_particle), None)
        if particle:
            self.info_label.setText(particle.mostrar_info())

    def plot_mass(self):
        df = crear_dataframe(self.particles)
        graficar_masa(df)

    def plot_distribution(self):
        df = crear_dataframe(self.particles)
        graficar_distribucion_tipos(df)
