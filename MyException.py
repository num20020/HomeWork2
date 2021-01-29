class MyException(Exception):
    def __init__(self, owner, _message):
        super().__init__()
        self.message = owner._name + ': ' + _message