FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD ["python3", "manage.py", "runserver", "0:8000"]