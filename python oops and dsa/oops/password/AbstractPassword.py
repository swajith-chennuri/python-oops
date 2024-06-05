from abc import ABC, abstractmethod
class AbstractPassword(ABC):
    def __init__(self, password, attempts):
        self.password = password
        self.attempts = attempts
    @abstractmethod
    def authenticate(self):
        pass
