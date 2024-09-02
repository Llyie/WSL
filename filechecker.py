import os
import argparse
import datetime

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=checkpath)
    return parser.parse_args()

def checkpath(path):
    if os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"This is a directory")    
    elif os.path.exists(path):        
        file_size = os.path.getsize(path)
        file_creation_time = datetime.datetime.fromtimestamp(os.path.getctime(path))
        file_modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(path))
        
        print(f"File Size = {file_size} bytes")
        print(f"File Creation Time = {file_creation_time}")
        print(f"File Modification Time = {file_modification_time}")
        
        with open(path) as reader:
            char = reader.read()
            print(char)
            print(len(char))
            return path
    else:
        raise argparse.ArgumentTypeError(f"Not a valid path")



def main():
    parsed_args = parse_arguments()

if __name__ == "__main__":
    main()
    