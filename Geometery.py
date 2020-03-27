from sys import stdout as ostream
from sys import stdin as istream

def sayHelloWorld():
    ostream.write('Hello World!')

def main():
    sayHelloWorld()

if __name__ == '__main__':
    main()