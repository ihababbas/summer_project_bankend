
import csv
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView ,ListCreateAPIView
# Create your views here.
from .models import QuestionsData
from .serializers import QuestionsDataSerializer
from .forms import UploadForm
from django.http import HttpResponse
import io

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
            next(io_string)  # Skip the header row
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







# def upload_csv(request):
#     # Check if the form has been submitted (POST method)
#     if request.method == 'POST':
#         # Create an instance of the UploadForm, using the form data from the request

#         form = UploadForm(request.POST, request.FILES)
#         # Check if the form data is valid

#         if form.is_valid():
#             # Retrieve the uploaded CSV file from the form
#             csv_file = request.FILES['csv_file']

#             # Decode the CSV file content from bytes to a string using utf-8 encoding
#             decoded_file = csv_file.read().decode('utf-8')

#             # Create a StringIO object to read the decoded CSV content line by line
#             io_string = io.StringIO(decoded_file)

#             # Skip the header row (first row) since it contains column names
#             next(io_string)

#             # Initialize an empty list to store the data from each row of the CSV file
#             data = []

#             # Iterate over each row in the CSV file
#             for row in csv.reader(io_string):

#                 # Extract the 'name' and 'email' values from the current row
#                 name, email = row

#                 # Create a MyModel object with the extracted data and save it to the database
#                 MyModel.objects.create(name=name, email=email)

#                 # Append the 'name' and 'email' values to the 'data' list for later use
#                 data.append({'name': name, 'email': email})

#             # After processing all rows, render the 'success.html' template
#             # and pass the 'data' list as a context variable for displaying the uploaded data
#             return render(request, 'success.html', {'data': data})

#     else:
#         # If the form hasn't been submitted (GET method), create an empty instance of the UploadForm
#         form = UploadForm()

#     # Render the 'upload.html' template with the UploadForm instance for displaying the upload form
#     return render(request, 'upload.html', {'form': form})
