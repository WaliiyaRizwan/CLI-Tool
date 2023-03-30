# Use an official Python runtime as a parent image
FROM python:3.7.3-stretch

# Set the working directory to /app
WORKDIR /app

# Copy source code and app.py file into the container at /app
COPY . app.py /app/

# Install packages from requirements.txt file
# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Explanation:
# - This Dockerfile sets up a Python 3.7.3 environment as the base image.
# - The working directory is set to /app, and the source code and app.py file are copied into the container at /app.
# - The requirements.txt file is used to install any necessary packages.
# - hadolint ignore=DL3013 is used to ignore a warning from hadolint, which is a tool for analyzing Dockerfiles.
