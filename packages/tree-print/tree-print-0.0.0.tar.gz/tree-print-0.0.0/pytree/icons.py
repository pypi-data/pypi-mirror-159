from .common import TreePathInfo
from .formatter import Formatter

_EXT_TO_ICON = {
    ".py": '🐍',
    ".pyc": '🐍',
    ".cfg": '🛠',
    ".rs" : '🦀',
    ".js" : '☕',
    ".lock": '🔒',
}

_FILE_ICON = '📄'
_FOLDER_ICON = '📂'


class Icons(Formatter):
    """Icon formatter, sets the icon field of a TreePathInfo depending on its extension."""
    def format(self, tpi:TreePathInfo):
        if tpi.is_file:
            tpi.icon = _EXT_TO_ICON.get(tpi.ext, _FILE_ICON)
        else:
            tpi.icon = _FOLDER_ICON
