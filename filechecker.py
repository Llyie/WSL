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
    else:
        raise argparse.ArgumentTypeError(f"Not a valid path")


parsed_args = parse_arguments()