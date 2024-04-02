from domain.clients import Clients
from domain.movies import Movies
from domain.assignments import Assignments
from repository.genericRepository import Repository


class ClientFileRepository(Repository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__readFile()

    def addEntity(self, client):
        super().addEntity(client)
        self.__writeFile()

    def modifyEntity(self, client):
        super().modfiyEntity(client)
        self.__writeFile()

    def deleteEntity(self, client):
        super().deleteEntity(client)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                clientId = line.split()[0]
                clientName = line.split()[1]
                clientCnp = line.split()[2]
                client = Clients(clientId, clientName, clientCnp)
                self._entities[clientId] = client

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for client in self.getAllEntities():
                f.write(f'{client.getEntityId()} {client.getClientName()} {client.getClientCnp()}\n')

class MovieFileRepository(Repository):
    def __init__(self, __fileName):
        super().__init__()
        self.__fileName = __fileName
        self.__readFile()

    def addEntity(self, movie):
        super().addEntity(movie)
        self.__writeFile()

    def modifyEntity(self, movie):
        super().modfiyEntity(movie)
        self.__writeFile()

    def deleteEntity(self, movie):
        super().deleteEntity(movie)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                movieId = line.split()[0]
                movieTitle = line.split()[1]
                movieDescription = line.split()[2]
                movieType = line.split()[3]
                movie = Movies(movieId, movieTitle, movieDescription, movieType)
                self._entities[movieId] = movie

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for movie in self.getAllEntities():
                f.write(f'{movie.getEntityId()} {movie.getMovieTitle()} {movie.getMovieDescription()} {movie.getMovieType()}\n')

class AssignmentFileRepository(Repository):
    def __init__(self, __fileName):
        super().__init__()
        self.__fileName = __fileName
        self.__readFile()

    def addEntity(self, assignment):
        super().addEntity(assignment)
        self.__writeFile()

    def modifyEntity(self, assignment):
        super().modfiyEntity(assignment)
        self.__writeFile()

    def deleteEntity(self, assignment):
        super().deleteEntity(assignment)
        self.__writeFile()

    def __readFile(self):
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                assignmentId = line.split()[0]
                clientId = line.split()[1]
                movieId = line.split()[2]
                assignment = Assignments(assignmentId, clientId, movieId)
                self._entities[assignmentId] = assignment

    def __writeFile(self):
        with open(self.__fileName, 'w') as f:
            for assignment in self.getAllEntities():
                f.write(f'{assignment.getEntityId()} {assignment.getClientId()} {assignment.getMovieId()}\n')
