from random import *
from datetime import *


def bDateChange(date):
    changed_date = []
    for element in date('.'):
        changed_date.append(element)
    return ('-'.join(changed_date))


class Passport:

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.gender = gen.upper()
        self.sity = city
        self.birth_date = birth_date

        self.authority = randint(1111, 9999)
        self.__number = randint(100000000, 999999999)
        self.create_date = datetime.today().strftime("%d-%m-%Y")

    def __str__(self):
        return f'Passport: {self.name} {self.surname}'

    def _print(self):
        print(f"Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gender}\n\
            \tCity: {self.sity}\n\
            \tBirth date: {self.birth_date.replace('.', '-')}\n\
            \tAuthority: {self.authority}\n\
            \tNumber : {self.__number}\n\
            \tDate: {self.create_date}")

    # def bDateChange(self):
    #     changed_date = []
    #     for element in self.birth_date.split('.'):
    #         changed_date.append(element)
    #     return ('-'.join(changed_date))


class ForeignPassport(Passport):

    def __init__(self, name, surname, patronymic, gen: str, city, birth_date):
        super().__init__(name, surname, patronymic, gen, city, birth_date)

        self.__number = randint(100000000, 999999999)
        self.visa = []

    def new_visa(self, country, end_time):
        self.visa.append({country: end_time})

    def _print(self):
        print(f"Passport info:\n\
            \tName: {self.name}\n\
            \tSurname: {self.surname}\n\
            \tPatronymic: {self.patronymic}\n\
            \tGender: {self.gender}\n\
            \tCity: {self.sity}\n\
            \tBirth date: {self.birth_date.replace('.', '-')}\n\
            \tNumber : {self.__number}")
        print('Visa info:')
        for item in self.visa:
            print('\t', list(item.keys())[0], ':', list(
                item.values())[0].replace('.', '-'))

    def not_expired(self):
        for item in self.visa:
            for element in item:
                if item[element].replace('.', '-').split('-')[2] >= datetime.today().strftime("%d-%m-%Y").split('-')[2]:
                    if item[element].replace('.', '-').split('-')[1] >= datetime.today().strftime("%d-%m-%Y").split('-')[1]:
                        print(item[element].replace('.', '-').split('-'),
                              datetime.today().strftime("%d-%m-%Y").split('-'))


Bob = Passport('Bob', 'Bobick', 'Bobovich', 'm', 'London', '25.06.2016')

# Bob._print()

Bill = ForeignPassport('Bill', 'Bobick', 'Bobovich',
                       'm', 'London', '25.06.2016')
Bill.new_visa('Poland', '01.09.2021')
Bill.new_visa('GB', '01.05.2021')
Bill.new_visa('USA', '01.10.2021')
# Bill._print()
Bill.not_expired()

#  Робота з датою (25-12-2000)
#  Метод вивведення дати народження у текстовому форматі (25-12-2000)

# ForeignPassport
# Методи:
#   Вивести всі відвідані країни
#   Відобразити інформацію про незакінчені візи
