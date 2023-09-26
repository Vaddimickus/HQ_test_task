from django.contrib import admin
from .models import Product, Student, Lesson, ProductStudentAccess, LessonStudentLink, LessonProductAccess


admin.site.register(Product)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(ProductStudentAccess)
admin.site.register(LessonStudentLink)
admin.site.register(LessonProductAccess)
