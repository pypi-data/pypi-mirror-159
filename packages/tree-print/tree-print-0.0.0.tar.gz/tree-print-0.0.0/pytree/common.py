from dataclasses import dataclass
from pathlib import PurePath
from typing import Optional

@dataclass
class TreePathInfo:
    """Class to structure the paths"""
    def __init__(self, root:str, name:str, is_file:bool=False) -> None:
        self.root = root
        self._name:str = name
        self.is_file = is_file
        self.icon: str  = ""
        self.size: Optional[str] = None
        self._ext: str = PurePath(name).suffix
        self._formatted_name: str = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name:str):
        self._name = new_name
        self._formatted_name = new_name

    @property
    def formatted_name(self) -> str:
        return self._formatted_name

    @formatted_name.setter
    def formatted_name(self, new_name:str):
        self._formatted_name = new_name

    @property
    def ext(self) -> str:
        return self._ext

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        size = f" [{self.size}]" if self.size  else ""
        return (self.icon + (' ' if self.icon != "" else '')
                + self._formatted_name
                + size)
