from MotorVehicle import MotorVehicle
from MyException import MyException

class Car(MotorVehicle):
    wheel_radius: int

    def __init__(self, name, weight, payload):
        super().__init__(name, weight, payload)
        self.min_radius = 15
        self.max_radius = 17

    def change_wheels(self,_wheel_radius):
        if _wheel_radius not in range(self.min_radius,self.max_radius):
            raise MyException(self,"Wrong wheels!")
        self.wheel_radius = _wheel_radius
        print('Wheels changed!')