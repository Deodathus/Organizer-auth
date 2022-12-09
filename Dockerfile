FROM python:3.9.6 AS builder
EXPOSE 8000
WORKDIR /auth
COPY requirements.txt /auth
COPY . /auth
RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

RUN addgroup --system docker
RUN adduser --system --shell /bin/bash --ingroup docker vscode