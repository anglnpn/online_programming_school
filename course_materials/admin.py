from django.contrib import admin


from course_materials.models import Course, Module, Lesson

admin.site.register(Course)

admin.site.register(Module)

admin.site.register(Lesson)

