from lib.trace import trace
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: trace <src> <dst> <name>")
        exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    name = sys.argv[3]

    dot = trace(src, dst)
    dot.render(name)
