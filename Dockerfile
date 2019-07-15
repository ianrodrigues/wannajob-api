FROM python:3.6-slim-stretch

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/local/app

RUN pip install --upgrade pip safety bandit pylint flake8 pytest coverage

COPY requirements.txt /usr/local/app/requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
