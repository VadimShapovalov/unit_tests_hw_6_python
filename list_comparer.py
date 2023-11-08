

class ListComparer:
    def __init__(self, list_one, list_two):
        self.list_one = list_one
        self.list_two = list_two

    def calculate_average(self, list_of_numbers):
        if not list_of_numbers:
            return None
        return sum(list_of_numbers) / len(list_of_numbers)

    def compare_averages(self):
        avg_list_one = self.calculate_average(self.list_one)
        avg_list_two = self.calculate_average(self.list_two)

        if avg_list_one is None or avg_list_two is None:
            return "Один или оба списка пусты"

        if avg_list_one > avg_list_two:
            return "Первый список имеет большее среднее значение"
        elif avg_list_one < avg_list_two:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"
