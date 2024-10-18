from abc import ABC, abstractmethod

class AbstractRequest(ABC):
    @abstractmethod
    def make_request(self, license_id, token, jsessionid):
        pass
