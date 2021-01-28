from dataclasses import dataclass
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



@dataclass
class Engine:
    name: str
    weight: int
    power: int
    fuel_type: str
    def __str__(self):
        return f'Engine: {self.name}, weight: {str(self.weight)}, power: {str(self.power)}, fuel: {str(self.fuel_type)}'

FuelType = ('gasoline','diesel')

class MotorVehicle(AbstractVehicle):
    motor: Engine

    def __init__(self, name, weight, payload):
        super().__init__(name, weight, payload)


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



class SailingYacht(AbstractVehicle):
    sail_area:int

    def __init__(self, name, weight, payload):
#
        super().__init__(name, weight, payload)

    def set_sail(self, area):
        self.sail_area = area

    def move_me_under(self, load):
        if load > self._payload :
            raise MyException(self,"You are sink!")
        print('Godspeed!')

class MotoBoat(MotorVehicle):
    def move_me_under(self, load):
        if load > self._payload :
            raise MyException(self,"You are sink with motor!")
        print('Fare you well!')


class Kickscooter(AbstractVehicle):

    def move_me_under(self, load):
        if load > self._payload :
            raise MyException(self,"Eat little less!")
        print('Have a good ride!')


class Car(MotorVehicle):
    wheel_radius: int
    def __init__(self, name, weight, payload):
        super().__init__(name,  weight, payload)
        self.min_radius = 15
        self.max_radius = 17

    def change_wheels(self,_wheel_radius):
        if _wheel_radius not in range(self.min_radius,self.max_radius):
            raise MyException(self,"Wrong wheels!")
        self.wheel_radius = _wheel_radius
        print('Wheels changed!')

class MyException(Exception):
    def __init__(self, owner, _message):
        super().__init__()
        self.message = owner._name + ': ' + _message

if __name__ == '__main__':
    print('Hello w')

    GMC_150 = Engine('GMC',300,150,'diesel')
    print(GMC_150)

    MAN_V8 = Engine('MAN V8', 1000, 1400, 'gasoline')
    print(MAN_V8)

    Chevrolet_Captiva = Car('Chevrolet Captiva', 3500, 800)
    Chevrolet_Captiva.powered_by(GMC_150)

    print(Chevrolet_Captiva)

    Oceanis45_Maria = SailingYacht('Maria',10500, 3500)
    Oceanis45_Maria.sail_area = 100

    print(Oceanis45_Maria)

    PrincessS65_Fighter = MotoBoat('Fighter',30500,5000)
    PrincessS65_Fighter.powered_by(MAN_V8)

    print(PrincessS65_Fighter)

    Razor_A6 = Kickscooter('Razor A6', 5, 100)

    print(Razor_A6)

    # calling methods with errors

    try:
        Chevrolet_Captiva.move_me_under(1000)
    except MyException as ex:
        print('Error!',ex.message)

    try:
        Chevrolet_Captiva.change_wheels(19)
    except MyException as ex:
        print('Error!',ex.message)

    try:
        Chevrolet_Captiva.refuel('water')
    except MyException as ex:
        print('Error!',ex.message)


    try:
        Oceanis45_Maria.move_me_under(4000)
    except MyException as ex:
        print('Error!',ex.message)


    try:
        PrincessS65_Fighter.move_me_under(5500)
    except MyException as ex:
        print('Error!',ex.message)

    try:
        PrincessS65_Fighter.refuel('diesel')
    except MyException as ex:
        print('Error!',ex.message)

    try:
        Razor_A6.move_me_under(120)
    except MyException as ex:
        print('Error!',ex.message)


    # calling methods with no errors

    try:
        Chevrolet_Captiva.move_me_under(700)
    except MyException as ex:
        print('Error!',ex.message)

    try:
        Chevrolet_Captiva.change_wheels(15)
    except MyException as ex:
        print('Error!',ex.message)

    try:
        Chevrolet_Captiva.refuel('diesel')
    except MyException as ex:
        print('Error!',ex.message)


    try:
        Oceanis45_Maria.move_me_under(3000)
    except MyException as ex:
        print('Error!',ex.message)


    try:
        PrincessS65_Fighter.move_me_under(4500)
    except MyException as ex:
        print('Error!',ex.message)

    try:
        PrincessS65_Fighter.refuel('gasoline')
    except MyException as ex:
        print('Error!',ex.message)

    try:
        Razor_A6.move_me_under(50)
    except MyException as ex:
        print('Error!',ex.message)

