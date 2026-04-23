FROM python:3.10-slim 
ENV PYTHONDONTWRITEBYTECODE=1m
ENV PYTHONUNBUFFERED=1
WORKDIR /apps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .  
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]

