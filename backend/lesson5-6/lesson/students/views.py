from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Student, StudentGroup, Subject

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

class ViewSubjects(View):
    def get(self, request):
        name = request.GET.get('name', '')

        subjects = Subject.objects.all()
        if name:
            subjects = Subject.objects.filter(name=name)
        subjects_data = []
        for subject in subjects:
            subjects_data.append({
                'name':subject.name
            })
        return JsonResponse({'data':subjects_data})
    
    def post(self, request):
        name = request.POST.get('name', '')
        return HttpResponse(name)

class ViewSubject(View):
    def get(self, request):
        try:
            subject = Subject.objects.all()
            subjects_data = {
                'name':subject.name
        }
        except Subject.DoesNotExist:
            subject = None

        subjects_data={}
        return JsonResponse({'data':subjects_data})

class ViewSubjectStudents(View):
    def get(self, request, id):
            students_data = []
            try:
                subject = Subject.objects.get(id=id)
                groups = subject.groups.all()
                for group in groups:
                    students = group.students.all()
                    for student in students:
                        students_data.append({'name':student.name})
            except Subject.DoesNotExist:
                students_data.append({"Subject with such ID does not exist"})
            return JsonResponse({'data':students_data})

