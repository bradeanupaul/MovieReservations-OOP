from domain.entity import Entity


class Movies(Entity):
    def __init__(self, movieId, movieTitle, movieDescription, movieType):
        super().__init__(movieId)
        self.__movieTitle = movieTitle
        self.__movieDescription = movieDescription
        self.__movieType = movieType

    def getMovieTitle(self):
        return self.__movieTitle

    def getMovieDescription(self):
        return self.__movieDescription

    def getMovieType(self):
        return self.__movieType

    def setMovieTitle(self, movieTitle):
        self.__movieTitle = movieTitle

    def setMovieDescription(self, movieDescription):
        self.__movieDescription = movieDescription

    def setMovieType(self, movieType):
        self.__movieType = movieType

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Titlul este: {self.getMovieTitle()}, Descrierea este: {self.getMovieDescription()}, Genul este: {self.__movieType}"
