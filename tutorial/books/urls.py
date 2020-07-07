from django.urls import path
from .views import BookDetailView,BooksListView


urlpatterns = [
      path('list/', BooksListView.as_view(), name="books list"),
      path('details/<int:pk>/', BookDetailView.as_view(), name="Book Detail"),
]
