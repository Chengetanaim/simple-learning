from django import forms

from .models import Questions, Answer


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['text']
        labels = {'text': ''}


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
        labels = {'text': 'Answer:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
