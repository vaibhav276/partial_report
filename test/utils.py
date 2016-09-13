import unittest
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.utils import encrypt_password, verify_password, count_matches

class TestUtils(unittest.TestCase):

    def test_encrypt_password(self):
        password = 'test'
        self.assertNotEqual(encrypt_password(password), password)

    def test_verify_password(self):
        password = 'test'
        encrypted_password = encrypt_password(password)
        self.assertTrue(verify_password(password, encrypted_password))

    def test_count_matches_1(self):
        matrix = 'ABHGKLIPO'
        size = 3
        cue_row = 1
        response = 'ABH'

        self.assertEqual(count_matches(matrix = matrix, size = size,
                                       cue_row = cue_row, response = response),
                        3)

    def test_count_matches_2(self):
        matrix = 'ABHGKLIPO'
        size = 3
        cue_row = 2
        response = 'GKL'

        self.assertEqual(count_matches(matrix = matrix, size = size,
                                       cue_row = cue_row, response = response),
                        3)

    def test_count_matches_3(self):
        matrix = 'ABHGKLIPO'
        size = 3
        cue_row = 3
        response = 'IPO'

        self.assertEqual(count_matches(matrix = matrix, size = size,
                                       cue_row = cue_row, response = response),
                        3)

    def test_count_matches_1_1(self):
        matrix = 'ABHGKLIPO'
        size = 3
        cue_row = 1
        response = 'AXY'

        self.assertEqual(count_matches(matrix = matrix, size = size,
                                       cue_row = cue_row, response = response),
                        1)

    def test_count_matches_2_2(self):
        matrix = 'ABHGKLIPO'
        size = 3
        cue_row = 2
        response = 'GKO'

        self.assertEqual(count_matches(matrix = matrix, size = size,
                                       cue_row = cue_row, response = response),
                        2)

    def test_count_matches_2_2(self):
        matrix = 'ABHGKLIPO'
        size = 3
        cue_row = 2
        response = 'YKL'

        self.assertEqual(count_matches(matrix = matrix, size = size,
                                       cue_row = cue_row, response = response),
                        2)
if __name__ == '__main__':
    unittest.main()
