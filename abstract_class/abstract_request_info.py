from abc import ABC, abstractmethod

class AbstractRequestInfo(ABC):
    @abstractmethod
    def make_request(self, license_id, token, jsessionid):
        pass
