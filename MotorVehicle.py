from dataclasses import dataclass
from MyException import MyException
from AbstractVehicle import AbstractVehicle

@dataclass
class Engine:
    name: str
    weight: int
    power: int
    fuel_type: str

    def __str__(self):
        return f'Engine: {self.name}, weight: {str(self.weight)}, power: {str(self.power)}, fuel: {str(self.fuel_type)}'


FuelType = ('gasoline', 'diesel')


class MotorVehicle(AbstractVehicle):
    motor: Engine

    def __str__(self):
        return super().__str__() + ' ' + self.motor.__str__()

    def powered_by(self, mtr: Engine):
        self.motor = mtr

    def move_me_under(self, load):
        if load > self._payload :
            raise MyException(self,"Cannot move!")
        print('Happy journey to you!')

    def refuel(self, fuel_type_):
        if fuel_type_ not in FuelType:
            raise MyException(self,'Wrong fuel type!')
        if fuel_type_ != self.motor.fuel_type :
            raise MyException(self,'Another fuel type needed!')
        print('Refuel complete!')