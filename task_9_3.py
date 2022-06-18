class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }
class Position(Worker):
    def get_fill_name(self):
        return f'{self.surname.capitalize()} {self.name.capitalize()} {self.position.lower()}'
    def total_income(self):
        total = self._income["wage"] + self._income["bonus"]
        return f'{total} руб.'


worker_1 = Position('Иван', 'Николаев', 'менеджер', 50000, 30000)
print(worker_1.get_fill_name())
print(worker_1.total_income())
