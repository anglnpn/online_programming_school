import unittest

from payments.services import (
    create_product,
    create_price,
    create_payment_session,
    get_payment_status)


class TestStripeCommand(unittest.TestCase):
    """
    Тестирование функций для
    работы со stripe.
    """

    def test_create_product(self):
        """
        Тестирование создания
        продукта(курса для оплаты) в stripe.
        """
        name = 'test product'
        description = 'test description'
        product_id = create_product(name, description)
        self.assertIsNotNone(product_id, int)

    def test_create_price(self):
        """
        Тестирование создания цены
        продукта(курса для оплаты) в stripe.
        """
        name = 'test product'
        description = 'test description'
        price_id = create_price(name, description)
        self.assertIsNotNone(price_id, int)

    def test_create_payment_session(self):
        """
        Тестирование создания сессии
        оплаты в stripe.
        """
        name = 'test product'
        description = 'test description'
        price_id = create_price(name, description)
        session_id = create_payment_session(
            price_id, 'http://test.com', 'http://test.com')
        self.assertIsNotNone(session_id, dict)

    def test_get_payment_status(self):
        """
        Тестирование получения статуса
        оплаты в stripe.
        """
        name = 'test product'
        description = 'test description'
        price_id = create_price(name, description)
        session_id = create_payment_session(
            price_id, 'http://test.com', 'http://test.com')
        status = get_payment_status(session_id)
        self.assertIsNotNone(status, str)
