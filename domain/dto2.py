from dataclasses import dataclass

@dataclass
class AssignedMoviesNumberDTO:
    name: str
    assignedMovies: int

class AssignedMoviesNumberDTOAssembler:
    @staticmethod
    def createAssignedMoviesNumberDto(client, moviesNumber):
        name = client.getClientName()
        assignedMovies = moviesNumber
        return AssignedMoviesNumberDTO(name, assignedMovies)