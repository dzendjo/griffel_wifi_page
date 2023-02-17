FROM python:3.9

COPY requirements.txt /opt/

RUN pip install -r /opt/requirements.txt --no-use-pep517 --no-cache-dir -q --compile

COPY app/ /opt/app/

WORKDIR /opt/app

CMD ["uvicorn", "main:app"]