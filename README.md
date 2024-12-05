# **Modelo Estándar de Partículas - Tutorial de Instalación y Uso**

## **Introducción**

Este proyecto simula un modelo estándar de partículas subatómicas, permitiendo visualizar las propiedades de diferentes partículas (como la masa y el tipo de partícula) y graficarlas utilizando **PyQt5** para la interfaz gráfica y **matplotlib** para las gráficas.

## **Requisitos**

- **Python 3.7+**
- **Anaconda** (opcional, pero recomendado para manejar entornos)
- **PyQt5** para la interfaz gráfica
- **pandas** para manejo de datos
- **matplotlib** para las gráficas

## **Instalación**

### **1. Crear un entorno virtual**

Recomendamos usar un entorno virtual para evitar conflictos con otras dependencias en tu sistema.

Si usas **Anaconda**:

```bash
conda create --name modelo_estandar python=3.10
conda activate modelo_estandar
```

Si usas **venv** en Python:

```bash
python -m venv modelo_estandar
source modelo_estandar/bin/activate  # En macOS/Linux
modelo_estandar\Scripts\activate  # En Windows
```

### **2. Instalar las dependencias**

En tu entorno virtual, instala las dependencias del proyecto.

1. **Clona el repositorio** (si es necesario):

   ```bash
   git clone https://github.com/tu_usuario/Modelo_Estandar.git
   cd Modelo_Estandar
   ```

2. **Instalar las dependencias**:

   Asegúrate de tener un archivo `requirements.txt` con las siguientes líneas:

   ```txt
   pandas
   matplotlib
   pyqt5
   ```

   Luego, instala las dependencias con `pip`:

   ```bash
   pip install -r requirements.txt
   ```

### **3. Configuración del entorno gráfico (opcional)**

Si encuentras problemas con **PyQt5** en macOS, sigue los pasos para instalar las dependencias de Qt necesarias:

```bash
brew install qt
```

Esto asegurará que las bibliotecas de Qt estén correctamente instaladas para que **PyQt5** funcione sin problemas.

## **Ejecutar el Proyecto**

### **1. Ejecutar la interfaz gráfica**

Para iniciar la aplicación, simplemente ejecuta el archivo `run_gui.py`:

```bash
python run_gui.py
```

Este comando abrirá una ventana donde podrás interactuar con la lista de partículas, visualizar su masa, y generar las gráficas correspondientes. También podrás elegir partículas específicas para ver información detallada sobre ellas.

### **2. Interfaz gráfica**

La interfaz tiene las siguientes funcionalidades:

- **Logo**: El logo del proyecto será mostrado en la parte superior.
- **Lista de partículas**: Puedes seleccionar una partícula de la lista para ver sus detalles (nombre, tipo y masa).
- **Botones de gráficas**: Permiten visualizar las gráficas de masa de las partículas y la distribución de tipos de partículas.

### **3. Ver gráficas**

Las gráficas generadas por los botones de la interfaz se guardan como archivos `.png` en el directorio actual. Puedes mostrarlas en la aplicación o visualizarlas directamente.

---

## **Estructura del Proyecto**

```
Modelo_Estandar/
├── Modelo_Estandar/
│   ├── __init__.py
│   ├── particulas.py
│   ├── analisis.py
│   ├── gui.py
├── tests/
│   ├── __init__.py
│   ├── test_particulas.py
│   ├── test_analisis.py
├── requirements.txt
├── run_gui.py
├── logo.png           # Logo del proyecto
└── README.md          # Este archivo
```

---

## **Pruebas Unitarias**

Puedes ejecutar las pruebas unitarias para asegurarte de que el código funciona correctamente. Si usas `pytest` o `unittest`, simplemente ejecuta:

```bash
pytest tests/
```

o

```bash
python -m unittest discover -s tests
```

