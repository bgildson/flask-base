FROM python:3.7

RUN useradd -ms /bin/bash flask

ENV PYTHONUNBUFFERED 1

WORKDIR /home/flask/app

ENV PATH $PATH:/home/flask/.local/bin

COPY poetry.lock pyproject.toml ./

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root

COPY . .

EXPOSE 5000

CMD gunicorn -w 5 -b 0.0.0.0:5000 'app:create_app()'
