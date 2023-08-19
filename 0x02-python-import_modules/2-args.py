#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("0 arguments.")
    elif argc == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    elif argc > 2:
        for arg in range(len(sys.argv)):
            if arg == 0:
                print("{} arguments:".format(argc - 1))
            print("{}: {}".format(arg, sys.argv[arg]))
