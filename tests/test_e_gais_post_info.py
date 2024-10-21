import unittest
from controllers.e_gais_post_info import EGAISPostInfo
from controllers.e_gais_request import EGAISRequest
from controllers.e_gais_extended_request import EGAISExtendedRequest
from controllers.e_gais_info_request import EGAISInfoRequest
from settings import requestid,token,blistRegionCodes,bregionCode,brole
import logging
import urllib3
import json
import requests
import datetime
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
        self.request_extended  = EGAISExtendedRequest(self.base_url)
        self.request_info = EGAISInfoRequest(self.base_url) 
        try:
            with open('test_args.json') as f:
                self.params = json.load(f)
            self.license_id = requestid
            if token=="":
                self.token = self.get_token()
                logger.info(f"Получили токен {self.token}")
            else:
                self.token=token
        except Exception as e:
            logger.error(f"test_create_sand_license ERROR {e}")
            print(f"An error occurred: {e}")
        current_date = datetime.date.today()
        self.date_string = current_date.strftime("%Y-%m-%d")

    def test_make_request(self):      
        # self.get_token()
        test_post_info_request_id = self.params.get('test_post_info_request_id', 3)
        if self.token is None:
            logging.error(f"test_json_structure token {self.token} is None")
        # Выполняем extended request
        self.request_extended.make_request(test_post_info_request_id,self.token)
        # Выполняем info request
        self.request_info.make_request(test_post_info_request_id,self.token)
        
        response_json = self.request_instance.make_request(test_post_info_request_id, self.token)
        if response_json is None:
            self.fail("Response text is None")
            logging.info("Response text is None")
        logging.info(f"Response {response_json}")
        if response_json is None:
            self.fail("Response text is None")
