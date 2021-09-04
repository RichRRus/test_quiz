import datetime

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from pytz import UTC
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from . import models, serializers


class QuizViewSet(viewsets.ModelViewSet):
    queryset = models.Quiz.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = serializers.QuizSerializer

    def get_serializer_class(self):
        method_serializer = {
            'create': serializers.QuizSerializer,
            'retrieve': serializers.QuizRetrieveSerializer,
            'update': serializers.QuizUpdateSerializer,
            'partial_update': serializers.QuizUpdateSerializer,
            'destroy': serializers.QuizSerializer,
            'list': serializers.QuizSerializer,
        }

        return method_serializer[self.action]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class QuestionTypesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionTypesSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        response_data = self.serializer_class(instance=models.Question.QUESTION_TYPES, many=True)

        return JsonResponse(response_data.data, status=200, safe=False)


class ActiveQuizListViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = models.Quiz.objects.filter(
        start_time__lte=datetime.datetime.now(tz=UTC),
        end_time__gt=datetime.datetime.now(tz=UTC)
    )
    permission_classes = [IsAuthenticated, ]

    def get_serializer_class(self):
        method_serializer = {
            'retrieve': serializers.QuizRetrieveSerializer,
            'list': serializers.QuizSerializer,
        }

        return method_serializer[self.action]


class PassQuizViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = models.Quiz.objects.all()
    serializer_class = serializers.PassQuizSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        if validated_data.get('anonymous'):
            user = None
        else:
            user = get_user_model().objects.filter(id=validated_data.get('user_id')).first()
            if not user:
                return JsonResponse({'error': 'User with `user_id` not found.'}, status=404)

        quiz = models.Quiz.objects.filter(id=validated_data.get('quiz_id')).first()
        if not quiz:
            return JsonResponse({'error': 'Quiz with `quiz_id` not found.'}, status=404)

        passed_quiz = models.PassedQuiz(
            user=user,
            quiz=quiz,
            quiz_name=quiz.name
        )

        for answer in validated_data.get('answers'):
            passed_quiz.set_answer(
                question_text=answer.get('question_text'),
                answer_text=answer.get('answer_text')
            )
        passed_quiz.save()

        return JsonResponse(data={}, status=201)


class GetUserPassedQuizzesViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.GetUserPassedQuizzesResponseSerializer

    def retrieve(self, request, *args, **kwargs):
        user = self.get_object()

        passed_quizzes = models.PassedQuiz.objects.filter(user=user)
        data = []
        for passed_quiz in passed_quizzes:
            data.append({
                'quiz_name': passed_quiz.quiz_name,
                'answers': passed_quiz.get_answers()
            })

        return JsonResponse(data, status=200, safe=False)
