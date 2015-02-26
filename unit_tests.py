import unittest, app

class RoutesTests(unittest.TestCase):
    def should_response_hello_world_when_call_index(self):
        self.assertEqual(app.index(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()