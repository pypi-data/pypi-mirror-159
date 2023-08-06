# main.py
#!/usr/bin/env python3
"""Utility to list content of directories in a tree-like format. Analog to the *NIX 'tree' command.
"""

import argparse
import fnmatch
import os
from pathlib import PurePath
from typing import List

from .common import TreePathInfo
from .formatter import Formatter
from .icons import Icons
from .sizes import Sizes
from .fonts import Font

TAB:str = "    "
ELEM_MIDDLE: str = "├── "
ELEM_LAST: str = "└── "
PARENT_MIDDLE: str = "│   "

# Prefix Rules
# 1. Write files first, then folders
# 2. Current level prefix is not added to the stack, just selected as needed
# 3. Push/pop from prefix stack when changing level
# 4. Push PARENT_MIDDLE if the current folder isn't last

def walk_and_print(path: PurePath = PurePath('.'),
                   print_files: bool = True,
                   filter_criteria: str = "",
                   formatters: List[Formatter] = []):
    """Walk the given path, extracts file/directory names and print the corresponging tree structure.
    """
    # DepthCount implements a stack where each element represent the number of remaining folders to
    # display on each nesting level. This is used to display vertical lines, spaces, or 'L'
    # terminators.

    depthCount:list[int] = []
    def get_parents_prefix():
        return "".join(PARENT_MIDDLE if x>0 else TAB for x in depthCount[:-1]) if len(depthCount) > 1 else ""
    dir_count = 0
    files_count = 0
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(path):
        if not print_files:
            files = []

        # Filter dirs and files
        found = [x for x in dirs if fnmatch.fnmatch(x, filter_criteria)]
        for f in found:
            dirs.remove(f)
        found = [x for x in files if fnmatch.fnmatch(x, filter_criteria)]
        for f in found:
            files.remove(f)

        dir_count+= len(dirs)
        files_count+= len(files)

        #  Build the full string formatted string including the tree hierarchy
        dir_name = os.path.basename(root)
        t_dir = TreePathInfo(root=root, name=dir_name, is_file=False)
        for f in formatters:
            f.format(t_dir)

        prefix = get_parents_prefix()
        prefix += ELEM_LAST if len(depthCount)>0 and depthCount[-1]==1 else ELEM_MIDDLE if len(depthCount)>0 else ""
        print(prefix+str(t_dir))

        # Adjust depth stack and reduce level (pop) if this is an empty folder
        if len(depthCount) > 0:
            depthCount[-1] -= 1
        while len(depthCount) > 0 and depthCount[-1] == 0 and (len(dirs)+len(files)==0):
            depthCount.pop()
        # Update stack with the n. of immediate children of this folder
        depthCount.append(len(dirs)+len(files))
        # Print files of current folder
        prefix = get_parents_prefix()
        for idx, file_name in enumerate(files):
            t_file = TreePathInfo(root=root, name=file_name, is_file=True)
            for f in formatters:
                f.format(t_file)
            joint = ELEM_LAST if idx==(len(files)-1) and len(dirs)==0 else ELEM_MIDDLE
            print(prefix+joint+str(t_file))
            # print(t_file)
            depthCount[-1] -= 1

        # Adjust depth stack
        while len(depthCount)>0 and depthCount[-1] == 0:
            depthCount.pop()
    print(f"\n{dir_count} directories, {files_count} files")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to print (defaults to current)", nargs='?', default=os.getcwd())
    parser.add_argument("-d", "--dir", help="Only show directories", action="store_true")
    parser.add_argument("-f", "--filt", type=str,
                        help="Filter out files and folders (supports shell-style wildcards such as ? and *)",
                        default="")
    parser.add_argument("-i", "--icons", help="Display icons", action="store_true")
    parser.add_argument("-c", "--color", help="Color output", action="store_true")
    parser.add_argument("-s", "--size", help="Show the file size", action="store_true")
    args = parser.parse_args()

    # Process arguments
    path = PurePath(args.path)
    filter_criteria:str = args.filt
    print_files:bool = not args.dir
    formatters:List[Formatter] = []
    if args.size:
        formatters.append(Sizes())
    if args.icons:
        formatters.append(Icons())
    if args.color:
        formatters.append(Font())

    # Call the main function
    walk_and_print(
        path = path,
        print_files = print_files,
        filter_criteria = filter_criteria,
        formatters = formatters,
        )

if __name__ == "__main__":
    main()