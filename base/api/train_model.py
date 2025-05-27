import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import StandardScaler
import pickle

# Загрузка данных
df = pd.read_csv('data/companies.csv')

X = df[['revenue', 'expenses', 'profit', 'debt', 'assets', 'liabilities']]
y = df[['rating', 'credit_amount']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = Sequential([
    Dense(64, activation='relu', input_shape=(6,)),
    Dense(64, activation='relu'),
    Dense(2)  # rating, credit_amount
])

model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.1)

# Сохранение модели и скалеров
model.save('company_rating_model.h5')
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)