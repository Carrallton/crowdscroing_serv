FROM python:3.11-slim
WORKDIR /base
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt&& \
    pip install gunicorn
COPY . .
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", " app.wsgi:application", "--bind", "0.0.0.0:8000"]