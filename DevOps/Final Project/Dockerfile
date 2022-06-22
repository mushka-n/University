FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_APP=js_example
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
