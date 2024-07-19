FROM python

WORKDIR /app

COPY ../test/requirements.txt .
RUN pip install -r requirements.txt

COPY ../test/entrypoint.py .
COPY ../know_time.py .

CMD ["python", "entrypoint.py"]