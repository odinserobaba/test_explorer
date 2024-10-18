from doctest import testfile
import requests
import logging
import json
from abstract_class.abstract_request_extended import AbstractRequestExtended
from utils.utils import append_text_to_file
from settings import res_file
# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class EGAISExtendedRequest(AbstractRequestExtended):
    def __init__(self, base_url):
        self.base_url = base_url
        self.response=""
        self.check=""

    def make_request(self, license_id, token):
        try:
            if token:
                url = self._build_url(license_id)
                headers = {
                    'Authorization': f'Bearer {token}',
                    # 'Cookie': f'JSESSIONID={jsessionid}'
                }
                logger.info(f"Sending request to {url}")
                response = requests.get(url, headers=headers, verify=False)
                response.raise_for_status()  # Проверка на ошибки HTTP
                logger.info(f"Received response with status code {response.status_code}")
                append_text_to_file("save_report/"+res_file,f'''* Получаем extendet по requestid {license_id}''')
                append_text_to_file("save_report/"+res_file,f'''
    {{{{collapse({self.base_url})
        response code - {response.status_code}
        <pre><code class='json'>
        {response.json()}
        </code></pre>
    }}}}                     
                                    ''')
                self.response=response.json()
                return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
        else:
            logger.error(f"Request failed:token {token} is NULL")

    def _build_url(self, license_id):
        return f"{self.base_url}/{license_id}/extended"

    def get_check(self):
        if self.response!="":
            js = self.response
            result = []
            for check in js['checks']:
                result.append([check['checkId'],check["code"],check["checkStatus"]["code"]])
            self.check=result
            logger.info(f"Проверки:")
            for x in result:
                logger.info(f"checkId: {x[0]} code: {x[1]} checkStatus: {x[2]}")
            return result
        else:
            logger.info(f"get_check уже вызывался:")
            return result
        