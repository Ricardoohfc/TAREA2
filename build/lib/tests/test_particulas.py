import unittest
from Modelo_Estandar.particulas import Particula

class TestParticula(unittest.TestCase):
    def setUp(self):
        self.electron = Particula("Electrón", "lepton", -1, 0.511)

    def test_mostrar_info(self):
        info = self.electron.mostrar_info()
        self.assertIn("Electrón", info)
        self.assertIn("lepton", info)
        self.assertIn("-1 e", info)
        self.assertIn("0.511 MeV/c^2", info)

if __name__ == '__main__':
    unittest.main()
