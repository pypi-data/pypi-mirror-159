# pytree
Simplified clone of the Linux ```tree``` command.

Supports displaying directory tree structure with colored output, icons, filesizes, filtered views and more. This utility prints as it scans the directories and can be interrupted anytime by pressing CTRL+C.
### Example output
```
$ python -m pytree -is
📂 pytree
├── 🐍 setup.py [303]
├── 📄 LICENSE [1065]
├── 📄 .gitignore [1799]
├── 📄 README.md [818]
├── 📂 tests
│   └── 📄 requirements.txt [187]
└── 📂 pytree
    ├── 🐍 __main__.py [4699]
    ├── 🐍 formatter.py [223]
    ├── 🐍 common.py [1205]
    ├── 🐍 sizes.py [334]
    ├── 🐍 __init__.py [34]
    ├── 🐍 fonts.py [1458]
    └── 🐍 icons.py [541]

2 directories, 12 files
```

## Installation
### From PYPI
```
pip install tree-print
```
### From source
```
git clone https://github.com/maxcurzi/pytree.git
python -m pip install -e pytree
```
Test if it works
```
$ cd pytree
$ python -m pytree
pytree
├── setup.py
├── LICENSE
├── .gitignore
├── README.md
├── tests
│   └── requirements.txt
└── pytree
    ├── __main__.py
    ├── formatter.py
    ├── common.py
    ├── sizes.py
    ├── __init__.py
    ├── fonts.py
    └── icons.py

2 directories, 12 files
```
## Usage
```
python -m pytree [-h] [-d] [-f FILT] [-i] [-c] [-s] [path]

positional arguments:
  path                  Path to print (defaults to current)

options:
  -h, --help            show this help message and exit
  -d, --dir             Only show directories
  -f FILT, --filt FILT  Filter out files and folders (supports shell-style wildcards such as ? and *)
  -i, --icons           Display icons
  -c, --color           Color output
  -s, --size            Show the file size
```

## Compatibility notes
Should work on both Windows and Linux.

Icons are UTF-8 encoded and may not display correctly on your terminal.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)