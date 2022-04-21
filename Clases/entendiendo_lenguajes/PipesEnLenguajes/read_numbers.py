import sys

def main():
    for num in sorted(map(int, next(sys.stdin).split(' ')[:-1])):
        print(num, end=' ')
    print()

if __name__ == '__main__':
    main()

# python3 holamundo.py