import unittest
from controllers.e_gais_request import EGAISRequest
import urllib3
urllib3.disable_warnings()
class TestEGAISRequest(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://lk-test.egais.ru/api-lc-license/tools/token'
        self.request_instance = EGAISRequest(self.base_url)

    def test_make_request(self):
        listRegionCodes = 77
        regionCode = 77
        role = 'develop'

        token = self.request_instance.make_request(listRegionCodes, regionCode, role)
        self.assertIsNot(token,None)
        # self.assertTrue(token.startswith('beaver'))
        # self.assertIn('beaver', token.lower()) //TODO добавить 
