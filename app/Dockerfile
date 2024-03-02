FROM python:3.12

# Poetry
ENV POETRY_HOME=/etc/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH $POETRY_HOME/bin:$PATH
RUN poetry config virtualenvs.create false

# SQLite
RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app

COPY . .

RUN poetry install

#CMD ["python","/app/src/app.py"]