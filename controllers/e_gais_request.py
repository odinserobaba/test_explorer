import requests
import logging
import paramiko
from abstract_class.abstract_request import AbstractRequest
from utils.utils import append_text_to_file
from settings import res_file,sand_token
# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class EGAISRequest(AbstractRequest):
    def __init__(self, base_url):
        self.base_url = base_url
        self.vm_details = {
            "hostname": "10.0.50.208",
            "username": "Serobaba",
            "password": "nuanred"
        }
        self.jhost_details = {
            "hostname": "10.10.4.32",
            "username": "Serobaba",
            "password": "nuanred"
        }

    def execute_ssh_commands(self, commands, vm_details, jhost_details):
        try:
            logger.info(f"Start EGAISRequest execute_ssh_commands")
            vm = paramiko.SSHClient()
            vm.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            vm.connect(vm_details['hostname'], username=vm_details['username'],
                       password=vm_details['password'])

            vm_transport = vm.get_transport()
            dest_addr = (jhost_details['hostname'], 22)
            local_addr = (vm_details['hostname'], 22)
            vm_channel = vm_transport.open_channel(
                "direct-tcpip", dest_addr, local_addr)

            jhost = paramiko.SSHClient()
            jhost.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            jhost.connect(jhost_details['hostname'], username=jhost_details['username'],
                          password=jhost_details['password'], sock=vm_channel)
            res = []
            logger.info(f"EGAISRequest execute_ssh_commands выполняем команды {commands}")
            for c in commands:
                if c:
                    stdin, stdout, stderr = jhost.exec_command(c + '\n')
                    res.append(stdout.read().decode())
                else:
                    continue
                    # logger.error(f"EGAISRequest execute_ssh_commands нет команд для выполнения {commands}")
                    # raise ValueError(f"Нет команд для выполнения ")
                    # continue
            jhost.close()
            vm.close()
            return res
        except Exception as e:  
            logger.error(f"EGAISRequest execute_ssh_commands произошла ошибка {e}")
            return None

    def get_token_b(self):
        logger.info(f"EGAISRequest get_token_b получаем токен")
        url = "https://license.api-lk.monitor-utm.ru/tools/token?role=developer"
        payload = ""
        headers = {
            'accept': '*/*',
        }
        try:
            response = requests.request(
                "GET", url, headers=headers, data=payload, verify=False)
            logger.info(f"EGAISRequest get_token_b токен {response.text}")
            return response.text
        except Exception as e:
            logger.error(f"EGAISRequest get_token_b произошла ошибка {e}")
        finally:
            return None

    def run_http_requests_on_remote(self, inn='7841051711', license_type_code=9, request_type_code=7, orgBriefName='ООО "ЗХП_АП "', orgFullName='ООО "ЗХП_АП "'):
        # host = "http://lk-test.test-kuber-nd.fsrar.ru/"
        host = "https://license.api-lk.monitor-utm.ru/"  # SANDBOX
        # host = "https://lk-test.egais.ru/api-lc-license/"
        # role = 'role=developer'
        get_token = 'tools/token?listRegionCodes=77&regionCode=77&role=developer'
        post_license = 'dashboard/license/request/'

        file = '/home/nuanred/Desktop/wiki/license_pr/out/1.pdf'
        file_path = '/home/ldapusers/Serobaba/1.pdf'

        # Команда для отправки POST-запроса
        # get_token_cmd = self.get_token_b()
        # Команда для отправки POST-запроса
    
        if sand_token:
            post_request_cmd = f"""
            curl -X POST '{host}{post_license}' -H 'accept: */*' -H "Authorization:{sand_token}" -F 'file=@{file_path}' -F 'inn={inn}' -F 'licenseTypeCode={license_type_code}' -F 'orgBriefName={orgBriefName}' -F 'orgFullName={orgFullName}' -F 'requestTypeCode={request_type_code}'
            """
        logging.info(f"post_cmd -> {post_request_cmd}")
        vm_details = {
            "hostname": "10.0.50.208",
            "username": "Serobaba",
            "password": "nuanred"
        }
        jhost_details = {
            "hostname": "10.10.4.32",
            "username": "Serobaba",
            "password": "nuanred"
        }
        # commands = [get_token_cmd, post_request_cmd]
        commands = [post_request_cmd]
        logger.info(f"EGAISRequest run_http_requests_on_remote команды для выполнения {commands}")
        try:
            result = self.execute_ssh_commands(commands, vm_details, jhost_details)
            logger.info(f"EGAISRequest run_http_requests_on_remote команды для выполнения {result}")
            return result
        except Exception as e:
            logger.error(f"EGAISRequest run_http_requests_on_remote произошла ошибка {e} при выполнении команд {commands}")

# run_http_requests_on_remote(inn='7841051711', license_type_code=2, request_type_code=4,
#                             orgBriefName='ООО "Тестирование"', orgFullName='Тестирование')
