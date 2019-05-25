import unittest
from wiki import RequestWiki
from unittest.mock import patch, Mock



class TestWiki(unittest.TestCase):

    def test_response(self):
        response = RequestWiki()
        self.assertEqual(response.geo_search(), 200)

    def






if __name__ == '__main__':
    unittest.main()




