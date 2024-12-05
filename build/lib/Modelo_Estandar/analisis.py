
import matplotlib.pyplot as plt

def crear_dataframe(particles):
    data = {
        "Nombre": [p.nombre for p in particles.values()],
        "Tipo": [p.tipo for p in particles.values()],
        "Carga (e)": [p.carga for p in particles.values()],
        "Masa (MeV/c^2)": [p.masa for p in particles.values()],
        "Carga de Color": [p.carga_color for p in particles.values()],
        "Sabor": [p.sabor for p in particles.values()]
    }
    df = pd.DataFrame(data)
    df["Masa (MeV/c^2)"] = pd.to_numeric(df["Masa (MeV/c^2)"], errors="coerce")  # Convierte a numérico
    df = df.dropna(subset=["Masa (MeV/c^2)"])  # Elimina filas con valores no válidos
    return df

def graficar_masa(df, filename="masa.png"):
    print(df)
    df.plot(kind='bar', x='Nombre', y='Masa (MeV/c^2)', legend=False, color='skyblue')
    plt.title("Masa de las Partículas del Modelo Estándar")
    plt.ylabel("Masa (MeV/c^2)")
    plt.xlabel("Partícula")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def graficar_distribucion_tipos(df, filename="distribucion_tipos.png"):
    df['Tipo'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title("Distribución de Tipos de Partículas")
    plt.ylabel("")
    plt.savefig(filename)
    plt.close()
