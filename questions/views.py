
import csv
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView ,ListCreateAPIView
# Create your views here.
from .models import QuestionsData
from .serializers import QuestionsDataSerializer
from .forms import UploadForm
from django.http import HttpResponse
import io 
import random
from collections import Counter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse

class QuestionsDataDetailView(RetrieveUpdateDestroyAPIView):
    """
      A view for listing and creating QuestionsData objects.


    Args:
    
        ListCreateAPIView (class): Django Rest Framework's ListCreateAPIView class
            used for handling both list (GET) and create (POST) operations.

    """
    queryset = QuestionsData.objects.all()
    serializer_class = QuestionsDataSerializer

class QuestionsDataListView(ListCreateAPIView):
    """
     A view for listing and creating QuestionsData objects.

    Args:
        ListCreateAPIView (class): Django Rest Framework's ListCreateAPIView class
            used for handling both list (GET) and create (POST) operations.

    """
    queryset=QuestionsData.objects.all()
    serializer_class= QuestionsDataSerializer


def upload_csv(request):
    """
    Handle the CSV file upload and save data to the database.

    Args:
        equest (HttpRequest): The HTTP request object containing the form data.


    Returns:
        HttpResponse: If the request method is POST and the form is valid, it returns
        the success.html template with the uploaded data in the context. Otherwise,
        it returns the upload.html template with the upload form.
    """
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            next(io_string)  
            data = []
            for row in csv.reader(io_string):
                type, questions ,correct,wrong1,wrong2,wrong3= row
                QuestionsData.objects.create(type=type, questions=questions,correct=correct,wrong1=wrong1,wrong2=wrong2,wrong3=wrong3)
                data.append({'type':type,'questions':questions,'correct':correct,'wrong1':wrong1,'wrong2':wrong2,'wrong3':wrong3})
            
            return render(request, 'success.html' ,{'data':data} )
    else:
        form = UploadForm()
    
    return render(request, 'upload.html', {'form': form})


def download_csv(request):
    """
        Download CSV file containing QuestionsData.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response containing the CSV file.

    """
    # Create an HTTP response with content type 'text/csv; charset=utf-8'
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    # Set the response header to suggest downloading the file as 'data.csv'
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    # Create a CSV writer to write data into the response
    writer = csv.writer(response)
    # Write the header row to the CSV file with column names: 'type', 'questions', 'correct', 'wrong1', 'wrong2', 'wrong3'
    writer.writerow(['type', 'questions', 'correct', 'wrong1', 'wrong2', 'wrong3'])

    # Retrieve all objects from the QuestionsData model
    questions = QuestionsData.objects.all()
    # Loop through each QuestionsData object and write its data to a row in the CSV file
    for question in questions:
        writer.writerow([question.type, question.questions, question.correct, question.wrong1, question.wrong2, question.wrong3])

    # Return the response, which contains the CSV file with data from the QuestionsData model
    return response


def clear_all_data(request):
    """
    Clear all data from the database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response indicating the success of the operation.
    """
    QuestionsData.objects.all().delete()

    # Return a response to indicate the success of the operation
    return HttpResponse("All data has been cleared from the database.")


from django.http import JsonResponse
import random

from django.http import JsonResponse
import random
from .models import QuestionsData

def get_random_questions(request):
    """
    Retrieve 10 random questions from the database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The JSON response containing the selected random questions.
    """
    # Fetch all questions from the database
    all_questions = QuestionsData.objects.all()

    # Check if there are at least 10 questions in the database
    if all_questions.count() >= 10:
        # Select 10 random questions from the queryset
        random_questions = random.sample(list(all_questions), 10)
    else:
        # If there are less than 10 questions in the database, set random_questions to all available questions
        random_questions = all_questions

    # Serialize the questions to JSON
    serialized_questions = [
        {
            'type': question.type,
            'question': question.questions,
            'options': [
                {'text': question.correct, 'is_correct': True},
                {'text': question.wrong1, 'is_correct': False},
                {'text': question.wrong2, 'is_correct': False},
                {'text': question.wrong3, 'is_correct': False},
            ]
        }
        for question in random_questions
    ]

    # Return the JSON response
    return JsonResponse(serialized_questions, safe=False, json_dumps_params={'ensure_ascii': False})




# def get_50_random_questions(request):
#     """
#     Retrieve 50 random questions from the database, divided into two equal groups.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The HTTP response for the view containing the selected random questions.


#     """
#     # Fetch all questions from the database
#     all_questions = QuestionsData.objects.all()

#     # Check if there are at least 50 questions in the database
#     if all_questions.count() >= 50:
#         # Select 50 random questions from the queryset
#         random_questions = random.sample(list(all_questions), 50)

#         # Divide the randomly selected questions into two equal groups
#         middle_index = len(random_questions) // 2
#         group1 = random_questions[:middle_index]
#         group2 = random_questions[middle_index:]
#     else:
#         # If there are less than 50 questions in the database, set group1 and group2 to all available questions
#         group1 = all_questions
#         group2 = all_questions

#     # Your view logic here...
#     return render(request, 'random_questions_template.html', {'group1': group1, 'group2': group2})

def get_random_50_questions(request):
    """
    Retrieve 50 random questions from the database, divided into two equal groups.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The JSON response containing the two groups of selected random questions.
    """


    # Check if there are at least 50 questions in the database
    all_questions = QuestionsData.objects.all()

    # Check if there are at least 10 questions in the database
    if all_questions.count() >= 50:
        # Select 10 random questions from the queryset
        random_questions = random.sample(list(all_questions), 50)
    else:
        # If there are less than 10 questions in the database, set random_questions to all available questions
        random_questions = all_questions

    # Serialize the questions to JSON
    serialized_questions = [
        {
            'type': question.type,
            'question': question.questions,
            'options': [
                {'text': question.correct, 'is_correct': True},
                {'text': question.wrong1, 'is_correct': False},
                {'text': question.wrong2, 'is_correct': False},
                {'text': question.wrong3, 'is_correct': False},
            ]
        }
        for question in random_questions
    ]

    # Return the JSON response
    return JsonResponse(serialized_questions, safe=False, json_dumps_params={'ensure_ascii': False})



def display_types_and_count(request):
    """
    Display the types available in the database and count how many times each type is repeated.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response for the view containing the types and their counts.

    Note:
        - Make sure to include appropriate URL patterns to associate this view with the
          desired endpoint in your project's urls.py file.
    """
    # Fetch all questions from the database
    all_questions = QuestionsData.objects.all()

    # Extract the type field from each question and create a list of types
    types_list = [question.type for question in all_questions]

    # Use Counter to count the occurrences of each type
    type_counts = Counter(types_list)

    # Convert the Counter object to a list of tuples (type, count)
    type_count_list = list(type_counts.items())
    # Your view logic here...
    return render(request, 'types_and_count_template.html', {'type_count_list': type_count_list})
    


class QuestionsDataView(APIView):
    def post(self, request):
        serializer = QuestionsDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
# def get_random_questions(request):
#     """

#     Retrieve 10 random questions from the database.

#     Args:
#         request (HttpRequest): The HTTP request object.

#     Returns:
#         HttpResponse: The HTTP response for the view containing the selected random questions.

   
#     """
#     # Fetch all questions from the database

#     all_questions = QuestionsData.objects.all()

#     # Check if there are at least 10 questions in the database
#     if all_questions.count() >= 10:
#         # Select 10 random questions from the queryset
#         random_questions = random.sample(list(all_questions), 10)
#     else:
#         # If there are less than 10 questions in the database, set random_questions to all available questions
#         random_questions = all_questions

#     # Your view logic here...
#     return render(request, 'random_questions_template.html', {'random_questions':random_questions})
