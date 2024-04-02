from dataclasses import dataclass

@dataclass
class AssignedMoviesNamesDTO:
    name: str
    assignedMovies: int

class AssignedMoviesNamesDTOAssembler:
    @staticmethod
    def createAssignedMoviesNamesDto(client, moviesNumber):
        name = client.getClientName()
        assignedMovies = moviesNumber
        return AssignedMoviesNamesDTO(name, assignedMovies)