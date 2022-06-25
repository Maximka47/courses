from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Student

# old method
def my_view(request):
    if request.method == 'GET':
        return JsonResponse({"result":"Result"})


# new(better) method
class MyView(View):
    def get(self, request, id):
        print(id)
        name = request.GET.get('name', '')
        print(name)

        students = Student.objects.all()
        if name:
            students = students.objects.filter(name=name)
        students_data = []
        for student in students:
            students_data.append({
                'name':student.name
            })
        return JsonResponse({'data':students_data})
    
    def post(self, request):
        name = request.POST.get('name', '')
        return HttpResponse(name)


class MyView(View):
    def get(self, request, pk):

        try:
            student = Student.objects.get(pk=pk)
            students_data = {
                'name':student.name
        }
        except Student.DoesNotExist:
            student = None
        students_data={}
        return JsonResponse({'data':students_data})