from django.urls import path
from .views import upload_csv, download_csv, QuestionsDataDetailView ,QuestionsDataListView

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('download/', download_csv, name='download_csv'),
    path('mymodel/<int:pk>/', QuestionsDataDetailView.as_view(), name='mymodel_detail'),
    path('view/',QuestionsDataListView.as_view(),name='list')
]