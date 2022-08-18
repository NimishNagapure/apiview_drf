from django.urls import path
from .views import ArticleView,ArticleDetailView

app_name = 'articles'

urlpatterns  =[
    path('articles/',ArticleView.as_view()),
    path('articles/<int:pk>',ArticleDetailView.as_view())
]