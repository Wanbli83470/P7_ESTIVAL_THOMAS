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

        users = {
   "results" : [
      {
         "address_components" : [
            {
               "long_name" : "1600",
               "short_name" : "1600",
               "types" : [ "street_number" ]
            },
            {
               "long_name" : "Amphitheatre Pkwy",
               "short_name" : "Amphitheatre Pkwy",
               "types" : [ "route" ]
            },
            {
               "long_name" : "Mountain View",
               "short_name" : "Mountain View",
               "types" : [ "locality", "political" ]
            },
            {
               "long_name" : "Santa Clara County",
               "short_name" : "Santa Clara County",
               "types" : [ "administrative_area_level_2", "political" ]
            },
            {
               "long_name" : "California",
               "short_name" : "CA",
               "types" : [ "administrative_area_level_1", "political" ]
            },
            {
               "long_name" : "United States",
               "short_name" : "US",
               "types" : [ "country", "political" ]
            },
            {
               "long_name" : "94043",
               "short_name" : "94043",
               "types" : [ "postal_code" ]
            }
         ],
         "formatted_address" : "1600 Amphitheatre Parkway, Mountain View, CA 94043, USA",
         "geometry" : {
            "location" : {
               "lat" : 37.4224764,
               "lng" : -122.0842499
            },
            "location_type" : "ROOFTOP",
            "viewport" : {
               "northeast" : {
                  "lat" : 37.4238253802915,
                  "lng" : -122.0829009197085
               },
               "southwest" : {
                  "lat" : 37.4211274197085,
                  "lng" : -122.0855988802915
               }
            }
         },
         "place_id" : "ChIJ2eUgeAK6j4ARbn5u_wAGqWA",
         "types" : [ "street_address" ]
      }
   ],
   "status" : "OK"
}

        # Start patching 'requests.get'.
        mock_get = mock_get_patcher.start()

        # Configure the mock to return a response with status code 200 and a list of users.
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = users
        print(mock_get)
        # Call the service, which will send a request to the server.
        response = RequestWiki()
        # Stop patching 'requests'.

        # Assert that the request-response cycle completed successfully.
        self.assertEqual(response.geo_search(), 200)

        mock_get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
