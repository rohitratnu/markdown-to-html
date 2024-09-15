FROM python:3.10-alpine
RUN pip install --upgrade pip
RUN apk update

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]
