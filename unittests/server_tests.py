import unittest

from GB_pyhton_CS import server


class TestRequestHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.mq = []  # message queue required for server functions

    def test_presence(self):
        request = {'action': 'presence'}
        self.assertEqual(server.request_handler(request, self.mq)['payload'], 'presence established')

    def test_msg(self):
        request = {'action': 'msg', 'to': 'test_receiver', 'from': 'test_sender', 'message': 'test_msg'}
        self.assertEqual(server.request_handler(request, self.mq)['payload'], 'message received')
        self.assertEqual(self.mq[0]['message'], 'test_msg')

    def test_get_msgs(self):
        request = {'action': 'msg', 'to': 'test_receiver', 'from': 'test_sender', 'message': 'test_msg_1'}
        msg = request['message']
        server.request_handler(request, self.mq)
        request = {"action": "get_msgs", "user": {"username": 'test_receiver'}, }
        self.assertEqual(server.request_handler(request, self.mq)['payload'][0]['message'], msg)

    def test_empty(self):
        request = ''
        with self.assertRaises(TypeError) as e:
            server.request_handler(request, self.mq)


class TestResponseConstructor(unittest.TestCase):

    def test_response_construction(self):
        self.assertEqual(server.response_constructor('test')['payload'], 'test')

    def test_response_empty(self):
        self.assertIs(server.response_constructor()['payload'], None)
        
if __name__ == '__main__':
    unittest.main()
    
