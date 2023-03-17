FROM arm64v8/python:3.11.2-alpine3.17

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8383"]
