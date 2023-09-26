from django.db import models


class Product(models.Model):
    name = models.CharField("Название", max_length=250)
    owner = models.CharField("Владелец", max_length=250)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField("Имя", max_length=250)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField("Название", max_length=250)
    duration = models.IntegerField("Продолжительность")
    link = models.CharField("Ссылка", max_length=250)

    def __str__(self):
        return self.name


class ProductStudentAccess(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.name + "->" + self.product.name


class LessonProductAccess(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + "->" + self.lesson.name


class LessonStudentLink(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    viewing_time = models.IntegerField("Время просмотра")
    viewed = models.BooleanField("Просмотрено или нет")

    def __str__(self):
        self._bol = ""
        if self.viewed:
            self._bol = "Просмотрено"
        else:
            self._bol = "Не просмотрено"
        return self.student.name + "->" + self.lesson.name + "->" + str(self.viewing_time) + "->" + self._bol


