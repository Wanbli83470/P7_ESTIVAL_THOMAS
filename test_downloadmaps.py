"""Import the gmaps file to test the RequestMap class
Import of Unittest and the mock and path module to test API requests
"""
import unittest
from unittest.mock import patch, Mock
from gmaps import RequestMap
import json
# Test Without mock


class TestMaps(unittest.TestCase):

    """Using the unittest module to check the responses of the gmaps.py file"""

    def setUp(self):
        """SetUp function to create class instances that will be used for testing"""
        self.response = RequestMap(words="versaille")


    def test_form_input(self):
        """test the type of user input >>> str """
        self.assertIs(type(self.response.words), str)

    def test_file_format(self):
        pass

# with mock


class MockTestMaps(unittest.TestCase):

    def test_mock_data(self):
        """Mocking a whole function"""
        mock_get_patcher = patch('gmaps.search.get')
        get_file = open('json_maps_1.json', 'r')
        json_file = json.load(get_file)

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = json_file

        # Call the service, which will send a request to the server.
        response = RequestMap()


        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.response(), 200)
        self.assertIn("78000 Versailles, France", response.get_adress())
        self.assertEqual((48.801408, 2.130122), response.get_location())
        # Close the processus
        mock_get_patcher.stop()
        get_file.close()


if __name__ == '__main__':
    unittest.main()
