import unittest
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import models

class TestExperiment(unittest.TestCase):

    def test_default_generate(self):
        e = models.Experiment()
        # print e.generate()
        self.assertEqual(len(e.generate()), 60)

    def test_generate_1(self):
        e = models.Experiment()
        self.assertEqual(len(e.generate(num_trials = 15, data_type = 'alpha',
                                        matrix_size = 3)), 60)

    def test_generate_2(self):
        e = models.Experiment()
        self.assertEqual(len(e.generate(num_trials = 5, data_type = 'alpha',
                                        matrix_size = 3)), 20)

    def test_generate_3(self):
        e = models.Experiment()
        self.assertEqual(len(e.generate(num_trials = 5, data_type = 'alpha',
                                        matrix_size = 4)), 20)

if __name__ == '__main__':
    unittest.main()
