import unittest
from gmaps import RequestMap
from unittest.mock import patch, Mock

# Without mock
class TestMaps(unittest.TestCase):

    def setUp(self):
        self.response = RequestMap(words="versaille")
        self.response2 = RequestMap(words="Stade vélodrome")
        self.response3 = RequestMap(words="Basilique Saint-maximin")
        self.response4 = RequestMap(words="")

    def test_form_input(self):
        self.assertIs(type(self.response.words), str)

    def test_response(self):
        self.assertEqual(self.response.response(), 200)
        self.assertEqual(self.response2.response(), 200)
        self.assertEqual(self.response3.response(), 200)
        self.assertEqual(self.response4.response(), 400)

    def test_adress(self):
        self.assertEqual(self.response.get_adress(), "78000 Versailles, France")
        self.assertEqual(self.response2.get_adress(), "3 Boulevard Michelet, 13008 Marseille, France")
        self.assertEqual(self.response3.get_adress(), "10 Place de L Hôtel de ville, 83470 Saint-Maximin-la-Sainte-Baume, France")
        self.assertRaises(self.response4.get_adress(),IndexError)

    def test_coordinates(self):
        self.assertEqual(self.response.get_location(), (48.801408, 2.130122))
        self.assertEqual(self.response2.get_location(), (43.269827, 5.395887300000001))
        self.assertEqual(self.response3.get_location(), (43.4527228, 5.8634467))
        self.assertRaises(self.response4.get_location(), IndexError)

    def test_format_json(self):
        pass
# with mock



if __name__ == '__main__':
    unittest.main()




