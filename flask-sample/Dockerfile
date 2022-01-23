FROM python:3.8.9


RUN pip install Flask
RUN pip install flask-restx
RUN pip install -U flask-cors

WORKDIR /app

COPY ./ .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]