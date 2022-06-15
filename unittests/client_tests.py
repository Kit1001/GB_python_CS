import unittest

from GB_pyhton_CS import client


class TestResponseHandler(unittest.TestCase):

    def test_response_200(self):
        response = {
            "response": 200,
            "time": None,
            "payload": 'test payload'
        }
        result = client.response_handler(response)
        self.assertEqual(result, 'test payload')

    def test_response_non_200(self):
        response = {
            "response": 400,
            "time": None,
            "payload": 'test payload'
        }
        with self.assertRaises(ValueError) as e:
            client.response_handler(response)

    def test_response_empy(self):
        response = ''
        with self.assertRaises(TypeError) as e:
            client.response_handler(response)


class TestMessageConstructor(unittest.TestCase):

    def test_message_construction(self):
        # print(client.message_constructor())
        args = 'test', 'test', 'test'
        message = {'action': 'msg', 'to': 'test', 'from': 'test', 'message': 'test'}
        self.assertEqual(client.message_constructor(*args), message)


class TestPresenceConstructor(unittest.TestCase):

    def test_presence_constructor(self):
        args = 'test_name', 'test_status'
        presence = {"action": "presence", "type": "status",
                    "user": {"account_name": 'test_name', "status": 'test_status'}}
        self.assertEqual(client.presence_constructor(*args), presence)


if __name__ == '__main__':
    unittest.main()
