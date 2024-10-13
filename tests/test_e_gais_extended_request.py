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


class TestEGAISExtendedRequest(unittest.TestCase):

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
        self.base_url = 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request'
        self.request_instance = EGAISExtendedRequest(self.base_url)
        self.license_id = requestid
        if token=="":
            self.token = self.get_token()
            logger.info(f"Получили токен {self.token}")
        else:
            self.token=token
        # self.jsessionid = '2D76793EF3BDCC914ECF896C887FB2AA'


    def test_json_structure(self):
        self.get_token()
        if self.token is None:
            logging.error(f"test_json_structure token {self.token} is None")
        response = self.request_instance.make_request(self.license_id, self.token)
        if response is None:
            self.fail("Response text is None")
            logging.info("Response text is None")
        logging.info(f"Response {response}")
        response_json = response

        expected_keys = [
            "availableChecks",
            "availableRequestTypes",
            "canBeGenerated",
            "requestId",
            "inn",
            "organization",
            "orgBriefName",
            "orgFullName",
            "deloNum",
            "dateInsert",
            "dateChange",

            "checks",
            "deloDate",
            "licenseType",
            "attach",
            "regionCode", 
            "status",
            "indicator",

            "requestType",
            "reregTypes",
            "execUser",
            # "erulRequest",
            "finalResult",
            "suspensionSign",

            "kppNeeded", 
            "fromEpgu", 
            "checkFalse",
            "numberDaysFromRequestDateinsert", 
            "examIsActive",
            "emailNeeded",
            "mvdNeeded",
            "minselhozNeeded",
            "description",
            "requestTypeDescription",

            "statusCode", 
            "licenseTypeId",
            "requestTypeId"
]

        for key in expected_keys:
            self.assertIn(key, response_json, f"Key '{key}' is missing in the response JSON")

        # Проверка структуры вложенных объектов
        logger.info(f"Проверка структуры вложенных объектов")
        self.assertIsInstance(response_json["availableChecks"], list)
        self.assertIsInstance(response_json["checks"], list)
        self.assertIsInstance(response_json["attach"], list)
        self.assertIsInstance(response_json["licenseType"], dict)
        self.assertIsInstance(response_json["status"], dict)
        self.assertIsInstance(response_json["indicator"], dict)
        self.assertIsInstance(response_json["requestType"], dict)
        self.assertIsInstance(response_json["execUser"], dict)
        # self.assertIsInstance(response_json["erulRequest"], dict)

        # Проверка структуры вложенных объектов в availableChecks
        logger.info(f"Проверка структуры вложенных объектов в availableChecks")
        for check in response_json["availableChecks"]:
            self.assertIn("code", check)
            self.assertIn("apiOrder", check)
            self.assertIn("name", check)
            self.assertIn("groupCode", check)
            self.assertIn("upload", check)
            self.assertIn("delete", check)
            self.assertIn("deleteGenerated", check)
            self.assertIn("cluster", check)
            self.assertIn("examDoc", check)
            self.assertIn("automatic", check)
            self.assertIn("newGroupCode", check)
            self.assertIn("newGroupName", check)

        # Проверка структуры вложенных объектов в checks
        logger.info(f"Проверка структуры вложенных объектов в checks")
        for check in response_json["checks"]:
            self.assertIn("checkId", check)
            self.assertIn("requestId", check)
            self.assertIn("dateInsert", check)
            self.assertIn("code", check)
            self.assertIn("apiOrder", check)
            self.assertIn("name", check)
            self.assertIn("groupCode", check)
            self.assertIn("upload", check)
            self.assertIn("delete", check)
            self.assertIn("deleteGenerated", check)
            self.assertIn("cluster", check)
            self.assertIn("examDoc", check)
            self.assertIn("automatic", check)
            self.assertIn("newGroupCode", check)
            self.assertIn("newGroupName", check)
            self.assertIn("checkStatus", check)
            self.assertIn("autoStart", check)
            self.assertIn("error", check)

        # Проверка структуры вложенных объектов в attach
        logger.info(f"Проверка структуры вложенных объектов в attach")
        for attach in response_json["attach"]:
            self.assertIn("id", attach)
            self.assertIn("fileName", attach)
            self.assertIn("ext", attach)
            self.assertIn("type", attach)

        # Проверка структуры вложенных объектов в licenseType
        logger.info(f"Проверка структуры вложенных объектов в licenseType")
        self.assertIn("code", response_json["licenseType"])
        self.assertIn("description", response_json["licenseType"])
        self.assertIn("shortName", response_json["licenseType"])
        self.assertIn("region", response_json["licenseType"])

        # Проверка структуры вложенных объектов в status
        logger.info(f"Проверка структуры вложенных объектов в status")
        self.assertIn("code", response_json["status"])
        self.assertIn("description", response_json["status"])
        self.assertIn("initialStatus", response_json["status"])
        self.assertIn("finishedStatus", response_json["status"])

        # Проверка структуры вложенных объектов в indicator
        logger.info(f"Проверка структуры вложенных объектов в indicator")
        self.assertIn("finished", response_json["indicator"])
        self.assertIn("total", response_json["indicator"])
        self.assertIn("showPercent", response_json["indicator"])

        # Проверка структуры вложенных объектов в requestType
        logger.info(f"Проверка структуры вложенных объектов в requestType")
        self.assertIn("code", response_json["requestType"])
        self.assertIn("description", response_json["requestType"])
        self.assertIn("region", response_json["requestType"])

        # Проверка структуры вложенных объектов в execUser
        logger.info(f"Проверка структуры вложенных объектов в execUser")
        self.assertIn("id", response_json["execUser"])
        self.assertIn("firstName", response_json["execUser"])
        self.assertIn("middleName", response_json["execUser"])
        self.assertIn("lastName", response_json["execUser"])

        # Проверка структуры вложенных объектов в erulRequest
        # logger.info(f"Проверка структуры вложенных объектов в erulRequest")
        # self.assertIn("erulLicNum", response_json["erulRequest"])
        # self.assertIn("versionLic", response_json["erulRequest"])
        # self.assertIn("issueData", response_json["erulRequest"])
        # self.assertIn("erulChangeResult", response_json["erulRequest"])
        # self.assertIn("erulChangeErrorType", response_json["erulRequest"])
        # self.assertIn("errorDescription", response_json["erulRequest"])

if __name__ == '__main__':
    unittest.main()
