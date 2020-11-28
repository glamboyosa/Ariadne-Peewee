FROM python:3.8

WORKDIR /code

COPY requirements.txt . 

RUN pip install -r requirements.txt 

COPY . . 

EXPOSE 8000

CMD ["uvicorn", "index:app", "--host", "127.0.0.1", "--port", "8000"]