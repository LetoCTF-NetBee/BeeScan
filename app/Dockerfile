FROM python:3
WORKDIR /app
ENV FLASK_APP=__init__.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt update -y && apt install -y build-essential
COPY requirements.txt requirements.txt
RUN pip install wheel
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]