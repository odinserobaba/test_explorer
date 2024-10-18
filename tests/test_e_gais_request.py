import unittest

from controllers.e_gais_request import EGAISRequest
from settings import requestid, token, blistRegionCodes, bregionCode, brole
import logging
import urllib3
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
        self.sand_license= EGAISRequest("")
       
    def test_create_sand_license(self, inn='7841051711', license_type_code=9, request_type_code=7, orgBriefName='ООО "ЗХП_АП "', orgFullName='ООО "ЗХП_АП "'):
        result=self.sand_license.run_http_requests_on_remote(inn='7841051711', license_type_code=9, request_type_code=7, orgBriefName='ООО "ЗХП_АП "', orgFullName='ООО "ЗХП_АП "')
        self.assertIsNotNone(result)