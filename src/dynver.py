from importlib.metadata import version
from logging import INFO
from logging import basicConfig
from logging import info


def dynver() -> str:
    return version('prova-python-dynver')


def main() -> None:
    basicConfig(level=INFO, format='%(message)s')
    info('dynver: %s', dynver())
