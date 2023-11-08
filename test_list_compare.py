import pytest


from list_comparer import *
# from list_comparer import ListComparer


class TestListComparer:

    def test_average_comparison_greater(self):
        list_one = [1, 2, 3, 4, 5]
        list_two = [1, 2, 3]
        comparer = ListComparer(list_one, list_two)
        assert comparer.compare_averages() == "Первый список имеет большее среднее значение"

    def test_average_comparison_lesser(self):
        list_one = [1, 2, 3]
        list_two = [4, 5, 6]
        comparer = ListComparer(list_one, list_two)
        assert comparer.compare_averages() == "Второй список имеет большее среднее значение"

    def test_average_comparison_equal(self):
        list_one = [1, 2, 3]
        list_two = [1, 2, 3]
        comparer = ListComparer(list_one, list_two)
        assert comparer.compare_averages() == "Средние значения равны"

    def test_empty_list_one(self):
        list_one = []
        list_two = [1, 2, 3]
        comparer = ListComparer(list_one, list_two)
        assert comparer.compare_averages() == "Один или оба списка пусты"

    def test_empty_list_two(self):
        list_one = [1, 2, 3]
        list_two = []
        comparer = ListComparer(list_one, list_two)
        assert comparer.compare_averages() == "Один или оба списка пусты"

    def test_both_lists_empty(self):
        list_one = []
        list_two = []
        comparer = ListComparer(list_one, list_two)
        assert comparer.compare_averages() == "Один или оба списка пусты"

