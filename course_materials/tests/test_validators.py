from rest_framework.test import APITestCase

from course_materials.validators import MaterialLinkValidator
from rest_framework.exceptions import ValidationError


class MaterialsValidatorTest(APITestCase):
    """
    Тестирование валидатора ссылок на видео.
    """

    def setUp(self):
        self.link = "http://youtube.com/watch?v=123"
        self.link2 = "http://rutube/watch?v=456"

    def test_valid_link(self):
        """
        Проверяет, что валидатор не вызывает
        исключение для корректной ссылки
        на youtube.com через API.

        """
        validator = MaterialLinkValidator(field='video_link')
        valid_data = {'video_link': 'http://youtube.com/watch?v=123'}
        result = validator(valid_data)
        self.assertEqual(result, None)

    def test_invalid_non_youtube_link(self):
        """
        Проверяет, что валидатор вызывает исключение
        для неправильной ссылки, не на youtube.com через API.
        """
        validator = MaterialLinkValidator(field='video_link')
        invalid_data = {'video_link': 'http://rutube.com/watch?v=456'}
        with self.assertRaises(ValidationError) as context:
            validator(invalid_data)

        expected_error_message = "Разрешены ссылки только на youtube.com"
        self.assertEqual(str(context.exception.detail[0]),
                         expected_error_message)
