from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = '__all__'


class QuizUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Quiz
        fields = ('name', 'end_time', 'description', )


class QuizRetrieveSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = models.Quiz
        depth = 2
        fields = '__all__'

    def get_questions(self, obj):
        questions = models.Question.objects.filter(quiz=obj)
        return QuestionSerializer(instance=questions, many=True).data


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Question
        fields = '__all__'


class QuestionTypesSerializer(serializers.Serializer):
    question_types_ids = serializers.SerializerMethodField()
    question_types_names = serializers.SerializerMethodField()

    def get_question_types_ids(self, obj):
        return obj[0]

    def get_question_types_names(self, obj):
        return obj[1]


class AnswerSerializer(serializers.Serializer):
    question_text = serializers.CharField()
    answer_text = serializers.CharField()


class PassQuizSerializer(serializers.Serializer):
    quiz_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    answers = serializers.ListField(child=AnswerSerializer())
    anonymous = serializers.BooleanField()


class GetUserPassedQuizzesRequestSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()


class GetUserPassedQuizzesResponseSerializer(serializers.Serializer):
    quiz_name = serializers.CharField()
    answers = serializers.ListField(child=AnswerSerializer())
