##############
# Base Stage
##############
FROM python:3.6-slim-stretch AS base

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/local/app

RUN pip install --upgrade pip gunicorn

COPY requirements.txt /usr/local/app/requirements.txt
RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--log-level", "warning", "--reload", "wannajob.wsgi:application"]


#####################
# Development Stage
#####################
FROM base AS development

RUN pip install --upgrade safety bandit pylint flake8 pytest coverage


####################
# Production Stage
####################
FROM base AS production

ENV DJANGO_SETTINGS_MODULE 'wannajob.settings.production'

COPY . /usr/local/app


#################
# Statics Stage
#################
FROM production AS statics

RUN python manage.py collectstatic --no-input --clear


############################
# Production (Nginx) Stage
############################
FROM nginx:1.17-alpine AS nginx

COPY ./docker/nginx/django.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/local/app

RUN mkdir statics
COPY --chown=nginx:nginx --from=statics /usr/local/app/static /usr/local/app/static
