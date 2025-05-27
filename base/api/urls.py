from django.urls import path
from .views import UploadFileView, PredictCreditView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('predict/', PredictCreditView.as_view(), name='predict'),
]