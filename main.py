# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#import pandas as pd
data = {
    "Назва": [
        "Мистецтво війни",
        "Гаррі Поттер і філософський камінь",
        "1984",
        "Великий Гетсбі",
        "Атлант розправив плечі",
        "Хмарний атлас"
    ],
    "Автор": [
        "Сунь-Цзи",
        "Дж. К. Ролінг",
        "Джордж Орвелл",
        "Ф. Скотт Фіцджеральд",
        "Айн Ренд",
        "Девід Мітчелл"
    ],
    "Рік видання": [2010, 2018, 2012, 2014, 2020, 2016],
    "Ціна": [200, 350, 180, 250, 400, 300]
}

books = pd.DataFrame(data)

print("Усі книги:")
print(books)
print()

average_price = books["Ціна"].mean()
print("Середня ціна книг:", average_price)
print()

recent_books = books[books["Рік видання"] > 2015]
print("Книги, видані після 2015 року:")
print(recent_books)
print()

sorted_books = books.sort_values(by="Ціна", ascending=True)
print("Книги, відсортовані за ціною (зростання):")
print(sorted_books)

