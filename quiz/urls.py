from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'quiz/admin', views.QuizViewSet)
router.register(r'question/admin', views.QuestionViewSet)
router.register(r'question/types', views.QuestionTypesViewSet)
router.register(r'quiz/active', views.ActiveQuizListViewSet)
router.register(r'quiz/pass', views.PassQuizViewSet)
router.register(r'user', views.GetUserPassedQuizzesViewSet)

urlpatterns = router.urls
