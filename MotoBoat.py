from MotorVehicle import MotorVehicle
from MyException import MyException

class MotoBoat(MotorVehicle):
    def move_me_under(self, load):
        if load > self._payload :
            raise MyException(self,"You are sink with motor!")
        print('Fare you well!')