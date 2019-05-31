"""Import the wiki.py file to test the RequestWiki class
Import of Unittest and the mock and path module to test API requests
"""
import unittest
from wiki import RequestWiki
from unittest.mock import patch, Mock
import json


# Travail du format json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#Conversion en JSON

x_json = json.dumps(x)

print(type(x_json))


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


class BasicTests(unittest.TestCase):

    def test_mock_whole_function(self):
        """Mocking a whole function"""
        mock_get_patcher = patch('wiki.r.get')
        get_file = open('json_wiki_1.json', 'r')
        json_file = json.load(get_file)
        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = json_file
        print(mock_get)
        # Call the service, which will send a request to the server.
        response = RequestWiki()
        # Stop patching 'requests'.

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.geo_search(), 200)
        self.assertIn(4223656, response.get_adress())
        get_file.close()

        get_file = open('json_wiki_2.json', 'r')
        json_file = json.load(get_file)
        mock_get.return_value.json.return_value = json_file

        self.assertIn("Le stade Vélodrome", response.resume(id_page=153581, url="Stade%20Vélodrome"))

        mock_get_patcher.stop()



if __name__ == '__main__':
    unittest.main()
