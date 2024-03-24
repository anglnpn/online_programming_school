from rest_framework import serializers

from materials.models import Course, Lesson, Module
from materials.services import convert_currencies
from materials.validators import MaterialLinkCustomValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [MaterialLinkCustomValidator(field='link')]


class ModuleSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'sequence_number',
                  'name_module', 'description', 'image',
                  'lessons_count', 'lessons']

    def get_lessons_count(self, instance):
        return instance.lesson_set.count()


class CourseSerializer(serializers.ModelSerializer):
    modules_count = serializers.SerializerMethodField()
    modules = ModuleSerializer(source='module_set', many=True, read_only=True)
    price_course = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'name_course', 'image',
                  'description', 'author',
                  'module_count', 'modules', 'price',
                  'price_course', 'update_date']

    def get_modules_count(self, instance):
        return instance.module_set.count()

    def get_price_course(self, instance):
        return convert_currencies(instance.price)


class CourseListSerializer(serializers.ModelSerializer):
    modules_count = serializers.SerializerMethodField()
    modules = ModuleSerializer(source='module_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name_course', 'description', 'module_count']

    def get_modules_count(self, instance):
        return instance.module_set.count()
