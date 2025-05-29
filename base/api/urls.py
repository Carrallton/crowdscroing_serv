from django.urls import path
from .views import UploadExcelFileView, CompanyDetailView

urlpatterns = [
    path('upload/', UploadExcelFileView.as_view(), name='upload-excel'),
    path('companies/<str:inn>/', CompanyDetailView.as_view(), name='company-detail'),
]