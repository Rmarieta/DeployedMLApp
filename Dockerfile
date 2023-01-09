FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD gunicorn --workers=4 --bind 0.0.0.0:3000 app:app
