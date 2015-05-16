import unittest, pyweb

class RoutesTests(unittest.TestCase):
	def setUp(self):
		self.app = pyweb.app.test_client()

	def test_should_response_hello_world_when_call_index(self):
		response = self.app.get('/hello')
		self.assertEqual(response.data, "Hello, World!")

if __name__ == '__main__':
    unittest.main()