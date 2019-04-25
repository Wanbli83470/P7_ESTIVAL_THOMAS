"""we import unittest to test the parsing
we import the parsing file as a 'script' to standardize our tests"""
import unittest
from parse import Parsing as script

class TestParsing(unittest.TestCase):
    """In TDD we write the result that we want to obtain with a test class
    to avoid repeating the code, we register a class instance as soon as we start the test"""
    def setUp(self):
        print("setUp")
        self.question = script("""Salut Grand Py est-ce que tu connais 
        adresse openclassrooms""", nb_letter=6)
        self.question2 = script("""Peux tu me donner l'adresse de la 
        basilique de Saint-Maximin""", nb_letter=6)
        self.question3 = script("Ou se trouve le château de Versaille", nb_letter=6)
        self.question4 = script("l'emplacement du parc Astérix", nb_letter=3)
        self.question5 = script("J'aimerais voir Le stade de Manchester", nb_letter=4)

    def test_parse(self):
        """Test all the examples initiated in the setup"""
        print("Test Parse")
        self.assertEqual(self.question.parser(), "adresse openclassrooms ")
        self.assertEqual(self.question2.parser(), "adresse basilique saint-maximin ")
        self.assertEqual(self.question3.parser(), "château versaille ")
        self.assertEqual(self.question4.parser(), "parc astérix ")
        self.assertEqual(self.question5.parser(), "stade manchester ")

if __name__ == '__main__':
    unittest.main()