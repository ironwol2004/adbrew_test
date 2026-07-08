from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from rest.repository.todo import TodoRepository
import rest.controller.requests.todo as todo_requests
import rest.controller.responses.todo as todo_responses

class TodoListView(APIView):
    def __init__(self):
        try:
            # Initialize the todo repository
            self.todo_repository = TodoRepository()
            # Log the initialization
            logging.info("Todo list view initialized successfully")
        except Exception as e:
            # Log the error for debugging purposes
            logging.error(f"Error initializing todo list view: {e}")
            raise e

    def get(self, request):
        try:
            # Get all todos
            todos = self.todo_repository.get_all_todos()
            # Convert the todos to a response
            response = todo_responses.to_todo_response(todos)
            # Return the response
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            # Log the error for debugging purposes
            logging.error(f"Error getting todos: {e}")
            # Generic error response to avoid leaking internal details
            return Response({"OOPs! Something went wrong": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            # Validate the request
            if not todo_requests.validate_todo_request(request.data):
                # Invalid request response
                return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)
            # Convert the request to a todo model
            todo = todo_requests.to_todo_model(request.data)
            # Create the todo
            if not self.todo_repository.create_todo(todo):
                return Response({"error": "Failed to save todo item in database"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # Successful creation response
            return Response({"message": "Todo created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            # Log the error for debugging purposes
            logging.error(f"Error creating todo: {e}")
            # Generic error response to avoid leaking internal details
            return Response({"OOPs! Something went wrong": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

