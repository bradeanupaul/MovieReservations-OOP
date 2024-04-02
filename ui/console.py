from domain.exceptions.duplicateError import DuplicateError
from service.clientService import ClientService
from service.movieService import MovieService
from service.assignmentService import AssignmentService


class Console:
    def __init__(self, clientService: ClientService, movieService: MovieService, assignmentService: AssignmentService):
        self.__clientService = clientService
        self.__movieService = movieService
        self.__assignmentService = assignmentService

    def addClient(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            clientName = input("Scrie numele clientului: ")
            clientCnp = input("Scrie cnp-ul clientului: ")
            self.__clientService.addClient(clientId, clientName, clientCnp)
        except DuplicateError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifyClient(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            newClientName = input("Scrie noul nume al clientului: ")
            newClientCnp = input("Scrie noul cnp al clientului: ")
            self.__clientService.mofifyClient(clientId, newClientName, newClientCnp)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteClient(self):
        try:
            clientId = input("Scrie id-ul clientului")
            self.__clientService.deleteClient(clientId)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def show(self, entities):
        for entity in entities:
            print(entity)

    def searchClient(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            print(self.__clientService.searchClient(clientId))
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def searchMovie(self):
        try:
            movieId = input("Scrie id-ul filmului: ")
            print(self.__movieService.searchMovie(movieId))
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def addMovie(self):
        try:
            movieId = input("Scrie id-ul filmului: ")
            movieTitle = input("Scrie titlul filmului: ")
            movieDescription = input("Scrie descrierea filmului: ")
            movieType = input("Scrie genul filmului: ")
            self.__movieService.addMovie(movieId, movieTitle, movieDescription, movieType)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modifyMovie(self):
        try:
            movieId = input("Scrie id-ul filmului: ")
            newMovieTitle = input("Scrie noul titlu: ")
            newMovieDescription = input("Scrie noua descriere: ")
            newMovieType = input("Scrie noul gen: ")
            self.__movieService.modifyMovie(movieId, newMovieTitle, newMovieDescription, newMovieType)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteMovie(self):
        try:
            movieId = input("Scrie id-ul filmului: ")
            self.__movieService.deleteMovie(movieId)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def assignClientToMovie(self):
        try:
            assignmentId = input("Scrie id-ul inscrierii: ")
            clientId = input("Scrie id-ul clientului: ")
            movieId = input("Scrie id-ul filmului: ")
            self.__assignmentService.addAssignment(assignmentId, clientId, movieId)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def deleteAssignment(self):
        try:
            clientId = input("Scrie id-ul clientului: ")
            movieId = input("Scrie id-ul filmului: ")
            self.__assignmentService.deleteAssignment(clientId, movieId)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def mostAssignedMovies(self):
        print(self.__assignmentService.mostAssigned())

    def sortedClients(self):
        try:
            sortOption = input("Alege metoda de sortare. (nume sau filme): ")
            if sortOption == "nume":
                print(self.__assignmentService.sortClientsByName())
            else:
                print(self.__assignmentService.sortClientsByMovies())
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def printMenu(self):
        print("1. Adauga client.")
        print("2. Modifica client.")
        print("3. Sterge client.")
        print("4. Cauta client.")
        print("c. Afiseaza toti clientii.")
        print("5. Adauga film.")
        print("6. Modifica film.")
        print("7. Sterge film.")
        print("8. Cauta film.")
        print("f. Afiseaza toate filmele.")
        print("9. Inscrie client la film.")
        print("10. Sterge inscriere.")
        print("i. Afiseaza toate inscrierile.")
        print("11. Afiseaza clientii cu filmele inchiriate.")
        print("12. Afiseaza cele mai inchiriate filme.")
        print("13. Afiseaza primi 30% clienti cu cele mai multe filme.")
        print("d. Statistica DTO.")
        print("x. Iesire.")

    def menu(self):
        while True:
            self.printMenu()
            option = input("Scrie optiunea: ")
            if option == "1":
                self.addClient()
            elif option == "2":
                self.modifyClient()
            elif option == "3":
                self.deleteClient()
            elif option == "4":
                self.searchClient()
            elif option == "c":
                self.show(self.__clientService.getAllClients())
            elif option == "5":
                self.addMovie()
            elif option == "6":
                self.modifyMovie()
            elif option == "7":
                self.deleteMovie()
            elif option == "8":
                self.searchMovie()
            elif option == "f":
                self.show(self.__movieService.getAllMovies())
            elif option == "9":
                self.assignClientToMovie()
            elif option == "10":
                self.deleteAssignment()
            elif option == "i":
                self.show(self.__assignmentService.getAllAssignments())
            elif option == "11":
                self.sortedClients()
            elif option == "12":
                self.mostAssignedMovies()
            elif option == "13":
                print("In lucru.")
            elif option == "d":
                print("In lucru.")
            elif option == "x":
                break
            else: print("Optiune gresita.")