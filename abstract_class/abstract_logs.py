from abc import ABC, abstractmethod

class AbstractLogs(ABC):
    # @abstractmethod
    @staticmethod
    def get_logs(self, path, services, context,message):
        pass
