from AbstractVehicle import AbstractVehicle
from MyException import MyException

class Kickscooter(AbstractVehicle):

    def move_me_under(self, load):
        if load > self._payload :
            raise MyException(self,"Eat little less!")
        print('Have a good ride!')