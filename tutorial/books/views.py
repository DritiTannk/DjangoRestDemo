from django.http import Http404
from rest_framework.views import APIView  # This is subclass of Django's view class and provided by rest framework.
from rest_framework.response import Response
from rest_framework import status

# App Imports
from .models import BookDetails
from .serializers import BookDetailsSerializer


# Create your views here.

class BooksListView(APIView):
    """
    This View method will create and list all the book records.
    """

    def get(self, request):
        books_obj = BookDetails.objects.all()  # Getting records from database.
        serializer = BookDetailsSerializer(books_obj, many=True)  # Serializing each record.
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        record = request.data  # Getting user data.
        serializer = BookDetailsSerializer(data=record)  # Serializing the user content.

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):

    def get_object(self, pk):
        """
        This function will search for particular requested record from database.
        """
        try:
            return BookDetails.objects.get(pk=pk)
        except BookDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        It will only display the request record contents.
        """
        record = self.get_object(pk)
        serializer = BookDetailsSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request, pk=None):
        """
        This function will update the request data data.
        """
        record = self.get_object(pk)
        serializer = BookDetailsSerializer(record,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None):
        """
        This will delete the record from the database.
        """
        record = self.get_object(pk)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


