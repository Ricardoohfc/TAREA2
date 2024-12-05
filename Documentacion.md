## **Documentación del Código**

Este proyecto consiste en una simulación interactiva de partículas subatómicas del Modelo Estándar. Utiliza **PyQt5** para la interfaz gráfica, **matplotlib** para la visualización gráfica y **pandas** para el manejo de datos.

### **Módulos Importados**

1. **`particulas`**: Contiene la definición de la clase `Particula` que representa a las partículas subatómicas.
2. **`analisis`**: Define las funciones para la creación de DataFrames y generación de gráficas.
3. **`PyQt5`**: Usado para la creación de la interfaz gráfica del usuario (GUI).
4. **`matplotlib`**: Utilizado para la creación de gráficas visuales.



### **Funciones**

#### `crear_dataframe(particles) -> pd.DataFrame`

Crea un DataFrame a partir de un diccionario de partículas. 

- **Argumentos**:
  - `particles`: Diccionario de partículas, donde cada valor es una instancia de la clase `Particula`.
  
- **Retorno**:
  - `DataFrame` con las columnas: `Nombre`, `Tipo`, `Carga (e)`, `Masa (MeV/c^2)`, `Carga de Color`, `Sabor`.

**Descripción**:
Convierte la lista de partículas en un DataFrame y limpia los valores no válidos en la columna de masa.



#### `graficar_masa(particle, filename="masa.png")`

Genera y guarda una gráfica de barras que muestra la masa de una partícula específica.

- **Argumentos**:
  - `particle`: Instancia de la clase `Particula` cuya masa será graficada.
  - `filename`: Nombre del archivo donde se guardará la gráfica. Por defecto es `"masa.png"`.
  
- **Descripción**:
Crea una gráfica de barras con la masa de una sola partícula y la guarda en un archivo de imagen. El archivo se guarda como `filename`.



#### `graficar_distribucion_tipos(df, filename="distribucion_tipos.png")`

Genera y guarda una gráfica circular mostrando la distribución de los tipos de partículas.

- **Argumentos**:
  - `df`: DataFrame de partículas, generalmente creado por `crear_dataframe`.
  - `filename`: Nombre del archivo donde se guardará la gráfica. Por defecto es `"distribucion_tipos.png"`.
  
- **Descripción**:
Crea una gráfica de pastel con la distribución de tipos de partículas y la guarda en un archivo de imagen.



### **Clase: `ModeloEstandarApp`**

La clase `ModeloEstandarApp` define la interfaz gráfica de usuario para interactuar con las partículas.

#### **Métodos de la clase `ModeloEstandarApp`**

##### `__init__(self, particles)`

Inicializa la aplicación con las partículas proporcionadas.

- **Argumentos**:
  - `particles`: Diccionario de partículas, donde cada valor es una instancia de la clase `Particula`.

**Descripción**:
Configura la interfaz gráfica inicial, crea los elementos de la ventana, y conecta las señales de los botones a las funciones correspondientes.



##### `initUI(self)`

Configura la interfaz de usuario de la aplicación.

**Descripción**:
Define la disposición de la ventana, agrega un logo, una lista de partículas, botones para generar las gráficas, y un área donde se mostrarán las gráficas.



##### `display_particle_info(self)`

Muestra la información de la partícula seleccionada en la lista.

**Descripción**:
Obtiene la partícula seleccionada de la lista y muestra su nombre y masa en un `QLabel`.



##### `plot_mass(self)`

Genera y muestra la gráfica de la masa de la partícula seleccionada.

**Descripción**:
- Obtiene la partícula seleccionada de la lista.
- Llama a la función `graficar_masa` para generar la gráfica de la masa.
- Muestra la gráfica generada en la interfaz.



##### `plot_distribution(self)`

Genera y muestra la gráfica de la distribución de tipos de partículas.

**Descripción**:
- Llama a la función `crear_dataframe` para generar un DataFrame de partículas.
- Llama a la función `graficar_distribucion_tipos` para generar la gráfica de la distribución.
- Muestra la gráfica generada en la interfaz.


##### `show_plot(self, filename)`

Muestra una gráfica en la interfaz.

- **Argumentos**:
  - `filename`: El nombre del archivo de la gráfica que debe mostrarse en la interfaz.

**Descripción**:
Carga la imagen de la gráfica desde el archivo especificado y la muestra en un `QLabel` en la interfaz gráfica.



### **Explicación de la Interfaz Gráfica**

La interfaz gráfica está basada en **PyQt5** y consta de los siguientes elementos:

1. **Logo**: Se muestra en la parte superior de la ventana, con un tamaño reducido a 150x150 píxeles.
2. **Lista de partículas**: Un `QListWidget` que permite al usuario seleccionar una partícula. Al seleccionar una, se muestra su nombre y masa en un `QLabel`.
3. **Botones**:
   - **"Graficar Masa"**: Muestra la masa de la partícula seleccionada en una gráfica de barras.
   - **"Graficar Distribución de Tipos"**: Muestra la distribución de tipos de partículas en una gráfica de pastel.
4. **Área de la gráfica**: Un `QLabel` que muestra las gráficas generadas, como imágenes.

