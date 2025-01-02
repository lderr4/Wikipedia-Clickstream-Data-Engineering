FROM python:3.9.13-slim

COPY requirements.txt /opt
RUN pip install --no-cache-dir -r /opt/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    gzip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


RUN mkdir -p /app/src


CMD tail -f /dev/null


