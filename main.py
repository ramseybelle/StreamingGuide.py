from typing import Any


class Movie:
    # defining member variables with their types
    def __init__(self, title: str, genre: str, director: str, year: int):
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year

    # getter functions for all the member variables of the class movie
    def get_title(self):
        return self.title

    def get_genre(self):
        return self.genre

    def get_director(self):
        return self.director

    def get_year(self):
        return self.year


class StreamingService:
    # initializing empty dictionary

    def __init__(self, name):
        self.name = name
        self.catalog = dict()  # initializing empty dictionary

    def add_movie(self, mov: Movie):
        title = mov.get_title()  # taking title out from the Movie object passed
        self.catalog[
            title] = mov  # adding new movie values to the dictionary with key as title and Movie object as value

    def delete_movie(self, delmovie):
        if delmovie not in self.catalog.keys():  # if provided title is not present in the catalog dictionary then
            # returning false
            return False
        else:
            del self.catalog[delmovie]  # "del" command is used to delete the value

    def isPresent(self,
                  movName):  # it is a simple function to check if movie is there in catalog(dictionary) or not ,
        # we will further require this function
        if movName in self.catalog.keys():
            return True

    def get_name(self):  # to get the name of the Streaming service
        return self.name

    def get_catalog(self):  # to get the dictionary in which we stored all the movies
        return self.catalog


class StreamingGuide:
    listOfallServices: list[Any]

    def __init__(self):
        self.listOfallServices = []  # initializing empty dictionary for storing all the streaming service objects

    def add_streaming_service(self, streaming_service):
        self.listOfallServices.append(streaming_service)  # simply adds the streaming service

    def delete_streaming_service(self, name):  # delete the service

        for i in self.listOfallServices:  # this will iterate through all the objects stored in list
            if (
                    i.get_name() == name):  # if provided streaming service object is in the list we will  remove it,
                # we are assessing the names by "." operator and getter function
                self.listOfallServices.remove(i)

            break  # as soon we delete the object we will come out from the loop

    def where_to_watch(self, movieTitle):
        lst = []  # taking the empty list
        for service in self.listOfallServices:  # again going throught all the streaming service objects stored in
            # listOf allServices
            catalog = service.get_catalog()  # for each streaming service object we are getting their catalog
            # dictionary where movies are stored
            if movieTitle in catalog.keys():  # if movie title is there in the dictionary keys
                movieobj = catalog[movieTitle]  # we store that movie object in the variable called "movie obj"
                lst.append(str(movieobj.title) + "(" + str(
                    movieobj.year) + ")")  # form that movie obj variable we extract the title and year then convert
                # it into string type for concatenation

                break  # as soon we find the movie we append tne name and year to the first position ad come out from
                # the loop

        # this loop goes through all the streaming services to find the presence of movie in specific streaming
        # service object
        for service in self.listOfallServices:

            if (service.isPresent(
                    movieTitle)):  # here we use isPresent function for checking presence of movie in a streaming
                # service ,
                lst.append(service.name)  # if we find the movie in the catalog we add the name

        if len(lst) == 0:  # if list is empty mean movie isn't available in any Streaming service it will return none

            return None
        return lst  # here we return the final output list


# these are all the initializations of objects and addition of data

movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)  # initialization of all movie objects
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflix')  # new object of  StreamingService
stream_serv_1.add_movie(movie_2)  # adding new movie into StreamingService dictionary

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')  # deleting movie from StreamingService dictionary
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()  # creating object of StreamingGuide
stream_guide.add_streaming_service(stream_serv_1)  # adding new Streaming service object into Streaming guide list

stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')  # deleting =Streaming service object from Streaming guide list
search_results = stream_guide.where_to_watch('Little Women')  # searching for the querry
print(search_results)  # printing the results                         #printing the results
