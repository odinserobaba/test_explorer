import unittest
from controllers.e_gais_info_request import EGAISInfoRequest
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


class TestEGAISInfoRequest(unittest.TestCase):
    
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
        self.request_instance = EGAISInfoRequest(self.base_url)
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
        response_json = self.request_instance.make_request(self.license_id, self.token)
        if response_json is None:
            self.fail("Response text is None")
            logging.info("Response text is None")
        logging.info(f"Response {response_json}")
        if response_json is None:
            self.fail("Response text is None")

        expected_keys = [
            "requestId", "ogrn", "inn", "kpp", "orgActivityName", "orgNameBrief", "orgNameFull",
            "address", "region", "email", "comment", "rakrEntities", "rakrCerts", "phone",
            "ops", "final", "infoCadastralObjects", "cadastralObjectsIsEmpty", "notExFnsOp",
            "execUser", "mvdData", "minselhozData", "fromEpgu", "dataForRequests", "ogrnFilledFromEgrul",
            "innFilledFromEgrul", "kppFilledFromEgrul", "orgNameBriefFilledFromEgrul",
            "orgNameFullFilledFromEgrul", "addressFilledFromEgrul", "egrulData"
        ]

        for key in expected_keys:
            self.assertIn(key, response_json, f"Key '{key}' is missing in the response JSON")
            logger.info(f"Key '{key}' is present in the response JSON")

        # Проверка структуры вложенных объектов
        logger.info("Проверка структуры вложенных объектов")
        self.assertIsInstance(response_json["region"], dict)
        self.assertIsInstance(response_json["rakrEntities"], list)
        self.assertIsInstance(response_json["rakrCerts"], list)
        self.assertIsInstance(response_json["ops"], list)
        self.assertIsInstance(response_json["infoCadastralObjects"], list)
        self.assertIsInstance(response_json["execUser"], dict)
        self.assertIsInstance(response_json["dataForRequests"], dict)

        # Проверка структуры вложенных объектов в region
        logger.info("Проверка структуры вложенных объектов в region")
        self.assertIn("code", response_json["region"])
        self.assertIn("name", response_json["region"])
        self.assertIn("timeZone", response_json["region"])
        self.assertIn("active", response_json["region"])
        self.assertIn("fiasUuid", response_json["region"])
        

        # Проверка структуры вложенных объектов в rakrEntities
        for entity in response_json["rakrEntities"]:
            self.assertIn("lic_request_id", entity)
            self.assertIn("rakrEntityNumber", entity)
            logger.info("rakrEntities structure is correct")

        # Проверка структуры вложенных объектов в rakrCerts
        for cert in response_json["rakrCerts"]:
            self.assertIn("lic_request_id", cert)
            self.assertIn("rakrCertNumber", cert)
            logger.info("rakrCerts structure is correct")

        # Проверка структуры вложенных объектов в ops
        for op in response_json["ops"]:
            self.assertIn("id", op)
            self.assertIn("opId", op)
            self.assertIn("kpp", op)
            self.assertIn("address", op)
            self.assertIn("addressTail", op)
            self.assertIn("region", op)
            self.assertIn("area", op)
            self.assertIn("contractTo", op)
            self.assertIn("comment", op)
            self.assertIn("dutyFree", op)

            # Проверка структуры вложенных объектов в region внутри ops
            self.assertIn("code", op["region"])
            self.assertIn("name", op["region"])
            self.assertIn("timeZone", op["region"])
            self.assertIn("active", op["region"])
            self.assertIn("fiasUuid", op["region"])
            logger.info("Проверка структуры вложенных объектов в ops")

        # Проверка структуры вложенных объектов в infoCadastralObjects
        for cadastral in response_json["infoCadastralObjects"]:
            self.assertIn("id", cadastral)
            self.assertIn("cadastralNumber", cadastral)
            self.assertIn("cadastralType", cadastral)

            # Проверка структуры вложенных объектов в cadastralType
            self.assertIn("id", cadastral["cadastralType"])
            self.assertIn("code", cadastral["cadastralType"])
            self.assertIn("description", cadastral["cadastralType"])
            logger.info("Проверка структуры вложенных объектов в infoCadastralObjects")

        # Проверка структуры вложенных объектов в execUser
        logger.info("Проверка структуры вложенных объектов в execUser")
        self.assertIn("id", response_json["execUser"])
        self.assertIn("firstName", response_json["execUser"])
        self.assertIn("middleName", response_json["execUser"])
        self.assertIn("lastName", response_json["execUser"])
        

        # Проверка структуры вложенных объектов в dataForRequests
        logger.info("Проверка структуры вложенных объектов в dataForRequests")
        self.assertIn("mvdDataList", response_json["dataForRequests"])
        self.assertIn("minselhozDataList", response_json["dataForRequests"])
        self.assertIn("fnsDataList", response_json["dataForRequests"])
        self.assertIn("rosreestrDataList", response_json["dataForRequests"])
        self.assertIn("rosaccrDataList", response_json["dataForRequests"])
        

        # Проверка структуры вложенных объектов в fnsDataList
        for fnsData in response_json["dataForRequests"]["fnsDataList"]:
            self.assertIn("recordNumber", fnsData)
            self.assertIn("kpp", fnsData)
            logger.info("Проверка структуры вложенных объектов в fnsDataList")

        # Проверка структуры вложенных объектов в rosreestrDataList
        for rosreestrData in response_json["dataForRequests"]["rosreestrDataList"]:
            self.assertIn("recordNumber", rosreestrData)
            self.assertIn("cadastralNumber", rosreestrData)
            self.assertIn("objectType", rosreestrData)
            logger.info("Проверка структуры вложенных объектов в rosreestrDataList")

        # Проверка структуры вложенных объектов в rosaccrDataList
        for rosaccrData in response_json["dataForRequests"]["rosaccrDataList"]:
            self.assertIn("recordNumber", rosaccrData)
            self.assertIn("rakrCert", rosaccrData)
            self.assertIn("rakrEntity", rosaccrData)
            logger.info("Проверка структуры вложенных объектов в rosaccrDataList")
