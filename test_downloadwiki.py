import unittest
from wiki_wrapper import RequestWiki
from unittest.mock import patch, Mock

class TestWiki(unittest.TestCase):

	@patch('wiki_wrapper.RequestWiki.geo_search')
	def testStatus(self, mock_code):

		# MOCK
		mock_code.return_value.status_code = 200
		# TEST
		instance = RequestWiki()
		http = instance.geo_search()
		print(http)
		assert http.status_code == 200


	@patch('wiki_wrapper.RequestWiki.resume')
	def testResume(self, mock_resume):
		# MOCK
		mock_resume.return_value.data = ['Stade Vélodrome', 'Marseille Genocide Memorial']
		# TEST
		instance = RequestWiki()

		data = instance.resume()
		assert data == ['Stade Vélodrome', 'Marseille Genocide Memorial']



	# def setUp(self):
	# 	print("setUp")
	# 	self.result = RequestWiki()

	# def testData(self):
	# 	print("Test Data")
	# 	self.assertEqual(self.result.geo_search(), None)

if __name__ == '__main__':
	unittest.main()