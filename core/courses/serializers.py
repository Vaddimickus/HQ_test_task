from rest_framework import serializers


class Api1:
    def __init__(self, student, product, lesson_name, time, viewed):
        self.student = student
        self.product = product
        self.lesson_name = lesson_name
        self.time = time
        self.viewed = viewed


class Api3:
    def __init__(self, kol_vo_prosmotr_lesson, sum_time, number_of_students, percentage_product_purchase):
        self.kol_vo_prosmotr_lesson = kol_vo_prosmotr_lesson
        self.sum_time = sum_time
        self.number_of_students = number_of_students
        self.percentage_product_purchase = percentage_product_purchase


class Api1Serializer(serializers.Serializer):
    student = serializers.CharField()
    product = serializers.CharField()
    lesson_name = serializers.CharField()
    time = serializers.IntegerField()
    viewed = serializers.BooleanField()


class Api3Serializer(serializers.Serializer):
    kol_vo_prosmotr_lesson = serializers.IntegerField()
    sum_time = serializers.IntegerField()
    number_of_students = serializers.IntegerField()
    percentage_product_purchase = serializers.FloatField()

