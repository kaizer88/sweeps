from app import app
import unittest


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)

    # check if response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/api")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # checking id content return is application/json
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/api")
        self.assertEqual(response.content_type, "application/json")


if __name__ == '__main__':
    unittest.main()
