from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Lesson, Question, Choice, Submission

def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lesson_set.all()
    return render(request, 'course_details_bootstrap.html', {'course': course, 'lessons': lessons})

@login_required
def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        if choice_id:
            choice = get_object_or_404(Choice, pk=choice_id)
            Submission.objects.create(user=request.user, question=question, choice=choice)
            messages.success(request, 'Your answer has been submitted.')
        else:
            messages.error(request, 'Please select an answer.')
    return redirect('OnlineCourse:course_details', course_id=question.lesson.course.id)

@login_required
def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    submissions = Submission.objects.filter(user=request.user, question__lesson__course=course)
    total_questions = Question.objects.filter(lesson__course=course).count()
    correct_answers = submissions.filter(choice__is_correct=True).count()
    score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    return render(request, 'exam_result.html', {
        'course': course,
        'submissions': submissions,
        'score': score,
        'correct_answers': correct_answers,
        'total_questions': total_questions,
    })