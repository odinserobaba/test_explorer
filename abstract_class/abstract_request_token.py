from abc import ABC, abstractmethod

class AbstractRequestToken(ABC):
    @abstractmethod
    def make_request(self, listRegionCodes, regionCode, role):
        pass
