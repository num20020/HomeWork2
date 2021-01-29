from MyException import MyException
from Car import Car
from SailingYacht import SailingYacht
from MotoBoat import MotoBoat
from Kickscooter import Kickscooter
from MotorVehicle import Engine

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
    Oceanis45_Maria.set_sail(100)

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
