import unittest

from controllers.e_gais_request import EGAISRequest
from settings import requestid, token, blistRegionCodes, bregionCode, brole
import logging
import urllib3
import json
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


class TestEGAISIRequest(unittest.TestCase):
    def setUp(self):
        logger.info(f"Запускаем тест test_create_sand")
        self.sand_license = EGAISRequest("")
        try:
            with open('test_args.json') as f:
                self.params = json.load(f)
        except Exception as e:
            logger.error(f"test_create_sand_license ERROR {e}")
            print(f"An error occurred: {e}")
        current_date = datetime.date.today()
        self.date_string = current_date.strftime("%Y-%m-%d")

    def test_create_sand_license(self, inn='7841051711', license_type_code=9, request_type_code=7, orgBriefName='ООО "ЗХП_АП "', orgFullName='ООО "ЗХП_АП "'):
        try:
            license_type_code = self.params.get('sand_license_create_license_type_code', 3)
            request_type_code = self.params.get('sand_license_create_request_type_code', 7)
            message = self.params.get('sand_license_create_message', "")
            log_path = self.params.get('log_path', "./save_report")+f"/{self.date_string}"
            logger.info(f"Тест test_create_sand license_type_code = {license_type_code} request_type_code = {request_type_code}")
            result = self.sand_license.run_http_requests_on_remote(
                inn='7841051711', license_type_code=license_type_code, request_type_code=request_type_code, orgBriefName='ООО "ЗХП_АП "', orgFullName='ООО "ЗХП_АП "')
            
            # Если нет папки создадим ее
            logger.info(f"Тест test_create_sand {log_path}")
            if not os.path.exists(log_path):
                logger.info(f"Тест test_create_sand создаем папку {log_path}")
                os.makedirs(log_path)
            save_jsons_context(context=result[0], output_file=log_path, message=message)
            self.assertEqual(True,True)
        except Exception as e:
            logger.error(f"test_create_sand_license ERROR {e}")
            print(f"An error occurred: {e}")   
