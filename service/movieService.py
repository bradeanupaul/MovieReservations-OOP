from domain.movies import Movies
from repository.genericRepository import Repository


class MovieService:
    def __init__(self, movieRepository: Repository, assignmentRepository: Repository):
        self.__assignmentRepository = assignmentRepository
        self.__movieRepository = movieRepository

    def searchMovie(self, movieId):
        return self.__movieRepository.getEntityById(movieId)

    def getAllMovies(self):
        return self.__movieRepository.getAllEntities()

    def addMovie(self, movieId, movieTitle, movieDescription, movieType):
        movie = Movies(movieId, movieTitle, movieDescription, movieType)
        self.__movieRepository.addEntity(movie)

    def modifyMovie(self, movieId, newMovieTitle, newMovieDescription, newMovieType):
        movie = Movies(movieId, newMovieTitle, newMovieDescription, newMovieType)
        self.__movieRepository.modfiyEntity(movie)

    def deleteMovie(self, movieId):
        assignments = self.__assignmentRepository.getAllEntities()
        for assignment in assignments:
            if assignment.getMovieId() == movieId:
                self.__assignmentRepository.deleteEntity(assignment.getMovieId())
        self.__movieRepository.deleteEntity(movieId)
