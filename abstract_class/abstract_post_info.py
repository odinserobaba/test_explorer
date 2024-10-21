from abc import ABC, abstractmethod

class AbstractRequestPostInfo(ABC):
    @abstractmethod
    def make_request(self, license_id, token, jsessionid):
        pass
