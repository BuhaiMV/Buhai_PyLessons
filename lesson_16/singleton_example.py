from lesson_16.mona_lisa_singleton import singleton


@singleton
class MonaLisa:
    def __init__(self, age, author, size):
        self.age = age
        self.author = author
        self.size = size
        self.smile = True


mona_lisa_1 = MonaLisa(12, 'Da Vinci', 'large')
mona_lisa_2 = MonaLisa(200, 'unknown poor boy', 'large')
print(mona_lisa_1.author)
print(mona_lisa_2.author)
mona_lisa_1.age = 201
mona_lisa_2.age = 300
del mona_lisa_1
del mona_lisa_2
mona_lisa_3 = MonaLisa(350, 'printer', 'small')
print(mona_lisa_3.age)
