def calculate_total(price, tax_percent):
    if price < 0:
        return "Ошибка: цена не может быть отрицательной"

    if tax_percent > 20:
        return "Ошибка: налог не может быть больше 20%"

    return price + price * tax_percent / 100

print(calculate_total(100, 20))
print(calculate_total(100, 25))
print(calculate_total(-50, 10), "\n")



def get_level(points):
    if points >= 100:
        return "Эксперт"
    if points >= 50:
        return "Продвинутый"
    if points >= 20:
        return "Начинающий"
    else:
        return "Новичок"

print(get_level(101))
print(get_level(51))
print(get_level(21))
print(get_level(0),  "\n")



def process_status(status):
    match status:
        case "act":
            return "Статус активен"
        case "none_act":
            return "Статус неактивен"
        case "zhdun=)":
            return "Статус в ожидании"
        case "bloc":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"


print(process_status("act"))
print(process_status("none_act"))
print(process_status("zhdun=)"))
print(process_status("bloc"))
print(process_status("unknown"))
