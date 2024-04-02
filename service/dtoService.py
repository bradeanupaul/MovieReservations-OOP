from domain.dto1 import AssignedMoviesNamesDTOAssembler
from domain.dto2 import AssignedMoviesNumberDTOAssembler


class DtoService:
    def __init__(self, clientService, movieService, assignmentService):
        self.__clientService = clientService
        self.__movieService = movieService
        self.__assignmentService = assignmentService

    def __createClientNameDtos(self):
        clientDtos = []
        count = self.assignedClients()
        for client in self.__clientService.getAllClients():
            if client.getEntityId() in count:
                dto = AssignedMoviesNamesDTOAssembler.createAssignedMoviesNamesDto(client, count[client.getEntityId()])
                clientDtos.append(dto)
        return clientDtos

    def __createClientMoviesDtos(self):
        clientDtos = []
        count = self.assignedClients()
        for client in self.__clientService.getAllClients():
            if client.getEntityId() in count:
                dto = AssignedMoviesNumberDTOAssembler.createAssignedMoviesNumberDto(client, self.getMoviesNumber(client))
                clientDtos.append(dto)
        return clientDtos

    def assignedClients(self):
        count = {}
        for element in self.__assignmentService.getAllAssignments():
            if element.getEntityId() in count:
                count[element.getClientId()] += 1
            else:
                count[element.getClientId()] = 1
        return count

    def getMoviesNumber(self, client):
        number = 0
        for assignment in self.__assignmentService.getAllAssignments():
            if client.getEntityId() == assignment.getClientId():
                number += 1
        return number

    def firstByName(self):
        count = self.assignedClients()
        j = int((100 * len(count)) / 100)
        clientDtos = self.__createClientNameDtos()
        clientDtos = sorted(clientDtos, key=lambda x: x.name, reverse=False)
        return clientDtos[:j]

    def firstByMovies(self):
        count = self.assignedClients()
        j = int((100 * len(count)) /100)
        clientDtos = self.__createClientMoviesDtos()
        clientDtos = sorted(clientDtos, key=lambda x: x.assignedMovies, reverse=True)
        return clientDtos[:j]