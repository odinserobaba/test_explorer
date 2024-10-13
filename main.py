from controllers.e_gais_request import EGAISRequest
from controllers.e_gais_info_request import EGAISInfoRequest
from controllers.e_gais_logs import EGAISLogs
if __name__ == "__main__":
    token_base_url = 'https://lk-test.egais.ru/api-lc-license/tools/token'
    info_base_url = 'https://lk-test.egais.ru/api-lc-license/dashboard/license/request'
    listRegionCodes = 77
    regionCode = 77
    role = 'admin'
    license_id = 225358
    jsessionid = '2D76793EF3BDCC914ECF896C887FB2AA'

    # token_request_instance = EGAISRequest(token_base_url)
    # try:
    #     token = token_request_instance.make_request(listRegionCodes, regionCode, role)
    #     print(f"Token: {token}")

    #     info_request_instance = EGAISInfoRequest(info_base_url)
    #     response = info_request_instance.make_request(license_id, token, jsessionid)
    #     print(response.status_code)
    #     print(response.text)
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    # logs = EGAISLogs
    EGAISLogs.get_logs(path='/media/nuanred/backup/lic_test/lic_test/logs/',services='api-lc-license',context='test-kuber',message='test')
