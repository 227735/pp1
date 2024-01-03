class Statistics:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def display_numbers(self):
        numbers_str = ''
        for num in self.numbers:
            numbers_str += str(num) + ' '
        return numbers_str.strip()

    def display_statistics(self):
        return f"Minimum: {min(self.numbers)}\nMaximum: {max(self.numbers)}\nMean: {sum(self.numbers) / len(self.numbers)}\nMedian: {sorted(self.numbers)[len(self.numbers)//2]}"

statistics_obj = Statistics()

numbers_to_add = [12, 37, 6, 9, 17]

for number in numbers_to_add:
    statistics_obj.add_number(number)

print("Numbers:", statistics_obj.display_numbers())

print(statistics_obj.display_statistics())