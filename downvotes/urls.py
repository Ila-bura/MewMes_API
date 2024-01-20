from django.urls import path
from downvotes import views

urlpatterns = [
    path('downvotes/', views.DownVoteList.as_view()),
]