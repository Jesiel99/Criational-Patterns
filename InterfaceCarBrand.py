import abc
from abc import ABCMeta


class InterfaceCarBrand(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def models(self):
        raise NotImplementedError

    @abc.abstractmethod
    def info(self):
        raise NotImplementedError


class CarBrand(InterfaceCarBrand, metaclass=ABCMeta):

    def __new__(cls, model):
        subs = InterfaceCarBrand.__subclasses__()
        for sub in subs:
            if cls != sub and model in sub.models:
                return sub()
        else:
            raise ModuleNotFoundError


class Fiat(InterfaceCarBrand):
    models = ['uno', 'siena', 'novo uno']

    def info(self):
        print('Fiat')


class Wolksvagen(InterfaceCarBrand):
    models = ['gol', 'fusca']

    def info(self):
        print('Wolksvagen')


class Ford(InterfaceCarBrand):

    models = ['carro ford', 'kkk']

    def info(self):
        print('Ford')
