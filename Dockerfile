FROM python

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY ./app /app

EXPOSE 8000

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["gunicorn",  "main:app", "--worker-class",  "uvicorn.workers.UvicornWorker",  "--bind",  "0.0.0.0:8000"]