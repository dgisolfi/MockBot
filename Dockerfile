FROM python:3.7
LABEL maintainer="Daniel Gisolfi"
RUN apt-get update -y \
    && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential

ENV USER_ID=<PLACEHOLDER>
ENV BOT_ID=<PLACEHOLDER>
ENV GROUP_ID=<PLACEHOLDER>
ENV API_TOKEN=<PLACEHOLDER>

EXPOSE 5050

WORKDIR /bot
COPY ./MockBot ./MockBot
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "-m", "MockBot"]

