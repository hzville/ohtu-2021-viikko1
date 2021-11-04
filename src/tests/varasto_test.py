import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)
        
        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uusi_varasto_negatiivinen_tilavuus(self):
        varasto = Varasto(-1)
        self.assertEqual(varasto.tilavuus, 0)

    def test_uusi_varasto_negatiivinen_alkusaldo(self):
        varasto = Varasto(0, -1)
        self.assertEqual(varasto.saldo, 0)

    def test_lisaa_varastoon_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_yli_tilaavudeen(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, 10)
        
    def test_ota_varastosta_nega(self):
        self.assertEqual(self.varasto.ota_varastosta(-5), 0.0)

    def test_ota_varastosta_yli_saldon(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(self.varasto.ota_varastosta(15), 10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_print(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10" )