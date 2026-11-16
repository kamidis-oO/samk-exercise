#!/usr/bin/python3
"""Entry point for the samk-exercise demo."""

from functions import add, greet


def main():
    print(greet("SAMK"))
    print("2 + 3 =", add(2, 3))


if __name__ == "__main__":
    main()
