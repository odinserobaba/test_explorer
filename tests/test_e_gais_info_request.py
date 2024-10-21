import unittest
from controllers.e_gais_post_info import EGAISPostInfo
from controllers.e_gais_request import EGAISRequest
from settings import requestid,token,blistRegionCodes,bregionCode,brole
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


class TestEGAISPostInfo(unittest.TestCase):
    
    def get_token(self):
        token_base_url = 'https://lk-test.egais.ru/api-lc-license/tools/token'   
        logger.info(f"get_token {brole} {bregionCode} {blistRegionCodes} {blistRegionCodes}")
        token_request_instance = EGAISRequest(token_base_url)
        try:
            token = token_request_instance.make_request(blistRegionCodes, bregionCode, brole)
            print(f"Token: {token}")
            return token
        except Exception as e:
            logger.error(f"get_token ERROR {e}")
            print(f"An error occurred: {e}")
    
    
    def setUp(self):
        self.base_url = 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request'
        self.request_instance = EGAISPostInfo(self.base_url)
        self.license_id = requestid
        if token=="":
            self.token = self.get_token()
            logger.info(f"Получили токен {self.token}")
        else:
            self.token=token
        # self.jsessionid = '2D76793EF3BDCC914ECF896C887FB2AA'
        
        

    def test_make_request(self):
        self.get_token()
        if self.token is None:
            logging.error(f"test_json_structure token {self.token} is None")
        response = self.request_instance.make_request(self.license_id, self.token)
        
