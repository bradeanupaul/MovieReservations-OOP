class DuplicateError(Exception):
    def __init__(self, message):
        self.__message = message

    def __String__(self):
        return f'{self.__message}'
