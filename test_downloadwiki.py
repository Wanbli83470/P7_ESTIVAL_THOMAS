"""Import the wiki.py file to test the RequestWiki class
Import of Unittest and the mock and path module to test API requests
"""
import unittest
from wiki import RequestWiki
from unittest.mock import patch, Mock
import json


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


class MockTestWiki(unittest.TestCase):

    def test_api_velodrome(self):
        """Mocking with json file local"""
        mock_get_patcher = patch('wiki.r.get')
        get_file = open('json/json_wiki_1.json', 'r')
        json_file = json.load(get_file)
        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = json_file
        print(mock_get)
        # Call the service, which will send a request to the server.
        response = RequestWiki(lat=43.269827, lng=5.395887300000001)
        # Stop patching 'requests'.

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.geo_search(), 200)
        self.assertIn(4223656, response.get_adress())
        get_file.close()

        get_file = open('json/json_wiki_2.json', 'r')
        json_file = json.load(get_file)
        mock_get.return_value.json.return_value = json_file

        self.assertIn("Le stade Vélodrome", response.resume(id_page=153581, url="Stade%20Vélodrome"))
        get_file.close()

        mock_get_patcher.stop()

    def test_api_basilique(self):
        """Mocking with json file local"""
        mock_get_patcher = patch('wiki.r.get')
        get_file = open('json/json_wiki_3.json', 'r')
        json_file = json.load(get_file)
        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = json_file
        print(mock_get)
        # Call the service, which will send a request to the server.
        response = RequestWiki(lat=43.4527228, lng=5.8634467)
        # Stop patching 'requests'.

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.geo_search(), 200)
        self.assertIn(1450977, response.get_adress())
        get_file.close()

        get_file = open('json/json_wiki_4.json', 'r')
        json_file = json.load(get_file)
        mock_get.return_value.json.return_value = json_file

        self.assertIn("La basilique", response.resume(id_page=1450977, url="Basilique%20Sainte-Marie-Madeleine%20de%20Saint-Maximin-la-Sainte-Baume"))
        get_file.close()

        mock_get_patcher.stop()

    def test_api_Sagrada_familia(self):
        """Mocking with json file local"""
        mock_get_patcher = patch('wiki.r.get')
        get_file = open('json/json_wiki_5.json', 'r')
        json_file = json.load(get_file)
        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = json_file
        print(mock_get)
        # Call the service, which will send a request to the server.
        response = RequestWiki(lat=41.4036299, lng=2.1743558)
        # Stop patching 'requests'.

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.geo_search(), 200)
        self.assertIn(56154, response.get_adress())
        get_file.close()

        get_file = open('json/json_wiki_6.json', 'r')
        json_file = json.load(get_file)
        mock_get.return_value.json.return_value = json_file

        self.assertIn('La Sagrada Família, Temple Expiatori de la Sagrada Família', response.resume(id_page=56154, url="Sagrada%20Família"))
        get_file.close()

        mock_get_patcher.stop()



if __name__ == '__main__':
    unittest.main()
