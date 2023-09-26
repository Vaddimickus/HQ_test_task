from .models import Product, Student, ProductStudentAccess, LessonStudentLink, LessonProductAccess
from .serializers import Api1Serializer, Api3Serializer, Api1, Api3
from django.http import JsonResponse


def index_api1(request):
    return JsonResponse(api1(request.GET["student_id"]))


def index_api2(request):
    return JsonResponse(api2(request.GET["student_id"], request.GET["product_id"]))


def index_api3(request):
    return JsonResponse(api3())


def api1(student_id):
    product_student_access = ProductStudentAccess.objects.all()
    lesson_student_links = LessonStudentLink.objects.all()
    lesson_product_access = LessonProductAccess.objects.all()

    result = []
    psa = product_student_access.filter(student=student_id)
    if psa:
        for j in psa:
            lpl = lesson_product_access.filter(product=j.product)
            for l in lpl:
                les = lesson_student_links.filter(student=student_id, lesson=l.lesson)
                for i in les:
                    result.append([
                        student_id,
                        j.product,
                        i.lesson,
                        i.viewing_time,
                        i.viewed
                    ])

    mas_res = dict()
    for i in range(len(result)):
        a1 = Api1(
            result[i][0],
            result[i][1],
            result[i][2],
            result[i][3],
            result[i][4],
        )
        serializer = Api1Serializer(a1)
        mas_res[i] = serializer.data
    return mas_res


def api2(student_id, product_id):
    product_student_access = ProductStudentAccess.objects.all()
    lesson_student_links = LessonStudentLink.objects.all()
    lesson_product_access = LessonProductAccess.objects.all()

    result = []
    psa = product_student_access.filter(student=student_id)
    if psa:
        for j in psa:
            if j.product.id == int(product_id):
                lpl = lesson_product_access.filter(product=j.product)
                for l in lpl:
                    les = lesson_student_links.filter(student=student_id, lesson=l.lesson)
                    for i in les:
                        result.append([
                            student_id,
                            j.product,
                            i.lesson,
                            i.viewing_time,
                            i.viewed
                        ])

    mas_res = dict()
    for i in range(len(result)):
        a1 = Api1(
            result[i][0],
            result[i][1],
            result[i][2],
            result[i][3],
            result[i][4],
        )
        serializer = Api1Serializer(a1)
        mas_res[i] = serializer.data
    return mas_res


def api3():
    products = Product.objects.all()
    students = Student.objects.all()
    product_student_access = ProductStudentAccess.objects.all()
    lesson_student_links = LessonStudentLink.objects.all()
    lesson_product_access = LessonProductAccess.objects.all()

    result = []
    for product in products:
        psa = product_student_access.filter(product=product)
        number_of_students = len(psa)
        percentage_product_purchase = 100 * number_of_students / len(students)
        sum_time = 0
        kol_vo_prosmotr_lesson = 0
        lpa = lesson_product_access.filter(product=product)
        for i in lpa:
            lsl = lesson_student_links.filter(lesson=i.lesson)
            for j in lsl:
                sum_time += j.viewing_time
                if j.viewed:
                    kol_vo_prosmotr_lesson += 1

        result.append([
            kol_vo_prosmotr_lesson,
            sum_time,
            number_of_students,
            percentage_product_purchase
        ])

    mas_res = dict()
    for i in range(len(result)):
        a1 = Api3(
            result[i][0],
            result[i][1],
            result[i][2],
            result[i][3],
        )
        serializer = Api3Serializer(a1)
        mas_res[i] = serializer.data
    return mas_res


