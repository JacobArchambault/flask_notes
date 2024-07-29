FROM python:alpine AS base
ENV PYBASE /pybase
ENV PYTHONUSERBASE $PYBASE
ENV PATH $PYBASE/bin:$PATH
ENV PYTHONDONTWRITEBYTECODE=1

FROM base AS builder
WORKDIR /tmp
COPY requirements.txt .
RUN PIP_USER=1 PIP_IGNORE_INSTALLED=1 pip install --no-compile --no-cache-dir -r requirements.txt

FROM base
COPY --from=builder /pybase /pybase
COPY . /app/notes
WORKDIR /app
EXPOSE 80
CMD ["gunicorn", "-b 0.0.0.0:80", "notes:create_app()"]
