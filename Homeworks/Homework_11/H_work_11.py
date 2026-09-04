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
    elif points >= 50:
        return "Продвинутый"
    elif points >= 20:
        return "Начинающий"
    else:
        return "Новичок"


print(get_level(101))
print(get_level(51))
print(get_level(21))
print(get_level(0), "\n")


def process_status(status):
    match status:
        case "active":
            return "Статус активен"
        case "inactive":
            return "Статус неактивен"
        case "pending":
            return "Статус в ожидании"
        case "blocked":
            return "Статус заблокирован"
        case _:
            return "Неизвестный статус"


print(process_status("active"))
print(process_status("inactive"))
print(process_status("pending"))
print(process_status("blocked"))
print(process_status("unknown"))
