import sys


def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)  # for writing lines to console line by line
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
