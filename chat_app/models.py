# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import User

class ChatBot(models.Model):
    # Define a ForeignKey relationship with the built-in User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="GeminiUser", null=True)

    # Define a CharField to store the user's input text with a maximum length of 500 characters
    text_input = models.CharField(max_length=500)

    # Define a TextField to store the output generated by the Gemini chatbot (nullable and blank allowed)
    gemini_output = models.TextField(null=True, blank=True)

    # Define a DateTimeField to store the timestamp when the record is created (auto-generated)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    # Define a human-readable string representation for the ChatBot model
    def __str__(self):
        # Return the user's input text as the string representation
        return self.text_input
