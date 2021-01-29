FROM python:3.6.1-alpine
LABEL maintainer=ArunKSingh
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
