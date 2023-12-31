[![Python Package](https://github.com/Suspir0n/orderpulse/actions/workflows/main.yml/badge.svg)](https://github.com/Suspir0n/orderpulse/actions/workflows/main.yml)
![GitHub contributors](https://img.shields.io/github/contributors/Suspir0n/orderpulse)
[![GitHub tag](https://img.shields.io/github/tag/Suspir0n/orderpulse.svg)](https://github.com/Suspir0n/orderpulse/tags)


# Order Pulse

Imagine a platform that handles real-time orders from an online store. This system uses a clean architecture and incorporates several technologies to ensure scalability, reliability and adequate monitoring.

## Description

This project will help in processing requests using Rabbitmq, Kafka, Grafana, SonaQube, Keyclock, among others, ensuring the best performance and commitment to the processes.

## Starting

To run the project, you will need to install the following programs:

- [Python: Required to create the project](https://www.python.org/downloads/)
- [Docker: Required to create the containers](https://www.docker.com/)
- [VS Code: For project development](https://code.visualstudio.com/)

## ⌨️ Developing

Use Gitpod, a free online development environment for GitHub.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Suspir0n/orderpulse.git)

Or use the code locally using:
```
$ cd "directory of your choice"
$ git clone https://github.com/Suspir0n/orderpulse.git
```

### Building

To build a FastAPI application, run the commands below:

```
$ docker-compose up --build -d
```

These are the dependencies within requirements.txt:

```
annotated-types==0.6.0
anyio==4.2.0
click==8.1.7
colorama==0.4.6
commit-linter==1.0.3
fastapi==0.108.0
h11==0.14.0
httptools==0.6.1
idna==3.6
pydantic==2.5.3
pydantic_core==2.14.6
python-dotenv==1.0.0
PyYAML==6.0.1
sniffio==1.3.0
starlette==0.32.0.post1
typing_extensions==4.9.0
uvicorn==0.25.0
watchfiles==0.21.0
websockets==12.0
```

## Test

In this lib, functional tests were used, with it we can run it like this:

    python -m unittest discover tests -v

## Additional

In this lib we use loggings, to be able to know everything that is going on behind the scenes, as well as to know if there was any error or bug somewhere in the code, it will demonstrate for you

## Configuration

To execute the project, it is necessary to use VsCode or an IDE of your preference, so that it identifies the dependencies necessary for execution in the repository. Once the project is imported, it will be possible to test its functionality in real time.

## Contributions

Contributions are always welcome! I hope I have helped someone in need.

## 🔓 License
MIT © [Evandro Silva](https://www.linkedin.com/in/suspir0n/)
