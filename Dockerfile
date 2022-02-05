FROM python:3.9-alpine

WORKDIR /app

COPY . .

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --update alpine-sdk
RUN apk add --update libffi-dev
RUN python3 -m pip install "poetry==1.1.12"
RUN poetry install --no-dev --no-interaction --no-ansi

ENTRYPOINT ["poetry", "run", "python3", "/app/src/marvin/bot.py"]