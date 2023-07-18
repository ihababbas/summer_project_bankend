
import csv
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your views here.

from .models import QuestionsData
from .serializers import QuestionsDataSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UploadForm
from django.http import HttpResponse


class QuestionsDataDetailView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionsData.objects.all()
    serializer_class = QuestionsDataSerializer


def upload_csv(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            next(io_string)  # Skip the header row

            for row in csv.reader(io_string):
                type, questions,correct,wrong1,wrong2,wrong3= row
                QuestionsData.objects.create(type=type, questions=questions,correct=correct,wrong1=wrong1,wrong2=wrong2,wrong3=wrong3)

            return render(request, 'success.html')
    else:
        form = UploadForm()
    
    return render(request, 'upload.html', {'form': form})


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['type', 'questions','correct','wrong1','wrong2','wrong3'])  # Write header row

    my_models = QuestionsData.objects.all()
    for my_model in my_models:
        writer.writerow([my_model.type, my_model.questions,my_model.correct,my_model.wrong1,my_model.wrong2,my_model.wrong3])

    return response