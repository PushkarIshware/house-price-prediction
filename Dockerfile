FROM python:3.11-alpine 

# Set work directory
WORKDIR /code

# suitable packages requried for apis.
RUN apk update && apk add --no-cache \
    bash \
    build-base \
    curl \
    libc-dev \
    g++ \
    gnupg \
    krb5 \
    krb5-dev \
    unixodbc-dev \
    libexpat \
    gcc \
    python3-dev \
    musl-dev \
    linux-headers \
    libpq-dev \
    libffi-dev

COPY ./ .

RUN pip3 install -r requirements.txt

# Expose port (for uvicorn)
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
