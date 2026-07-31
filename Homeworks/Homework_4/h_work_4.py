string_0 = "Привет"
chislo_zceloe = 42
chislo_s_tochkoy = 3.14
spisok = [1, 2, 3]
print((string_0), "-", type(string_0))
print((chislo_zceloe), "-", type(chislo_zceloe))
print((chislo_s_tochkoy), "-", type(chislo_s_tochkoy))
print((spisok), "-", type(spisok), "\n")

string_1 = "python PROGRAMMING"
print(string_1)
print(string_1.lower())
print(string_1.upper())
print(string_1.capitalize())
print(string_1.title(), "\n")

string_2 = " Hello World "
print(string_2.strip())
print(string_2.lstrip())
print(string_2.rstrip(), "\n")

string_3 = "яблоко,банан,апельсин,груша"
fructs = string_3.split(",")
print(fructs)
string_4 = " | ".join(fructs)
print(string_4, "\n")

string_5 = "Я изучаю Python. Python - это круто!"
rep_string_5 = string_5.replace("Python", "Java")
print(string_5)
print(rep_string_5, "\n")

string_6 = "Python программирование на Python"
print(string_6.find("Python"))
print(string_6.count("Python"))
print(string_6.find("Java"), "\n")

string_7 = "Hello123"
string_7_1 = "12345"
string_7_2 = "Hello"
string_7_3 = "   "
print("Строка",  string_7, "Содержит и буквы и цифры? = ", string_7.isalnum())
print("Строка",  string_7_1, "Содержит только цифры? = ", string_7_1.isdigit())
print("Строка",  string_7_2, "Содержит только буквы? = ", string_7_2.isalpha())
print("Строка",  string_7_3, "Содержит только пробелы? = ", string_7_3.isspace(), "\n")

string_8 = "Python very good"
print(string_8[0:3])
print(string_8[-3:])
print(string_8[::2])
print(string_8[::-1], "\n")

string_9 = "Он сказал: \"Привет\""
string_10 = """Первая строка
Вторая строка"""
print(string_9)
print(string_10)
