FROM python:3.10.0-buster

RUN apt-get update && apt-get upgrade -y \
&& apt-get install -y pipenv \
&& rm -rf /var/lib/apt/lists/*

EXPOSE 7070
WORKDIR /app
COPY . /app

RUN pipenv install --system --deploy
ENTRYPOINT ["python3"]
CMD ["debug_msg_api.py"]
