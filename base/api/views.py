from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import Company
import pandas as pd
import pickle
import numpy as np
from tensorflow.keras.models import load_model

class UploadFileView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file = request.FILES['file']
        df = pd.read_excel(file)

        for _, row in df.iterrows():
            Company.objects.create(
                revenue=row['revenue'],
                expenses=row['expenses'],
                profit=row['profit'],
                debt=row['debt'],
                assets=row.get('assets', 0),
                liabilities=row.get('liabilities', 0)
            )

        return Response({"status": "success", "message": f"{len(df)} записей добавлено"})

class PredictCreditView(APIView):
    def post(self, request):
        model = load_model('company_rating_model.h5')
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        data = request.data
        features = [
            float(data['revenue']),
            float(data['expenses']),
            float(data['profit']),
            float(data['debt']),
            float(data.get('assets', 0)),
            float(data.get('liabilities', 0))
        ]

        features_scaled = scaler.transform([features])
        prediction = model.predict(features_scaled)[0]

        return Response({
            'rating': int(prediction[0]),
            'credit_amount': round(float(prediction[1]), 2)
        })