from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Grade, Subject
from django.db.models import Avg
from django.shortcuts import render



def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def create_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        student = Student.objects.create(name=name)
        return redirect('student_list')  # Перенаправление на страницу списка студентов
    return render(request, 'create_student.html')



def create_subject(request):
    if request.method == 'POST':
        subject_name = request.POST['subject_name']
        subject = Subject.objects.create(subject_name=subject_name)
        return redirect('subject_list')  # Перенаправление на страницу списка предметов
    return render(request, 'create_subject.html')


def edit_student(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']
        student_id = request.POST['student_id']

        student.name = name
        student.course = course
        student.id = student_id
        student.save()
        return redirect('student_list')

    context = {'student': student}
    return render(request, 'edit_student.html', context)

def edit_subject(request, pk):
    subject = Subject.objects.get(pk=pk)

    if request.method == 'POST':
        subject_name = request.POST['subject_name']
        professor = request.POST['professor']

        subject.subject_name = subject_name
        subject.professor = professor
        subject.save()
        return redirect('subject_list')

    context = {'subject': subject}
    return render(request, 'edit_subject.html', context)

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})

def delete_subject(request, pk):
    subject = Subject.objects.get(pk=pk)

    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')

    context = {'subject': subject}
    return render(request, 'delete_subject.html', context)


def report(request):
    # Расчет средних баллов по дисциплинам
    subject_averages = Grade.objects.values('subject__name').annotate(average_grade=Avg('grade'))

    # Получение лучшего и худшего студента
    best_student = Student.objects.annotate(average_grade=Avg('grade__grade')).order_by('-average_grade').first()
    worst_student = Student.objects.annotate(average_grade=Avg('grade__grade')).order_by('average_grade').first()

    context = {
        'subject_averages': subject_averages,
        'best_student': best_student,
        'worst_student': worst_student
    }


    return render(request, 'report.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def subject_list(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subject_list.html', context)




