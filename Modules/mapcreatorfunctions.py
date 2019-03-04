import sys

def end(grid):
    str = ""
    for i in grid:
        str += ",".join(i) + "\n"
    print(str)
    sys.exit()
