from abc import ABC, abstractmethod

from .common import TreePathInfo


class Formatter(ABC):
    @abstractmethod
    def format(self, tpi:TreePathInfo):
        """Format the input string and return the resulting value"""
