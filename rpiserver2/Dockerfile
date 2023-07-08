FROM arm32v7/python:3.7-slim-buster
RUN apt-get update \
&& apt-get install build-essential -y \
&& pip install poetry

COPY ./pyproject.toml /app/
WORKDIR /app/
RUN poetry install --no-dev