FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

RUN python -m venv /opt/venv
ENV PATH="opt/venv/bin:$PATH"

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY . /app

EXPOSE 8002

# Définir la commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]