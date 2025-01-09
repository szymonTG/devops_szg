FROM python:3.14.0a1

WORKDIR /flask_app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]

EXPOSE 5000
