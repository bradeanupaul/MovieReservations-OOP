from repository.fileRepository import ClientFileRepository, MovieFileRepository, AssignmentFileRepository
from service.assignmentService import AssignmentService
from service.movieService import MovieService
from service.clientService import ClientService
from ui.console import Console

def main():
    clientFileRepository = ClientFileRepository("clients.txt")
    movieFileRepository = MovieFileRepository("movies.txt")
    assignmentFileRepository = AssignmentFileRepository("assignments.txt")

    clientService = ClientService(clientFileRepository, assignmentFileRepository)
    movieService = MovieService(movieFileRepository, assignmentFileRepository)
    assignmentService = AssignmentService(assignmentFileRepository, clientFileRepository, movieFileRepository)

    console = Console(clientService, movieService, assignmentService)

    console.menu()

main()