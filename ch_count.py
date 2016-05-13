import sys
import argparse

def count_chars(stream, char):
    """
    Loop through each char in each line of stdin
    and count the user specified chars
    """
    for row in stream:
            count = 0
            for ch in row:
                    if ch == char:
                            count += 1
            sys.stdout.write(count + '\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--char", action="store", dest="char",
                        help="The character that will be counted on each line of input")
    args = vars(parser.parse_args())

    count_chars(sys.stdin, args['char'])

if __name__ == '__main__':
    main()

