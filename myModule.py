import configparser 
parser = configparser.ConfigParser()


def readFile(key, value):
    parser.read('sourceFile.py')
