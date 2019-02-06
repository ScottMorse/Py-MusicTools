import unittest
from pymusician import notate

class TestTempoClass(unittest.TestCase):

    def test_initialization(self):

        notate.Tempo(60)
        notate.Tempo(1)
        notate.Tempo(100.5)

        with self.assertRaises(ValueError):
            notate.Tempo(0)
        with self.assertRaises(ValueError):
            notate.Tempo(-1)
        with self.assertRaises(ValueError):
            notate.Tempo("1")

    def test_bpm_setter(self):

        tempo = notate.Tempo(60)

        self.assertEqual(tempo.spb,1)

        tempo.bpm = 120

        self.assertEqual(tempo.spb,0.5)

        with self.assertRaises(ValueError):
            tempo.bpm = "1"
        with self.assertRaises(ValueError):
            tempo.bpm = 0
        with self.assertRaises(ValueError):
            tempo.bpm = -1

if __name__ == "__main__":

    unittest.main()