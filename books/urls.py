import views
from django.urls import path

urlpatterns = [
    #author urls
    path('/author', views.AuthorViews.as_veiw()),
    path('/author/<int:author_id>', views.AuthorDetailViews.as_view()),

    #book urls
    path('/book', views.BookViews.as_veiw()),
    path('/book/<int:book_id>', views.BookDetailViews.as_view())
]

