from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
def questions(request):
    questions = Question.objects.order_by('-date_added')
    context = {'questions': questions}
    return render(request, 'html_css/questions.html', context)


@login_required()
def question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.order_by('-date_added')
    context = {'question': question, 'answers': answers}
    return render(request, 'html_css/question.html', context)


@login_required()
def new_question(request):
    if request.method != 'POST':
        form = QuestionForm()
    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.owner = request.user
            new_question.save()
            return redirect('html_css:questions')
    context = {'form': form}
    return render(request, 'html_css/new_question.html', context)


@login_required()
def new_answer(request, question_id):
    question = Question.objects.get(id=question_id)

    if request.method != 'POST':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = question
            new_answer.save()
            return redirect('html_css:question', question_id=question_id)

    context = {'question': question, 'form': form}
    return render(request, 'html_css/new_answer.html', context)