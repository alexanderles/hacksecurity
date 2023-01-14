#!/usr/bin/env python3

import argparse
from crawler import Crawler


def main(args):
    crawler = Crawler()
    crawler.run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is a web crawler!")
    parser.add_argument(
        "--input", "-i", help="This is an EXAMPLE input.", required=False)
    args = parser.parse_args()
    main(args)
