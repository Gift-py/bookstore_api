from books import views
from django.urls import path

urlpatterns = [
    #author urls
    path('author/', views.AuthorViews.as_view()),
    path('author/<int:author_id>/', views.AuthorDetailViews.as_view()),

    #book urls
    path('book/', views.BookViews.as_view()),
    path('book/<int:book_id>/', views.BookDetailViews.as_view())
]

