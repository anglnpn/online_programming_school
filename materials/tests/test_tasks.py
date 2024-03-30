import unittest
from datetime import datetime

from materials.models import Course
from payments.models import Subscribe, Payments
from users.models import User
from materials.tasks import send_moderator_email


class TestSendMailingTask(unittest.TestCase):
    """
    Тест отложенной задачи
    по отправке оповещений.
    """

    def setUp(self):
        self.user = User.objects.create(
            name='Test', surname='Test', email='test@t.com')
        self.course = Course.objects.create(
            author=self.user,
            name_course='Course Name',
            description='Course Description',
            price=1000,
            update_date=datetime.utcnow())

        self.user_2 = User.objects.create(
            name='Test2', surname='Test2', email='test2@t.com')
        self.payments = Payments.objects.create(
            payment_user=self.user_2, payment_date=datetime.now(),
            payment_course=self.course, payment_amount=1000000,
            payment_session_id='123456789012345',
            payment_status='successes')
        self.subscribe = Subscribe.objects.create(
            course_id=self.course.id, user=self.user_2)

    def test_send_moderator_email(self):
        """
        Тест отложенной задачи
        по отправке оповещений.
        """
        result = send_moderator_email(self.course.id)
        right_result = "success"
        self.assertEqual(result, right_result)