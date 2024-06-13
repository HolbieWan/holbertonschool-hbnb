FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV APP_PORT=8000

EXPOSE $APP_PORT

VOLUME app/data

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:$APP_PORT", "app:app"]