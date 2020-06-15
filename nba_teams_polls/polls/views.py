from django.shortcuts import render

from .models import Question, Choice

# Get questions and display them
def index(request):
    return render(request, 'polls/index.html')  # index.html is a Template we will make... and we ALSO haven't created a URL for that Template yet.
    

