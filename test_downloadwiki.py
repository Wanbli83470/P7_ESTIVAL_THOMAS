"""Import the wiki.py file to test the RequestWiki class
Import of Unittest and the mock and path module to test API requests
"""
import unittest
from wiki import RequestWiki
from unittest.mock import patch, Mock

# Test Without mock

# class TestWiki(unittest.TestCase):
#
#     def setUp(self):
#         """SetUp function to create class instances that will be used for testing"""
#         # Instance de request Wiki
#         self.response = RequestWiki()
#         self.response.geo_search()
#         self.info = self.response.get_adress()
#         print("info = {}".format(self.info))
#
#
#     def test_response(self):
#         """tests of the responses http 200 or 400"""
#         self.assertEqual(self.response.geo_search(), 200)
#
#     def test_adress(self):
#         """Checking the recovered address"""
#         self.assertEqual(self.response.get_adress(), ("Lycée%20Honoré-d'Estienne-d'Orves", 4223656))
#
#     def test_resume(self):
#         """Test that the answer contains the relevant keywords"""
#         print(type(self.response.resume(url=self.info[0], id_page=self.info[1])))
#         self.assertIn("Le lycée Honoré-d’Estienne-d’Orves", self.response.resume(url=self.info[0], id_page=self.info[1]))


# Test With Mock

class TestWikiMock(unittest.TestCase):

    def test_response(self):
        print(" \n >>> MOCK \n test_response")
        with patch('wiki.r.get') as mock_get:
            mock_get.return_value.status_code = 200
            print(mock_get)
            response = RequestWiki()
            self.assertEqual(response.geo_search(), 200)

    @patch('wiki.RequestWiki.get_adress')
    def test_adress(self, mock_get_adress):
        print(" \n >>> MOCK \n test_adress")
        #On se sert de ce JSON inventé
        lieux = {"lieux": 'lieux_ok'}
        mock_get_adress = Mock()
        mock_get_adress.return_value.json.return_value = lieux
        #On instancie la classe et sa méthode
        lieu = 'lieux_ok'
        # On procède au test
        self.assertIn(lieu, lieux)


if __name__ == '__main__':
    unittest.main()
