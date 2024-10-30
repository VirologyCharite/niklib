import pytest

from niklib.trees import remove_node


class Test_Remove_Node:

    def test_empty(self):
        """
        Removing something from an empty list should give the empty list.
        """
        assert remove_node([], "xxx") == []

    def test_nonexistent(self):
        """
        Trying to remove something from a list that doesn't contain that thing
        should give back the original list.
        """
        data = [3, 4, 5]
        assert remove_node(data, "xxx") == data

    def test_remove_number(self):
        """
        Trying to remove a number from a list that does contain that thing
        should give back the list without that thing.
        """
        assert remove_node([3, 4, 5], 4) == [3, 5]

    def test_remove_string(self):
        """
        Trying to remove a string from a list that does contain that thing
        should give back the list without that thing.
        """
        assert remove_node(["a", "b"], "b") == ["a"]

    def test_remove_something_that_occurs_twice(self):
        """
        Trying to remove something from a list that contains that thing
        twice should give back the list without the copies of that thing.
        """
        assert remove_node([3, 4, 3, 5], 3) == [4, 5]

    def test_remove_something_that_occurs_three_times(self):
        """
        Trying to remove something from a list that contains that thing
        three times should give back the list without the copies of that thing.
        """
        assert remove_node([3, 4, 3, 5, 3], 3) == [4, 5]
