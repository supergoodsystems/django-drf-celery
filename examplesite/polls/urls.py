from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = "polls"
urlpatterns = [
    path("questions/", views.QuestionList.as_view(), name="question-list"),
    path("questions/<int:pk>/", views.QuestionDetail.as_view(), name="question-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
