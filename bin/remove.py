#!/usr/bin/env python

import sys
import argparse

from niklib.trees import remove_node


def get_args() -> argparse.Namespace:
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "strings",
        nargs="*",
        help="The strings from which we remove the target.",
    )

    parser.add_argument(
        "--target",
        required=True,
        help="The thing to remove from the list of arguments.",
    )

    parser.add_argument(
        "--sep",
        default=" ",
        help="The separator.",
    )

    return parser.parse_args()


def main() -> None:
    """
    Remove the thing!
    """
    args = get_args()

    print(args.sep.join(remove_node(args.strings, args.target)))


if __name__ == "__main__":
    main()
