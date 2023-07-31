FROM python:3.11-bookworm

RUN mkdir /project
COPY . /project
WORKDIR /project

ENTRYPOINT ["python", "main.py"]
CMD ["--help"]