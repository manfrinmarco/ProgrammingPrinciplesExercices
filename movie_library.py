import json


class MovieLibrary:

    class MovieNotFoundError(Exception):
        """
        Exception raised when a movie is not found in the collection.
        """
        def __init__(self, message="Movie was not found"):
            self.message = message
            super().__init__(self.message)

    def __init__(self, json_file):
        """
        Initialize the MovieLibrary instance.
        :param json_file: Absolute path to the movies.json file.
        """
        self.json_file = json_file
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self.movies = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.json_file}")

    def _save_to_file(self):
        """
        Save the current state of the movies collection to the JSON file.
        """
        try:
            with open(self.json_file, 'w', encoding='utf-8') as file:
                json.dump(self.movies, file, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.json_file}")

    def get_movies(self):
        """
        Retrieve the entire collection of movies.
        :return: List of all movies in the collection.
        """
        return self.movies

    def add_movie(self, title, director, year, genres):
        """
        Add a new movie to the collection.
        :param title: Title of the movie.
        :param director: Director of the movie.
        :param year: Year of the movie.
        :param genres: List of genres for the movie.
        """
        new_movie = {
            'title': title,
            'director': director,
            'year': year,
            'genres': genres
        }
        self.movies.append(new_movie)
        self._save_to_file()
        return new_movie

    def remove_movie(self, title):
        """
        Remove a movie from the collection by title.
        :param title: Title of the movie to be removed.
        :return: Removed movie if successful.
        """
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                self.movies.remove(movie)
                self._save_to_file()
                print(f"Movie '{title}' removed successfully.")
                return movie
        raise self.MovieNotFoundError()

    def update_movie(self, title, director=None, year=None, genres=None):
        """
        Update an existing movie's details.
        :param title: Title of the movie to be updated.
        :param director: New director (optional).
        :param year: New year (optional).
        :param genres: New genres (optional).
        :return: Updated movie dictionary.
        """
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                if director:
                    movie['director'] = director
                if year:
                    movie['year'] = year
                if genres:
                    movie['genres'] = genres
                self._save_to_file()
                print(f"Movie '{title}' updated successfully.")
                return movie
        raise self.MovieNotFoundError()

    def get_movie_titles(self):
        """
        Retrieve a list of all movie titles.
        :return: List of all movie titles.
        """
        return [movie['title'] for movie in self.movies]

    def count_movies(self):
        """
        Count the total number of movies.
        :return: Total number of movies.
        """
        return len(self.movies)

    def get_movie_by_title(self, title):
        """
        Retrieve a movie by its title.
        :param title: Title of the movie.
        :return: Movie dictionary if found.
        """
        for movie in self.movies:
            if movie['title'].lower() == title.lower():
                return movie
        raise self.MovieNotFoundError()

    def get_movies_by_title_substring(self, substring):
        """
        Retrieve movies that contain the substring in their title.
        :param substring: Substring to search for.
        :return: List of matching movies.
        """
        result = [
            movie for movie in self.movies
            if substring in movie['title']
        ]
        return result

    def get_movies_by_year(self, year):
        """
        Retrieve movies by release year.
        :param year: Year to filter by.
        :return: List of movies released in the specified year.
        """
        result = [
            movie for movie in self.movies
            if movie['year'] == year
        ]
        return result

    def count_movies_by_director(self, director):
        """
        Count movies by a specific director.
        :param director: Director name to count movies for.
        :return: Count of movies directed by the given director.
        """
        total = sum(
            1 for movie in self.movies
            if movie['director'].lower() == director.lower()
        )
        return total

    def get_movies_by_genre(self, genre):
        """
        Retrieve movies that belong to a specific genre.
        :param genre: Genre to filter by.
        :return: List of movies matching the genre.
        """
        result = [
            movie for movie in self.movies
            if genre.lower() in [g.lower() for g in movie['genres']]
        ]
        return result

    def get_oldest_movie_title(self):
        """
        Retrieve the title of the oldest movie in the collection.
        :return: Title of the oldest movie.
        """
        oldest = min(self.movies, key=lambda movie: movie['year'])
        return oldest['title']

    def get_average_release_year(self):
        """
        Calculate the average release year of all movies in the collection.
        :return: Average release year as a float.
        """
        total = sum(movie['year'] for movie in self.movies)
        return total / len(self.movies)

    def get_longest_title(self):
        """
        Retrieve the title with the longest length.
        :return: Longest title.
        """
        longest = None
        for movie in self.movies:
            if not longest or len(movie['title']) > len(longest['title']):
                longest = movie
        return longest['title']

    def get_titles_between_years(self, start_year, end_year):
        """
        Retrieve movie titles between the specified years.
        :param start_year: Start of the range.
        :param end_year: End of the range.
        :return: List of titles in the range.
        """
        result = []
        for movie in self.movies:
            if start_year <= movie['year'] <= end_year:
                result.append(movie['title'])
        return result

    def get_most_common_year(self):
        """
        Retrieve the most common release year among movies.
        :return: Year that occurs most often.
        """
        years = {}
        for movie in self.movies:
            years[movie['year']] = years.get(movie['year'], 0) + 1
        most_common_year = max(years, key=years.get)
        return most_common_year
