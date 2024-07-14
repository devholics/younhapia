FROM python:3.12-alpine AS build

WORKDIR /usr/src/app

RUN apk add --no-cache poetry
RUN python -m venv /opt/venv
ENV VIRTUAL_ENV="/opt/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apk add --no-cache build-base libpq-dev

COPY ./pyproject.toml ./poetry.lock ./
RUN poetry install --with prod --without dev

FROM python:3.12-alpine

WORKDIR /usr/src/app

RUN apk add --no-cache libpq
COPY --from=build /opt/venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"
COPY . .

ENV PORT=8080
ENV DJANGO_SETTINGS_MODULE=younhapia.settings.prod

VOLUME ["/usr/src/conf"]

ENTRYPOINT ["./docker-entrypoint.sh"]

CMD ["gunicorn", "younhapia.wsgi", "-b", "0.0.0.0:$PORT"]
