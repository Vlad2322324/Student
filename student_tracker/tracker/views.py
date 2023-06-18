from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Grade, Subject
from django.db.models import Avg, Min, Max
from django.shortcuts import render



def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def create_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        student = Student.objects.create(name=name)
        return redirect('student_list')
    return render(request, 'create_student.html')



def create_subject(request):
    if request.method == 'POST':
        subject_name = request.POST['subject_name']
        subject = Subject.objects.create(subject_name=subject_name)
        return redirect('subject_list')
    return render(request, 'create_subject.html')

def create_grade(request):
    if request.method == 'POST':
        grade_value = request.POST['grade']
        date = request.POST['date']
        subject_id = request.POST['subject']
        student_id = request.POST['student']

        grade = Grade.objects.create(
            grade=grade_value,
            date=date,
            subject_id=subject_id,
            student_id=student_id
        )
        return redirect('grade_list')

    subjects = Subject.objects.all()
    students = Student.objects.all()

    context = {'subjects': subjects, 'students': students}
    return render(request, 'create_grade.html', context)

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

def edit_grade(request, pk):
    grade = Grade.objects.get(pk=pk)
    subjects = Subject.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        grade_value = request.POST['grade']
        date = request.POST['date']
        subject_id = request.POST['subject']
        student_id = request.POST['student']

        grade.grade = grade_value
        grade.date = date
        grade.subject_id = subject_id
        grade.student_id = student_id
        grade.save()

        return redirect('grade_list')

    context = {
        'grade': grade,
        'subjects': subjects,
        'students': students
    }
    return render(request, 'edit_grade.html', context)


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

def delete_grade(request, pk):
    grade = get_object_or_404(Grade, pk=pk)

    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')

    context = {'grade': grade}
    return render(request, 'delete_grade.html', context)


def report(request):

    all_grades = Grade.objects.all()


    student_grades = all_grades.values('student').annotate(avg_grade=Avg('grade'))


    best_student = student_grades.order_by('-avg_grade').first()
    worst_student = student_grades.order_by('avg_grade').first()

    # Получение деталей о лучшем студенте
    if best_student:
        best_student_id = best_student['student']
        best_student_name = Grade.objects.filter(student=best_student_id).first().student.name
        best_student_avg_grade = best_student['avg_grade']
    else:
        best_student_name = "N/A"
        best_student_avg_grade = None

    if worst_student:
        worst_student_id = worst_student['student']
        worst_student_name = Grade.objects.filter(student=worst_student_id).first().student.name
        worst_student_avg_grade = worst_student['avg_grade']
    else:
        worst_student_name = "N/A"
        worst_student_avg_grade = None

    context = {
        'best_student_name': best_student_name,
        'best_student_avg_grade': best_student_avg_grade,
        'worst_student_name': worst_student_name,
        'worst_student_avg_grade': worst_student_avg_grade
    }

    return render(request, 'report.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def subject_list(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects}
    return render(request, 'subject_list.html', context)

def grade_list(request):
    grades = Grade.objects.all()
    context = {'grades': grades}
    return render(request, 'grade_list.html', context)

def average_report(request):
    if request.method == 'POST':
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')

        if subject_id == 'all':
            grades = Grade.objects.filter(student_id=student_id)
        else:
            grades = Grade.objects.filter(student_id=student_id, subject_id=subject_id)

        total_grades = len(grades)
        if total_grades > 0:
            sum_grades = sum(grade.grade for grade in grades)
            average_grade = sum_grades / total_grades
        else:
            average_grade = 0

        context = {
            'average_grade': average_grade,
            'students': Student.objects.all(),
            'subjects': Subject.objects.all()
        }
        return render(request, 'average_report.html', context)

    context = {
        'students': Student.objects.all(),
        'subjects': Subject.objects.all()
    }
    return render(request, 'average_report.html', context)





