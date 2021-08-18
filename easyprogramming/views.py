from django.shortcuts import render, redirect
from .models import Questions
from .forms import QuestionsForm, AnswerForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required()
def index(request):
    return render(request, 'easyprogramming/index.html')


@login_required()
def questions(request):
    questions = Questions.objects.order_by('-date_added')
    context = {'questions': questions}
    return render(request, 'easyprogramming/questions.html', context)


@login_required()
def question(request, question_id):
    question = Questions.objects.get(id=question_id)
    answers = question.answer_set.order_by('-date_added')
    context = {'question': question, 'answers': answers}
    return render(request, 'easyprogramming/question.html', context)


@login_required()
def new_question(request):
    if request.method != 'POST':
        form = QuestionsForm()
    else:
        form = QuestionsForm(data=request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.owner = request.user
            new_question.save()
            return redirect('easyprogramming:questions')
    context = {'form': form}
    return render(request, 'easyprogramming/new_question.html', context)


@login_required()
def new_answer(request, question_id):
    question = Questions.objects.get(id=question_id)

    if request.method != 'POST':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = question
            new_answer.save()
            return redirect('easyprogramming:question', question_id=question_id)

    context = {'question': question, 'form': form}
    return render(request, 'easyprogramming/new_answer.html', context)
