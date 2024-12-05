from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget
from PyQt5.QtGui import QPixmap
from .analisis import crear_dataframe, graficar_masa, graficar_distribucion_tipos
import os

class ModeloEstandarApp(QWidget):
    def __init__(self, particles):
        super().__init__()
        self.particles = particles
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Modelo Estándar de Partículas')
        layout = QVBoxLayout()

        # Display Logo (Reducido de tamaño)
        logo = QLabel(self)
        pixmap = QPixmap('logo.png')  # Asegúrate de tener el logo en la ruta correcta
        pixmap = pixmap.scaled(150, 150, aspectRatioMode=True)  # Reducir tamaño a 150x150 píxeles
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

        # Label to show the plot
        self.plot_label = QLabel(self)
        layout.addWidget(self.plot_label)

        self.setLayout(layout)

    def display_particle_info(self):
        # Obtener el nombre de la partícula seleccionada
        selected_item = self.particle_list.currentItem()
        if selected_item is not None:
            selected_particle_name = selected_item.text()
            # Buscar la partícula seleccionada en el diccionario
            particle = next((p for p in self.particles.values() if p.nombre == selected_particle_name), None)
            if particle:
                # Mostrar específicamente la masa de la partícula seleccionada
                self.info_label.setText(f"Partícula seleccionada: {particle.nombre}\nMasa: {particle.masa} MeV/c²")
                print(f"Masa de la partícula {particle.nombre}: {particle.masa} MeV/c²")

    def plot_mass(self):
        selected_item = self.particle_list.currentItem()
        if selected_item is not None:
            selected_particle_name = selected_item.text()
            # Buscar la partícula seleccionada en el diccionario
            particle = next((p for p in self.particles.values() if p.nombre == selected_particle_name), None)
            if particle:
                # Graficar la masa de la partícula seleccionada
                graficar_masa(particle, filename='masa.png')  # Guardamos la imagen en 'masa.png'

                # Mostrar la imagen en la interfaz
                self.show_plot('masa.png')

    def plot_distribution(self):
        df = crear_dataframe(self.particles)
        graficar_distribucion_tipos(df, filename='distribucion_tipos.png')  # Guardamos la imagen en 'distribucion_tipos.png'

        # Mostrar la imagen de distribución en la interfaz
        self.show_plot('distribucion_tipos.png')

    def show_plot(self, filename):
        # Cargar la imagen de la gráfica y mostrarla en el QLabel
        pixmap = QPixmap(filename)
        self.plot_label.setPixmap(pixmap)
        self.plot_label.setAlignment(Qt.AlignCenter)
