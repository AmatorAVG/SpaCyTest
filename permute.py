import argparse
from sympy.utilities.iterables import multiset_permutations


def main():

    parser = argparse.ArgumentParser(description='Program for seeking digits and proper nouns')
    parser.add_argument('amount', nargs='?', help='Amount of numbers', default=5, type=int)
    args = parser.parse_args()

    numbers = [0]*args.amount + [i for i in range(1, args.amount+1)]
    for el in multiset_permutations(numbers):
        print(el)


if __name__ == '__main__':
    main()
