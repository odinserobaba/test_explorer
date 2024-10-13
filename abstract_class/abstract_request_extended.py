from abc import ABC, abstractmethod

class AbstractRequestExtended(ABC):
    @abstractmethod
    def make_request(self, license_id, token, jsessionid):
        pass
