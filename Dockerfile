FROM python:3.9-slim
ENV PATH="/app:${PATH}"
WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install

COPY . .

CMD ["python", "-m", "pdb", "-c", "continue", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

