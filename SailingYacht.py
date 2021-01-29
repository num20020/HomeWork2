from AbstractVehicle import AbstractVehicle
from MyException import MyException

class SailingYacht(AbstractVehicle):
    sail_area:int

    def set_sail(self, area):
        self.sail_area = area

    def move_me_under(self, load):
        if load > self._payload :
            raise MyException(self,"You are sink!")
        print('Godspeed!')