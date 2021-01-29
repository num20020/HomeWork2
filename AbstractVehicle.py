from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    def __init__(self,name, weight, payload):
        self._name = name
        self._weight = weight
        self._payload = payload

    def __str__(self):
        return f'Name: {self._name}, weight: {str(self._weight)}, maximum load: {str(self._payload)}'

    @abstractmethod
    def move_me_under(self, load):
        pass