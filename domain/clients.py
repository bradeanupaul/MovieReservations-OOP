from domain.entity import Entity


class Clients(Entity):
    def __init__(self, entityId, entityName, entityCnp):
        super().__init__(entityId)
        self.__entityName = entityName
        self.__entityCnp = entityCnp

    def getClientName(self):
        return self.__entityName

    def getClientCnp(self):
        return self.__entityCnp

    def setClientName(self, entityName):
        self.__entityName = entityName

    def setClientCnp(self, entityCnp):
        self.__entityCnp = entityCnp

    def __str__(self):
        return f"Id-ul este: {self.getEntityId()}, Numele este: {self.__entityName}, Cnp-ul este: {self.__entityCnp}"