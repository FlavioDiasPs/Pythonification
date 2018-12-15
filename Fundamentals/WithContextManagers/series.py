import sys

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [line.strip() for line in f]
        
def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == '__main__':
    main('Fundamentals\Exceptions\exceptionsTryBlock.py')