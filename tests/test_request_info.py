import unittest
from settings import requestid, token, blistRegionCodes, bregionCode, brole
import logging
import urllib3
import json
import requests
import os
import datetime
from utils.utils import save_jsons_context,save_jsons_context
urllib3.disable_warnings()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class TestRequestInfo(unittest.TestCase):
    def setUp(self):
        logger.info(f"Запускаем тест TestRequestInfo")
        try:
            with open('tests.json') as f:
                self.params = json.load(f)
        except Exception as e:
            logger.error(f"TestRequestInfo ERROR {e}")
            print(f"An error occurred: {e}")
        current_date = datetime.date.today()
        self.date_string = current_date.strftime("%Y-%m-%d")
        logger.info(f"TestRequestInfo date string {self.date_string}")
    def test_request_info(self):
        request_id = self.params.get('test_request_info_request_id', 225494)
        test_request_info_log_path= self.params.get('test_request_info_log_path', "./save_report")
        test_request_info_message= self.params.get('test_request_info_log_path', "tests_task")
        test_request_info_task= self.params.get('test_request_info_task','123123')
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {token}',
        }
        response = requests.get(f'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/{request_id}/info', headers=headers, verify=False)    
        logger.info(f'TestRequestInfo request_id {request_id} token {token} date_string {self.date_string}')
        logger.info(f"TestRequestInfo response {response}")
        logger.info(f"TestRequestInfo response {response.json()}")
        # Если нет папки создадим ее
        test_request_info_log_path = test_request_info_log_path + '/'+self.date_string
        logger.info(f"TestRequestInfo {test_request_info_log_path}")
        if not os.path.exists(test_request_info_log_path):
            logger.info(f"TestRequestInfo создаем папку {test_request_info_log_path}")
            os.makedirs(test_request_info_log_path)
        file_name =test_request_info_log_path+'/'+f'{test_request_info_task}.md'
        logger.info(f"TestRequestInfo сохраняем в файл {file_name}")
        save_jsons_context(response.json(),file_name,test_request_info_message)
        
class TestRequestExtended(unittest.TestCase):
    def setUp(self):
        logger.info(f"Запускаем тест TestRequestInfo")
        try:
            with open('tests.json') as f:
                self.params = json.load(f)
        except Exception as e:
            logger.error(f"TestRequestInfo ERROR {e}")
            print(f"An error occurred: {e}")
        current_date = datetime.date.today()
        self.date_string = current_date.strftime("%Y-%m-%d")
        logger.info(f"TestRequestInfo date string {self.date_string}")
    def test_request_extended(self):
        request_id = self.params.get('test_request_extended_request_id', 225494)
        test_request_info_log_path= self.params.get('test_request_extended_log_path', "./save_report")
        test_request_info_message= self.params.get('test_request_extended_log_path', "tests_task")
        test_request_info_task= self.params.get('test_request_extended_task','123123')
        headers = {
            'accept': '*/*',
            'Authorization': f'Bearer {token}',
        }
        response = requests.get(f'https://lk-test.egais.ru/api-lc-license/dashboard/license/request/{request_id}/extended', headers=headers, verify=False)    
        logger.info(f'TestRequestExtended request_id {request_id} token {token} date_string {self.date_string}')
        logger.info(f"TestRequestExtended response {response}")
        logger.info(f"TestRequestExtended response {response.json()}")
        # Если нет папки создадим ее
        test_request_info_log_path = test_request_info_log_path + '/'+self.date_string
        logger.info(f"TestRequestExtended {test_request_info_log_path}")
        if not os.path.exists(test_request_info_log_path):
            logger.info(f"TestRequestExtended создаем папку {test_request_info_log_path}")
            os.makedirs(test_request_info_log_path)
        file_name =test_request_info_log_path+'/'+f'{test_request_info_task}.md'
        logger.info(f"TestRequestExtended сохраняем в файл {file_name}")
        save_jsons_context(response.json(),file_name,test_request_info_message)