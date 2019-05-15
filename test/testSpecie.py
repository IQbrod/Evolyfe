import unittest
from specie import Specie

class TestSpecie(unittest.TestCase):
    def setUp(self):
        self.stable_nobirth = Specie("Stable_NoBirth",0,0.02,0.02)
        self.stable = Specie("Stable",0.2,0.025,0.03)
        self.continuous = Specie("Continuous",0,0.5,0.2)
        self.extinction = Specie("Extinction",0,0.2,0.4)
        self.continuous_carryingcap = Specie("Continuous_CarryingCapacity",0,0.03,0.02,0.0001)

    def test_equilibrium(self):
        self.assertEqual(self.stable_nobirth.equilibrium(), -1, "Stable & NoBirth should reach -1")
        self.assertTrue(self.stable.equilibrium() > 0, "Stable should reach > 1")
        self.assertEqual(self.continuous.equilibrium(), -1, "Continuous should reach -1")
        self.assertEqual(self.extinction.equilibrium(), 0, "Extinction should reach 0")
        self.assertEqual(self.continuous_carryingcap.equilibrium(), -1, "Stable & NoBirth should reach -1")