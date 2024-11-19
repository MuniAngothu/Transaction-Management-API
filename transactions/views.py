from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionListCreateView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        transactions = Transaction.objects.filter(user_id=user_id)
        serializer = TransactionSerializer(transactions, many=True)
        return Response({"transactions": serializer.data})

class TransactionDetailView(APIView):
    def get(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            serializer = TransactionSerializer(transaction, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)  
        



def api_home(request):
    return HttpResponse("""
        <h1>Welcome to the Transaction Management API</h1>
        <p>Use the following endpoints to interact with the API:</p>
        <ul>
            <li><strong>POST /api/transactions/</strong> - Create a new transaction.</li>
            <li><strong>GET /api/transactions/?user_id=[user_id]</strong> - Retrieve all transactions for a user.</li>
            <li><strong>GET /api/transactions/[transaction_id]/</strong> - Retrieve details of a specific transaction.</li>
            <li><strong>PUT /api/transactions/[transaction_id]/</strong> - Update the status of a transaction.</li>
        </ul>
        <p>For example, you can create a transaction by sending:</p>
        <pre>
        {
            "amount": 150.00,
            "transaction_type": "DEPOSIT",
            "user": 1
        }
        </pre>
        """, content_type="text/html")

        
#Other Routes For Fun,I Tried,Before Testing this don't Forget to change urls.py for these 
         
'''
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from django.db.models import Q

class TransactionDeleteView(APIView):
    def delete(self, request, transaction_id):
        try:
            transaction = Transaction.objects.get(id=transaction_id)
            transaction.delete()
            return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Transaction.DoesNotExist:
            return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)



class TransactionListCreateView(APIView):
    def get(self, request):
        user_id = request.query_params.get('user_id')
        status_filter = request.query_params.get('status')

        if not user_id:
            return Response({"error": "user_id is required"}, status=status.HTTP_400_BAD_REQUEST)

       
        transactions = Transaction.objects.filter(Q(user_id=user_id) & Q(status=status_filter)) if status_filter else Transaction.objects.filter(user_id=user_id)

        serializer = TransactionSerializer(transactions, many=True)
        return Response({"transactions": serializer.data}) 
    


class TransactionPaginatedListView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    pagination_class = PageNumberPagination
'''

