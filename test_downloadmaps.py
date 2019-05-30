"""Import the gmaps file to test the RequestMap class
Import of Unittest and the mock and path module to test API requests
"""
import unittest
from unittest.mock import patch, Mock
from gmaps import RequestMap
import json
# Test Without mock

# class TestMaps(unittest.TestCase):
#
#     """Using the unittest module to check the responses of the gmaps.py file"""
#
#     def setUp(self):
#         """SetUp function to create class instances that will be used for testing"""
#         self.response = RequestMap(words="versaille")
#         self.response2 = RequestMap(words="Stade vélodrome")
#         self.response3 = RequestMap(words="Basilique Saint-maximin")
#         self.response4 = RequestMap(words="")
#
#     def test_form_input(self):
#         """test the type of user input >>> str """
#         self.assertIs(type(self.response.words), str)
#
#
#     def test_response(self):
#         """tests of the responses http 200 or 400"""
#         self.assertEqual(self.response.response(), 200)
#         self.assertEqual(self.response2.response(), 200)
#         self.assertEqual(self.response3.response(), 200)
#         self.assertEqual(self.response4.response(), 400)
#
#     def test_adress(self):
#         """Checking the recovered address"""
#         self.assertEqual(self.response.get_adress(), "78000 Versailles, France")
#         self.assertEqual(self.response2.get_adress(), "3 Boulevard Michelet, 13008 Marseille, France")
#         self.assertEqual(self.response3.get_adress(), "10 Place de L Hôtel de ville, 83470 Saint-Maximin-la-Sainte-Baume, France")
#         self.assertRaises(self.response4.get_adress(), IndexError)
#
#     def test_coordinates(self):
#         """Test of geographical coordinates obtained"""
#         self.assertEqual(self.response.get_location(), (48.801408, 2.130122))
#         self.assertEqual(self.response2.get_location(), (43.269827, 5.395887300000001))
#         self.assertEqual(self.response3.get_location(), (43.4527228, 5.8634467))
#         self.assertRaises(self.response4.get_location(), IndexError)
#
#     def test_format_json(self):
#         """Test function to check the response format obtained >>> json """
#         pass




# with mock
class BasicTests(unittest.TestCase):

    def test_mock_whole_function(self):
        """Mocking a whole function"""
        mock_get_patcher = patch('gmaps.search.get')

        users = {
            "results": [
                {
                    "address_components": [
                        {
                            "long_name": "1600",
                            "short_name": "1600",
                            "types": ["street_number"]
                        },
                        {
                            "long_name": "Amphitheatre Pkwy",
                            "short_name": "Amphitheatre Pkwy",
                            "types": ["route"]
                        },
                        {
                            "long_name": "Mountain View",
                            "short_name": "Mountain View",
                            "types": ["locality", "political"]
                        },
                        {
                            "long_name": "Santa Clara County",
                            "short_name": "Santa Clara County",
                            "types": ["administrative_area_level_2", "political"]
                        },
                        {
                            "long_name": "California",
                            "short_name": "CA",
                            "types": ["administrative_area_level_1", "political"]
                        },
                        {
                            "long_name": "United States",
                            "short_name": "US",
                            "types": ["country", "political"]
                        },
                        {
                            "long_name": "94043",
                            "short_name": "94043",
                            "types": ["postal_code"]
                        }
                    ],
                    "formatted_address": "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA",
                    "geometry": {
                        "location": {
                            "lat": 37.4224764,
                            "lng": -122.0842499
                        },
                        "location_type": "ROOFTOP",
                        "viewport": {
                            "northeast": {
                                "lat": 37.4238253802915,
                                "lng": -122.0829009197085
                            },
                            "southwest": {
                                "lat": 37.4211274197085,
                                "lng": -122.0855988802915
                            }
                        }
                    },
                    "place_id": "ChIJ2eUgeAK6j4ARbn5u_wAGqWA",
                    "types": ["street_address"]
                }
            ],
            "status": "OK"
        }

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = users

        # Call the service, which will send a request to the server.
        response = RequestMap()
        print("test get adress")

        print(response.get_adress())
        # Stop patching 'requests'.

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.response(), 400)
        self.assertIn("USA", response.get_adress())
        mock_get_patcher.stop()

if __name__ == '__main__':
    unittest.main()
