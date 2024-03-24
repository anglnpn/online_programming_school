import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def create_product(name, description):
    """
    Создание продукта(курса для оплаты) в stripe
    """
    try:
        product = stripe.Product.create(
            name=name,
            description=description,
            type='good',
        )
        return product.id
    except stripe.error.StripeError as e:
        return {'error': str(e)}


def create_price(product_id, amount):
    """
    Создание цены продукта
    """
    currency = 'rub'
    try:
        price = stripe.Price.create(
            unit_amount=amount,
            currency=currency,
            product=product_id,
        )
        return price.id
    except stripe.error.StripeError as e:
        return {'error': str(e)}


def create_payment_session(price_id, success_url, cancel_url):
    """
   Создание сессии оплаты в stripe
    """
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': price_id,
                'quantity': 1,
            }],
            mode='payment',
            success_url=success_url,
            cancel_url=cancel_url,
        )
        return {'session_id': session.id, 'payment_url': session.url}
    except stripe.error.StripeError as e:
        return {'error': str(e)}


def get_payment_status(session_id):
    """
   Получение статуса оплаты в stripe
    """
    try:
        status = stripe.checkout.Session.retrieve(
            id=session_id
        )
        return status.status
    except stripe.error.StripeError as e:
        return {'error': str(e)}