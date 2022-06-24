from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from students.models import Student

# old method
def my_view(request):
    if request.method == 'GET':
        return JsonResponse({"result":"Result"})


# new(better) method
class MyView(View):
    def get(self, request):
        students = Student.objects.all()
        students_data = []
        for student in students:
            students_data.append({
                'name':student.name
            })
        return JsonResponse({'data':students_data})
    
    def post(self, request):
        return JsonResponse({"result":"Result_for_post"})
