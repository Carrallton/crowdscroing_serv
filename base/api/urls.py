from django.urls import path
from .views import UploadExcelFileView

urlpatterns = [
    path('upload/', UploadExcelFileView.as_view(), name='upload-excel'),
]