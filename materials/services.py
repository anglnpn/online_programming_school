def convert_currencies(price_course):
    """
    Функция получает цену в рублях.
    Возвращает ее в копейках
    """
    price_in_pennies = price_course * 100
    return price_in_pennies
