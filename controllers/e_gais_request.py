import requests
import logging
from abstract_class.abstract_request_token import AbstractRequestToken
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

class EGAISRequest(AbstractRequestToken):
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, listRegionCodes, regionCode, role):
        try:
            url = self._build_url(listRegionCodes, regionCode, role)
            headers = {
                'accept': '*/*'
            }
            logger.info(f"Sending request to {url}")
            response = requests.get(url, headers=headers, verify=False)
            response.raise_for_status()  # Проверка на ошибки HTTP
            logger.info(f"Received response with status code {response.status_code}")
            token = self._extract_token(response.text)
            logger.info(f"Extracted token: {token}")
            
            
            # Пишем report
            append_text_to_file("save_report/"+res_file,f'''
{{{{collapse({self.base_url})
    response code - {response.status_code}
    <pre><code class='json'>
    {token}
    </code></pre>
}}}}                        
                                ''')
            return token
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def _build_url(self, listRegionCodes, regionCode, role):
        return f"{self.base_url}?listRegionCodes={listRegionCodes}&regionCode={regionCode}&role={role}"

    def _extract_token(self, response_text):
        # Предполагается, что токен находится в ответе в формате "Bearer <token>"
        if "Bearer" in response_text:
            token = response_text.split("Bearer ")[1].strip()
            return token
        else:
            logger.error("Token not found in response")
            raise ValueError("Token not found in response")
