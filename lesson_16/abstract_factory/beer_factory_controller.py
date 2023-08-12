from lesson_16.abstract_factory.factories.stoutFactory import StoutFactory
from lesson_16.abstract_factory.factories.lager_factory import LagerFactory


class AbstractBeerFactory:
    @staticmethod
    def get_factory(beer_type):
        if beer_type == 'lager':
            return LagerFactory()
        elif beer_type == 'stout':
            return StoutFactory()
        else:
            return 'wrong beer type'


lager_factory_1 = AbstractBeerFactory.get_factory('lager')
print(lager_factory_1.get_beer('hardened'))
