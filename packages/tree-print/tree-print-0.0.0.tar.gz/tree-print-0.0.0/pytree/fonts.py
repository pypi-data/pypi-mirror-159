from enum import Enum

from .common import TreePathInfo
from .formatter import Formatter


class TColor(Enum):
    BLACK   = "\u001b[30m"
    RED     = "\u001b[31m"
    GREEN   = "\u001b[32m"
    YELLOW  = "\u001b[33m"
    BLUE    = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN    = "\u001b[36m"
    WHITE   = "\u001b[37m"
    RESET   = "\u001b[0m"

class BGColor(Enum):
    BLACK   = "\u001b[40m"
    RED     = "\u001b[41m"
    GREEN   = "\u001b[42m"
    YELLOW  = "\u001b[43m"
    BLUE    = "\u001b[44m"
    MAGENTA = "\u001b[45m"
    CYAN    = "\u001b[46m"
    WHITE   = "\u001b[47m"
    RESET   = "\u001b[0m"

class Decorator(Enum):
    Bold      = "\u001b[1m"
    Underline = "\u001b[4m"
    Reversed  = "\u001b[7m"

class Font(Formatter):
    """Font color and weight formatter"""
    file_text_col: TColor  = TColor.WHITE
    file_back_col: BGColor = BGColor.RESET
    dir_text_col : TColor  = TColor.GREEN
    dir_back_col : BGColor = BGColor.RESET

    def format(self, tpi:TreePathInfo):
        if tpi.is_file:
            tpi.formatted_name = (
                self.file_back_col.value
                + self.file_text_col.value
                + tpi.name
                + TColor.RESET.value)
        else:
            tpi.formatted_name = (
                self.dir_back_col.value
                + Decorator.Bold.value
                + self.dir_text_col.value
                + tpi.name
                + TColor.RESET.value
            )
