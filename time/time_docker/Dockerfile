FROM python

WORKDIR /app

COPY ../time_docker/requirements.txt .
RUN pip install -r requirements.txt

COPY ../time_docker/time_server.py .
COPY ../know_time.py .

CMD ["python", "time_server.py"]