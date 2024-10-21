from doctest import testfile
import requests
import json
import logging
from abstract_class.abstract_post_info import AbstractRequestPostInfo
from utils.utils import append_text_to_file, compact_json
from settings import res_file
# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class EGAISPostInfo(AbstractRequestPostInfo):
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, license_id, token):
        try:
            url = self._build_url(license_id)
            headers = {
                'Authorization': f'Bearer {token}',
                'Accept': '*/*'
            }
            logger.info(f"Sending request to {url}")
            data = '''{"requestId":225492,"ogrn":null,"inn":"7841051711","kpp":"770102001","orgActivityName":"АО","orgNameBrief":"АО «ЦентрИнформ» ","orgNameFull":"КРЕСТЬЯНСКОЕ (ФЕРМЕРСКОЕ) ХОЗЯЙСТВО  ВАЮ ","address":"298405 Республика Крым 91 БАХЧИСАРАЙСКИЙ 1 1 БАХЧИСАРАЙ Г БАХЧИСАРАЙ УЛ ЛЕНИНА Д.106","region":{"code":"77","name":"МОСКВА Г","timeZone":3,"active":true,"fiasUuid":"0c5b2444-70a0-4932-980c-b4dc0d3f02b5"},"email":"info@r77.center-inform.ru","comment":null,"rakrEntities":[],"rakrCerts":[],"phone":"+79261234567","ops":[{"kpp":"784133001"}],"final":true,"infoCadastralObjects":[{"cadastralNumber":"77:77:1111111:7777","cadastralType":{"id":1,"code":"002001001000","description":"Земельный участок"}}],"cadastralObjectsIsEmpty":false,"notExFnsOp":false,"execUser":{"id":125,"firstName":"Подрядчик","lastName":"АО 'ЦЕНТРИНФОРМ'"},"mvdData":[],"minselhozData":[],"fromEpgu":false,"dataForRequests":{"mvdDataList":null,"minselhozDataList":null,"fnsDataList":null,"rosreestrDataList":null,"rosaccrDataList":[]},"ogrnFilledFromEgrul":false,"innFilledFromEgrul":false,"kppFilledFromEgrul":false,"orgNameBriefFilledFromEgrul":false,"orgNameFullFilledFromEgrul":false,"addressFilledFromEgrul":false,"egrulData":false}'''
            data=data.replace('225492',license_id)
            json_data = json.dumps(data)
            logger.info(f"Отправляем json  {compact_json(json_data)}")
            response = requests.post(
                url, headers=headers, verify=False, json=json_data,)
            response.raise_for_status()  # Проверка на ошибки HTTP
            logger.info(f"Received response with status code {
                        response.status_code}")
            append_text_to_file("save_report/"+res_file,
                                f'''* Получаем info по requestid {license_id}''')
            append_text_to_file("save_report/"+res_file, f'''
{{{{collapse(POST {self.base_url})
    response code - {response.status_code}
    <pre><code class='json'>
    {response.json()}
    </code></pre>
}}}}
                                ''')

            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def _build_url(self, license_id):
        return f"{self.base_url}/{license_id}/info"
