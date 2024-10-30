from typing import Iterable


def remove_node(namelist: Iterable[str], target: str) -> list[str]:
    """
    Take all occurrences of name out of the list.
    """
    data = list(namelist)

    while True:
        before = list(data)
        try:
            data.remove(target)
        except ValueError:
            return before
