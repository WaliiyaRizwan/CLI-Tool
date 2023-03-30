FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code and app.py file into the container at /app
COPY . /app/

# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
