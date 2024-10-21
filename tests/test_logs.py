import unittest
import json
from controllers.e_gais_extended_request import EGAISExtendedRequest
from controllers.e_gais_logs import EGAISLogs
from settings import token,requestid,blistRegionCodes,bregionCode,brole,main_path
import logging
import urllib3
import os
import datetime

from utils.utils import save_logs_context
urllib3.disable_warnings()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
path = main_path+str(datetime.datetime.now())
task = '484760'

class TestEGAISLogs(unittest.TestCase):

    def test_logs(self):
        
        api=EGAISLogs.get_logs(path=f'{path}',services='api-lc-license',context='test-kuber',message=task)
        lic=EGAISLogs.get_logs(path=f'{path}',services='lic-integrator',context='test-kuber',message=task)
        # leveler=EGAISLogs.get_logs(path=f'{path}/{task}',services='leveler-cf84',context='test-kuber',message=task)
        self.assertEqual(os.path.exists(api),True)
        self.assertEqual(os.path.exists(lic),True)
        
        # self.assertEqual(os.path.exists(leveler),True)
    # def test_save_context_to_redmine(self):
    #     api=EGAISLogs.get_logs(path=f'{path}/{task}',services='api-lc-license',context='test-kuber',message='test')
    #     save_logs_context(api,'ERROR',f'{path}/{task}',30,'test message')
if __name__ == '__main__':
    unittest.main()
