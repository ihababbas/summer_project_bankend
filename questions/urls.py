from django.urls import path
from .views import upload_csv, download_csv, QuestionsDataDetailView ,QuestionsDataListView, clear_all_data ,get_random_questions,get_random_50_questions,display_types_and_count , QuestionsDataView

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('download/', download_csv, name='download_csv'),
    path('clear/',clear_all_data, name = 'clear'),
    path('random10/',get_random_questions, name = 'random10'),
    path('random50/',get_random_50_questions, name = 'random50'),
    path('count/',display_types_and_count,name ='count'),
    path('question/<int:pk>/', QuestionsDataDetailView.as_view(), name='question_detail'),
    path('questions/',QuestionsDataListView.as_view(),name='questions'),
    path('addData/', QuestionsDataView.as_view(), name = 'addData')
]