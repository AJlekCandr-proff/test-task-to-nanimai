FROM python:3.13-slim

WORKDIR /code

RUN apt-get update && apt-get install -y make

RUN pip install --upgrade pip && pip install uv

COPY pyproject.toml uv.lock README.md /code/
RUN uv sync

COPY . /code/
