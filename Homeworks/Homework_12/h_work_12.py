class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f"'{self.title}' автор {self.author}, {self.pages} стр."

    def is_long(self):
        return self.pages > 300


book_1 = Book("Гарри Поттер", "Джоан Роулинг", 400)
book_2 = Book("Преступление и наказание", "Фёдор Достоевский", 672)
book_3 = Book("Мастер и Маргарита", "Михаил Булгаков", 480)

print(book_1.get_info())
print(book_1.is_long())

print(book_2.get_info())
print(book_2.is_long())

print(book_3.get_info())
print(book_3.is_long(), "\n")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Недостаточно средств")
            return False

    def get_balance(self):
        return self.balance


account = BankAccount("Сергей", 1000)
account.deposit(300)
print(account.owner, "ваш счет пополнен. Ваш баланс после пополнения:", account.get_balance())
print("Снятие 250:", account.withdraw(250))
print("Ваш баланс:", account.get_balance())
print("Снятие 2000:", account.withdraw(2000))
print("Ваш баланс:", account.get_balance())
