import os
import time
import subprocess
import logging
from abstract_class.abstract_logs import AbstractLogs

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class EGAISLogs(AbstractLogs):
    def __init__(self):
        pass

    @staticmethod
    def get_logs(path, services, context, message):
        try:
            # Получаем текущую дату
            date = time.strftime('%Y-%m-%d', time.localtime())

            # Формируем путь к папке с логами
            path = f'{path}/{date}_{services}_{context}_{message}'

            # Создаем папку, если ее нет
            if not os.path.exists(path):
                os.makedirs(path)
                logger.info(f'Папка "{path}" создана.')
            else:
                logger.info(f'Папка "{path}" уже существует.')

            # Подключаемся к DockerHub и получаем список подов
            sshProcess = subprocess.Popen(['ssh', 'DockerHub'], stdin=subprocess.PIPE,
                                          stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)
            sshProcess.stdin.write(f'kubectl config use-context {context}\n')
            sshProcess.stdin.write('kubectl get pods --all-namespaces\n')
            sshProcess.stdin.close()

            list = []
            for line in sshProcess.stdout:
                if line == "END\n":
                    break
                list.append(line)
                print(line, end="")
            for line in sshProcess.stdout:
                print(line, end="")

            # Получаем список подов и фильтруем его по имени сервиса
            data = tuple(x.split() for x in list[17:])
            find_str = services
            str_list = [[x[0], x[1]] for x in data if find_str in x[1]]
            logger.info(f"EGAISLogs {str_list}")
            print(str_list)
            if str_list!=[]:
                command = f'kubectl logs -n {str_list[0][0]} {str_list[0][1]}'
                logger.info(
                    f'EGAISLogs -> kubectl logs -n {str_list[0][0]} {str_list[0][1]}')
                sshProcess_save_log = subprocess.Popen(
                    ['ssh', 'DockerHub'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True, bufsize=0)
                sshProcess_save_log.stdin.write(command)
                sshProcess_save_log.stdin.close()
                save_text = sshProcess_save_log.stdout.readlines()
                save_text = [x.split('\n') for x in save_text]
                logger.info(
                    f'EGAISLogs -> пишем в файл - {path}/{context}{services}{message}.log')
                with open(f"{path}/{context}{services}{message}.log", "a") as output:
                    for x in save_text:
                        output.write(str(x[0]) + '\n')
                logger.info(
                    f'EGAISLogs -> успешно записан файл в  - {path}/{context}{services}{message}.log')
                return f'{path}/{context}{services}{message}.log'
            else:
                logger.error(f'EGAISLogs -> нет подов - {path} {context} {services} {message} ')
        except Exception as e:
            logger.exception(f'Ошибка при получении логов: {e}')
