FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE $PORT 

ENV PORT 8000

VOLUME /data

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]