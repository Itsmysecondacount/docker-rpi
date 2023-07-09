FROM arm32v7/python:3.7-slim-bullseye
RUN apt-get update \
&& apt-get install build-essential -y \
&& pip install poetry

COPY ./pyproject.toml /app/
WORKDIR /app/
RUN poetry install --no-dev

# Install app
COPY ./rpiserver2 /app/rpiserver2
RUN poetry install --no-dev
ENTRYPOINT poetry run uvicorn rpiserver2.server:valve_app --reload --host 0.0.0.0 --port 8080