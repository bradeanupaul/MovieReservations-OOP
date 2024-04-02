from domain.assignments import Assignments
from domain.exceptions.duplicateError import DuplicateError
from repository.genericRepository import Repository


class AssignmentService:
    def __init__(self, assignmentRepository: Repository, clientRepository: Repository, movieRepository: Repository):
        self.__assignmentRepository = assignmentRepository
        self.__clientRepository = clientRepository
        self.__movieRepository = movieRepository

    def addAssignment(self, assignmentId, clientId, movieId):
        if self.__clientRepository.getEntityById(clientId) is None:
            raise KeyError("Nu exista un client cu acest id.")
        if self.__movieRepository.getEntityById(movieId) is None:
            raise KeyError("Nu exista un film cu acest id.")

        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getClientId() == clientId and assignment.getMovieId() == movieId:
                raise DuplicateError("Clientul are deja acest film.")

        assignment = Assignments(assignmentId, clientId, movieId)
        self.__assignmentRepository.addEntity(assignment)

    def getAllAssignments(self):
        return self.__assignmentRepository.getAllEntities()

    def deleteAssignment(self, clientId, movieId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getClientId() == clientId and assignment.getMovieId() == movieId:
                self.__assignmentRepository.deleteEntity(assignment.getEntityId())

    def assignedMovies(self):
        count = {}
        for element in self.__assignmentRepository.getAllEntities():
            if element.getMovieId() in count:
                count[element.getMovieId()] += 1
            else:
                count[element.getMovieId()] = 1
        return count

    def mostAssigned(self):
        count = self.assignedMovies()
        maximum = 0
        list = []
        for i in count.keys():
            if count[i] > maximum:
                maximum = count[i]
        for i in count.keys():
            if count[i] == maximum:
                list.append(i)
        return list

    def assignmentClientName(self, clientId):
        list = self.__clientRepository.getAllEntities()
        for client in list:
            if client.getEntityId() == clientId:
                return client.getClientName

    def sortedNames(self):
        list = self.__clientRepository.getAllEntities()
        newList = []
        for client in list:
            newList.append(client.getClientName())
        newList.sort()
        return newList

    def sortClientsByName(self):
        list = self.sortedNames()
        count = self.assignedMovies()
        list1 = []
        list2 = []
        for i in count.keys():
            list1.append(i)
        for name in list:
            for element in list1:
                if name == self.assignmentClientName(element):
                    list2.append(self.__clientRepository.getEntityById(element))
        return list2

    #def sortClientsByMovies(self):