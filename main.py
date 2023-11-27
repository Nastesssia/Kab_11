import datetime

#11.1 средний уровень
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __del__(self):
        print("Объект удален")

    @classmethod
    def today(cls):
        today_date = datetime.datetime.now()
        return cls(today_date.day, today_date.month, today_date.year)

    def increase_year(self):
        self.year += 1

    def decrease_date(self):
        self.day -= 2
        if self.day <= 0:
            self.month -= 1
            if self.month == 0:
                self.year -= 1
                self.month = 12
            days_in_month = self.days_in_month(self.month)
            self.day = days_in_month + self.day

    def days_in_month(self, month):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2:
            if self.is_leap_year():
                return 29
        return days[month - 1]

    def is_leap_year(self):
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)

    def object_info(self):
        return f"{self.day}.{self.month}.{self.year}"

today_obj = Date.today()  # Получение сегодняшней даты

# Увеличение года на 1
today_obj.increase_year()

# Уменьшение даты на 2 дня
today_obj.decrease_date()

# Получение информации об объекте
info = today_obj.object_info()
print(f"Сегодняшняя дата: {datetime.datetime.now()}")
print(f"Дата увеличенная на год и уменьшенная на 2 дня: {info}")

#11.2 средний уровень
class Employee(Date):
    def __init__(self, fio, hire_day, hire_month, hire_year):
        super().__init__(hire_day, hire_month, hire_year)
        self.fio = fio
        self.hire_date = Date(hire_day, hire_month, hire_year)

    @classmethod
    def create_employee(cls):
        fio = input("Введите ФИО сотрудника: ")
        hire_day = int(input("Введите день поступления на работу: "))
        hire_month = int(input("Введите месяц поступления на работу: "))
        hire_year = int(input("Введите год поступления на работу: "))
        return cls(fio, hire_day, hire_month, hire_year)

    def years_of_service(self):
        today_date = datetime.datetime.now()
        service_years = today_date.year - self.hire_date.year
        if today_date.month < self.hire_date.month or (today_date.month == self.hire_date.month and today_date.day < self.hire_date.day):
            service_years -= 1
        return f"Количество лет работы на предприятии: {service_years}"

    def object_info(self):
        return f"ФИО: {self.fio}\nДата поступления: {self.hire_date.object_info()}"

employee_obj = Employee.create_employee()
print(employee_obj.years_of_service())  # Вывод количества лет работы
print(employee_obj.object_info())  # Вывод информации о сотруднике


