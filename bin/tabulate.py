from lib.tabulate import tabulate
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: tabulate <src> <dst> <name>")
        exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    name = sys.argv[3]

    html = tabulate(src, dst)
    with open(name, "w") as f:
        f.write(html)
