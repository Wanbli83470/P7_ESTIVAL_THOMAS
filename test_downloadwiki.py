"""Import the wiki.py file to test the RequestWiki class
Import of Unittest and the mock and path module to test API requests
"""
import unittest
from wiki import RequestWiki
from unittest.mock import patch, Mock

# Test sans Mock


class TestWiki(unittest.TestCase):

    def setUp(self):
        """SetUp function to create class instances that will be used for testing"""
        # Instance de request Wiki
        self.response = RequestWiki()
        self.response.geo_search()
        self.info = self.response.get_adress()
        print("info = {}".format(self.info))


    def test_response(self):
        """tests of the responses http 200 or 400"""
        self.assertEqual(self.response.geo_search(), 200)

    def test_adress(self):
        """Checking the recovered address"""
        self.assertEqual(self.response.get_adress(), ("Lycée%20Honoré-d'Estienne-d'Orves", 4223656))

    def test_resume(self):
        """Test that the answer contains the relevant keywords"""
        print(type(self.response.resume(url=self.info[0], id_page=self.info[1])))
        self.assertIn("Le lycée Honoré-d’Estienne-d’Orves", self.response.resume(url=self.info[0], id_page=self.info[1]))

# class TestWikiMock(unittest.TestCase):
#     @patch('wiki.RequestWki.geo_search'):
#
#     def test_response(self, mock_):
#         mock_.return_value.status_code = 200
#         response = RequestWiki()


if __name__ == '__main__':
    unittest.main()
