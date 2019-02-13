import sys

def end(grid):
    str = ""
    for i in grid:
        str += ",".join(i)
    print(str)
    sys.exit()
