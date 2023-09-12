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
        tree
        collection = tree.getroot()
        text = collection.text

        return text


movies = Movie.from_xml_to_string("films.xml")
print(movies)
#for movie in movies:
#    print(movie.title)
