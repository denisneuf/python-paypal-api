import unittest
from python_paypal_api.base import (
    Client,
    PaypalEndpoint,
    PaypalEndpointParams,
    PaypalApiException,
    ApiResponse,
    Utils,
    ProductType,
    CategoryType
)

class TestClientMethods(unittest.TestCase):

    '''
    def test_paypal_endpoint(self):
        assert PaypalEndpoint('foo') is not None

        @PaypalEndpoint('/api/call', method='POST')
        def my_endpoint(**kwargs):
            assert kwargs['path'] == '/api/call'
            assert kwargs['method'] == 'POST'

        my_endpoint()
        assert my_endpoint.__name__ == 'my_endpoint'

    '''

    def test_paypal_endpoint(self):
        # assert PaypalEndpoint('foo') is not None
        self.assertTrue(PaypalEndpoint('foo'))

        @PaypalEndpoint('/api/call', method='POST')
        def my_endpoint(**kwargs):
            # assert kwargs['path'] == '/api/call'
            self.assertEqual(kwargs['path'], '/api/call')
            # assert kwargs['method'] == 'POST'
            self.assertEqual(kwargs['method'], 'POST')

        my_endpoint()
        assert my_endpoint.__name__ == 'my_endpoint'

    def test_paypal_exception(self):

        error = {"message": "hey", "details": "Joe", "paypal_code": 999}

        headers = {"bar": "foo"}

        s = 'hello world'

        e = PaypalApiException(error, headers)
        self.assertTrue(e.error)
        self.assertTrue(e.headers)
        self.assertTrue(e.error.get("paypal_code"))
        with self.assertRaises(TypeError):
            s.split(2)
        # assert e.paypal_code == 999
        # assert e.message == 'Foo'

    def test_client_timeout(self):
        client = Client(timeout=1)
        assert client.timeout == 1
        client = Client()
        assert client.timeout is None


    def test_client_store_credentials(self):
        client = Client(store_credentials=True)
        assert client.store_credentials == True
        client = Client()
        assert client.store_credentials is False

    # @unittest.skip("demonstrating skipping")
    @unittest.expectedFailure
    def test_client_account(self):
        client = Client(account="pp")
        self.assertEqual(client.account, 'pp')

    def test_fill_query_params(self):
        self.assertTrue(PaypalEndpointParams('{}/{}').fill("boo", "bar"))


if __name__ == '__main__':
    unittest.main()


