FROM python:3.12-alpine AS build
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /usr/src/app

RUN apk add --no-cache build-base libpq-dev

RUN python -m venv /opt/venv
ENV VIRTUAL_ENV="/opt/venv"

COPY ./pyproject.toml ./uv.lock ./
RUN uv sync --frozen --no-default-groups --group prod

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
