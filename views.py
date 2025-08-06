from django.http import JsonResponse
from .queries import get_students_over_20

def drc_query_examples(request):
    students = get_students_over_20()
    return JsonResponse(list(students), safe=False)
