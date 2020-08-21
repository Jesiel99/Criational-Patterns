import abc
from abc import ABC, ABCMeta


class InterfaceEmploye(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def id(self):
        raise NotImplementedError

    @abc.abstractmethod
    def info(self):
        raise NotImplementedError


class Employe(InterfaceEmploye, metaclass=ABCMeta):

    def __new__(cls, id: str):
        subs = InterfaceEmploye.__subclasses__()
        for sub in subs:
            if cls != sub and sub.id == id:
                return sub()
        else:
            raise ModuleNotFoundError


class Worker(InterfaceEmploye):

    id = '1'

    def info(self):
        print('Worker')


class Doctor(InterfaceEmploye):

    id = '2'

    def info(self):
        print('Doctor')


class Cleaner(InterfaceEmploye):

    id = '3'

    def info(self):
        print('Cleaner')
