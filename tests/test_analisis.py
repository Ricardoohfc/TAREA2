#Importar funciones del módulo analisis y la clase Particula
from Modelo_Estandar.analisis import crear_dataframe
from Modelo_Estandar.particulas import Particula

def test_crear_dataframe():
    #Crear partículas de prueba
    particles = {
        'electron': Particula("Electrón", "lepton", -1, 0.51099895000),
        'photon': Particula("Fotón", "boson", 0, 0)
    }

    #Crear un DataFrame
    df = crear_dataframe(particles)

    #Verificar que el DataFrame no esté vacío
    assert not df.empty

    #Verificar el contenido del DataFrame
    assert df.iloc[0]["Nombre"] == "Electrón"
    assert df.iloc[0]["Tipo"] == "lepton"
    assert df.iloc[1]["Nombre"] == "Fotón"
    assert df.iloc[1]["Tipo"] == "boson"
