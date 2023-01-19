from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author

class BookViews(generics.GenericAPIView):
    query_set = Book.objects.all()
    serializer_class = BookSerializer
    
    #get books
    def get(self, request):
        serializer = self.serializer_class(self.query_set)
        return Response({'status':'success', 'books':serializer.data})
    

    #create book
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'book':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'failed', 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class BookDetailViews(generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_book(self, book_id):
        try:
            return Book.objects.get(book_id=book_id)
        except:
            return None

    #get book
    def get(self, request, book_id):
        book = self.get_book(book_id)

        if book == None:
            return Response({'status':'failed', 'message':'book does not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(book)
        return Response({'status':'success', 'book':serializer.data})
    
    #update book
    def patch(self, request, book_id):
        book = self.get_book(book_id)

        if book == None:
            return Response({'status':'failed', 'message':'book does not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'book':serializer.data}, status=status.HTTP_418_IM_A_TEAPOT)
        return Response({'status':'failed', 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    #delete book
    def delete(self, request, book_id):
        book = self.get_book(book_id)

        if book == None:
            return Response({'status':'failed', 'message':'book does not found'}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response({'status':'success'}, status=status.HTTP_204_NO_CONTENT)


class AuthorViews(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    #get author
    def get(self, request):
        serializer = self.serializer_class(Author.objects.all(), many=True)
        return Response({'status':'success', 'authors':serializer.data})
    
    #create author
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'author':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status':'failed', 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetailViews(generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_author(self, author_id):
        try:
            return Author.objects.get(author_id=author_id)
        except:
            return None

    #get author
    def get(self, request, author_id):
        author = self.get_author(author_id)

        if author == None:
            return Response({'status':'failed', 'message':'author not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(author)
        return Response({'status':'success', 'author':serializer.data})

    #update author
    def patch(self, request, author_id):
        author = self.get_author(author_id)

        if author == None:
            return Response({'status':'failed', 'message':'author not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'author':serializer.data}, status=status.HTTP_418_IM_A_TEAPOT)
        return Response({'status':'failed', 'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    #delete author
    def delete(self, request, author_id):
        author = self.get_author(author_id)
        print('\n\n',author,'\n\n')

        if author == None:
            return Response({'status':'failed', 'message':'author not found'}, status=status.HTTP_404_NOT_FOUND)
        
        author.delete()
        return Response({'status':'success'}, status=status.HTTP_204_NO_CONTENT)