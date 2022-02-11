FROM tiangolo/uvicorn-gunicorn:python3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./app ./app
COPY ./.migrations/ ./.migrations/
COPY ./alembic.ini .


RUN useradd admin && chown -R admin /src
USER admin

# Development Mode with Live Reload
ENTRYPOINT ["/start-reload.sh"]