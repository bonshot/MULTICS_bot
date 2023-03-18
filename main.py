"""
This is the main file for the project. It contains the main function and the
main loop.
"""

from os import getenv
from dotend import load_dotenv
from multics import MulticsBot
load_dotenv()

def main() -> int:
    """The main function of the project."""

    MulticsBot().run(getenv('TOKEN'))
    return 0

if __name__ == '__main__':
    main()