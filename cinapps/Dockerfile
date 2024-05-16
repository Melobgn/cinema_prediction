FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt .

RUN python -m venv /opt/venv
ENV PATH="opt/venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /app

EXPOSE 8001

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh","/app/entrypoint.sh"]