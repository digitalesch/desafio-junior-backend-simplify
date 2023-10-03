FROM python

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

COPY ./app /app

EXPOSE 80

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
 
CMD ["gunicorn",  "main:app",  "--workers",  "4",  "--worker-class",  "uvicorn.workers.UvicornWorker",  "--bind",  "0.0.0.0:80"]