import json

from django.conf import settings
from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=255, verbose_name='Quiz name')
    start_time = models.DateTimeField(verbose_name='Quiz start time')
    end_time = models.DateTimeField(verbose_name='Quiz end time')
    description = models.TextField(null=True, blank=True, verbose_name='Quiz description')

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return f'{self.id}. {self.name}'


class PassedQuiz(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.DO_NOTHING,
                             verbose_name='User ID')
    quiz = models.ForeignKey('quiz.Quiz', on_delete=models.DO_NOTHING, verbose_name='Quiz ID')
    quiz_name = models.CharField(max_length=255, verbose_name='Quiz name')
    _answers = models.TextField(default='[]', verbose_name='Answers')

    class Meta:
        verbose_name = "Passed quiz"
        verbose_name_plural = "Passed quizzes"

    def __str__(self):
        return f'{self.user}\n {self.quiz}'

    def set_answer(self, question_text, answer_text):
        answers = json.loads(self._answers)
        answers.append({'question': question_text, 'answer': answer_text})
        self._answers = json.dumps(answers)

    def get_answers(self):
        return json.loads(self._answers)


class Question(models.Model):
    QUESTION_TYPES = (
        (1, 'Text answer'),
        (2, 'Single choice'),
        (3, 'Multiple choices'),
    )

    question_text = models.TextField(verbose_name='Question text')
    type = models.CharField(max_length=100, choices=QUESTION_TYPES)
    quiz = models.ForeignKey('quiz.Quiz', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Quiz ID')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return f'{self.id}. {self.question_text}'
