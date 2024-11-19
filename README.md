# Transaction Management API - Tutorial

This API allows users to manage financial transactions. Below are the details of available routes, request formats, and example responses.

## Base URL

/api/

## 1\. Create a New Transaction

Endpoint: POST /transactions/

Description: Create a new transaction.

Request Body:

{  
"amount": 100.00,  
"transaction_type": "DEPOSIT",  
"user": 1  
}

Response:

{  
"transaction_id": 1,  
"amount": 100.00,  
"transaction_type": "DEPOSIT",  
"status": "PENDING",  
"user": 1,  
"timestamp": "2024-11-16T10:30:00Z"  
}

## 2\. Retrieve All Transactions for a User

Endpoint: GET /transactions/?user_id=&lt;id&gt;&status=&lt;status&gt;

Description: Retrieve all transactions for a specific user, optionally filtering by status.

Response:

{  
"transactions": \[  
{  
"transaction_id": 1,  
"amount": 100.00,  
"transaction_type": "DEPOSIT",  
"status": "PENDING",  
"timestamp": "2024-11-16T10:30:00Z"  
},  
{  
"transaction_id": 2,  
"amount": 50.00,  
"transaction_type": "WITHDRAWAL",  
"status": "COMPLETED",  
"timestamp": "2024-11-15T15:00:00Z"  
}  
\]  
}

## 3\. Retrieve a Specific Transaction

Endpoint: GET /transactions/&lt;transaction_id&gt;/

Description: Retrieve details of a specific transaction.

Response:

{  
"transaction_id": 1,  
"amount": 100.00,  
"transaction_type": "DEPOSIT",  
"status": "PENDING",  
"timestamp": "2024-11-16T10:30:00Z"  
}

## 4\. Update a Transaction's Status

Endpoint: PUT /transactions/&lt;transaction_id&gt;/

Description: Update the status of a specific transaction.

Request Body:

{  
"status": "COMPLETED"  
}

Response:

{  
"transaction_id": 1,  
"amount": 100.00,  
"transaction_type": "DEPOSIT",  
"status": "COMPLETED",  
"timestamp": "2024-11-16T10:30:00Z"  
}

## 5\. Delete a Transaction

Endpoint: DELETE /transactions/&lt;transaction_id&gt;/delete/

Description: Delete a specific transaction.

Response:

{  
"message": "Transaction deleted successfully"  
}

## 6\. Paginated Transactions

Endpoint: GET /transactions/paginated/

Description: Retrieve paginated transaction data.

Response:

{  
"count": 20,  
"next": "<http://127.0.0.1:8000/api/transactions/paginated/?page=2>",  
"previous": null,  
"results": \[  
{  
"transaction_id": 1,  
"amount": 100.00,  
"transaction_type": "DEPOSIT",  
"status": "PENDING",  
"timestamp": "2024-11-16T10:30:00Z"  
}  
\]  
}