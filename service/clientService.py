from domain.clients import Clients
from repository.genericRepository import Repository


class ClientService:
    def __init__(self, clientRepository: Repository, assignmentRepository: Repository):
        self.__clientRepository = clientRepository
        self.__assignmentRepository = assignmentRepository

    def searchClient(self, clientId):
        return self.__clientRepository.getEntityById(clientId)

    def getAllClients(self):
        return self.__clientRepository.getAllEntities()

    def addClient(self, clientId, clientName, clientCnp):
        client = Clients(clientId, clientName, clientCnp)
        self.__clientRepository.addEntity(client)

    def mofifyClient(self, clientId, newClientName, newClientCnp):
        client = Clients(clientId, newClientName, newClientCnp)
        self.__clientRepository.modfiyEntity(client)

    def deleteClient(self, clientId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getClientId() == clientId:
                self.__assignmentRepository.deleteEntity(assignment.getClientId())
        self.__clientRepository.deleteEntity(clientId)