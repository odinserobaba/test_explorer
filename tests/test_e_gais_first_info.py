import unittest
import json
from controllers.e_gais_extended_request import EGAISExtendedRequest
from controllers.e_gais_info_request import EGAISInfoRequest
from controllers.e_gais_request import EGAISRequest
from settings import token,requestid,blistRegionCodes,bregionCode,brole,blistRegionCodes
import logging
import urllib3
urllib3.disable_warnings()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class TestEGaisFirstInfo(unittest.TestCase):

    def get_token(self):
        token_base_url = 'https://lk-test.egais.ru/api-lc-license/tools/token'   
        logger.info(f"get_token {brole} {bregionCode} {blistRegionCodes} {blistRegionCodes}")
        token_request_instance = EGAISRequest(token_base_url)
        try:
            token = token_request_instance.make_request(blistRegionCodes, bregionCode, brole)
            print(f"Token: {token}")
            return token
        except Exception as e:
            print(f"An error occurred: {e}")
    

    def setUp(self):
        self.request_id = 225358
        self.res_file='test_13_10.md'
        self.base_url = 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request'
        self.request_extended_instance = EGAISExtendedRequest(self.base_url)
        self.request_info_instance = EGAISInfoRequest(self.base_url)
        self.license_id = requestid
        if token=="":
            self.token = self.get_token()
            logger.info(f"Получили токен {self.token}")
        else:
            self.token=token
        # self.jsessionid = '2D76793EF3BDCC914ECF896C887FB2AA'


    def test_base_info_request(self):
        logger.info(f"test_base_info_request -> request_id {self.request_id}")
        self.request_extended_instance.make_request(self.request_id,self.token)
        # self.request_info_instance.make_request(self.request_id,self.token)

if __name__ == '__main__':
    unittest.main()
