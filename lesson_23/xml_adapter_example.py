from xml.etree import ElementTree


class Movie:
    def __init__(self,
                 title,
                 format,
                 year,
                 rating,
                 description,
                 category):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        for genre in collection:
            for decade in genre:
                for movie in decade:
                    movies.append(cls(
                        movie.attrib['title'],
                        movie.find('format').text,
                        movie.find('year').text,
                        movie.find('rating').text,
                        movie.find('description').text,
                        genre.attrib['category']
                    ))
        return movies

    @classmethod
    def from_xml_to_string(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        text = ElementTree.tostring(collection)

        return text

    @classmethod
    def from_string_toxml(cls, text):
        tree = ElementTree.fromstring(text)

        return tree

    @classmethod
    def from_xml_to_json(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = {}
        genre_counter = 0
        for genre in collection:
            movies[f'genre{genre_counter}'] = {}
            decade_counter = 0
            for decade in genre:
                movies[f'genre{genre_counter}'][f'decade{decade_counter}'] = {}
                movie_counter = 0
                for movie in decade:
                    movies[f'genre{genre_counter}'][f'decade{decade_counter}'][f'movie{movie_counter}'] = {}
                    movies[f'genre{genre_counter}'][f'decade{decade_counter}'][f'movie{movie_counter}'][
                        'format'] = movie.find('format').text,
                    movies[f'genre{genre_counter}'][f'decade{decade_counter}'][f'movie{movie_counter}'][
                        'year'] = movie.find('year').text,
                    movies[f'genre{genre_counter}'][f'decade{decade_counter}'][f'movie{movie_counter}'][
                        'rating'] = movie.find('rating').text,
                    movies[f'genre{genre_counter}'][f'decade{decade_counter}'][f'movie{movie_counter}'][
                        'description'] = movie.find('description').text,
                    movie_counter += 1
                decade_counter += 1
            genre_counter += 1
        return movies


movies = Movie.from_xml_to_string("films.xml")
print(movies)
tree = Movie.from_string_toxml(movies)
print(Movie.from_string_toxml(movies))
test_json = Movie.from_xml_to_json("films.xml")
print(test_json)
# for movie in movies:
#    print(movie.title)
