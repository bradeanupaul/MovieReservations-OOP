from domain.entity import Entity


class Assignments(Entity):
    def __init__(self, assignmentId, clientId, movieId):
        super().__init__(assignmentId)
        self.__clientId = clientId
        self.__movieId = movieId

    def getClientId(self):
        return self.__clientId

    def getMovieId(self):
        return self.__movieId

    def setClientId(self, clientId):
        self.__clientId = clientId

    def setMovieId(self, movieId):
        self.__movieId = movieId

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Clientul este: {self.__clientId}, Filmul este: {self.__movieId}"