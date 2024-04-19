def convert_currencies(price_course: int) -> int:
    """
    Функция получает цену в рублях (int).
    Возвращает ее в копейках (int).
    """
    price_in_pennies = price_course * 100
    return price_in_pennies
