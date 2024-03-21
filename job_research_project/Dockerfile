FROM python:3.8

WORKDIR /app

RUN pip install requests==2.26.0 && pip install pandas && pip install psycopg2 && pip install sqlalchemy 

COPY api_call.py .

CMD ["python", "api_call.py"]
