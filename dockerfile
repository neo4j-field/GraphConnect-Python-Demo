FROM python:3.9
MAINTAINER AlexanderFournier

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/ /usr/src/app/client
COPY ./config/ /usr/src/app/config

ENV PYTHONPATH=/usr/src/app/pyarrow:$PYTHONPATH
ENV GOOGLE_APPLICATION_CREDENTIALS=/usr/src/app/config

CMD ["python","./client/main.py"]