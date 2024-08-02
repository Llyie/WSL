import os
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=checkpath)
    return parser.parse_args()

def checkpath(path):
    if os.path.exists(path):
        print("Valid path!")
        return path
    elif os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"This is a directory")
    else:
        raise argparse.ArgumentTypeError(f"Not a valid path")



def main():
    parsed_args = parse_arguments()

if __name__ == "__main__":
    main()
