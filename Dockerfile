FROM python:3.6.15-slim

# Copy local code to the container image
COPY . /app

# Sets the working directory
WORKDIR /app

# To fix ImportError: libGL.so.1: cannot open shared object file: No such file or directory
RUN apt-get update && apt-get install -y libgl1

#Install python libraries from requirements.txt
RUN pip3 install -r requirements.txt

# Set $PORT environment variable
ENV PORT 8080

# Run the web service on container startup
CMD exec gunicorn --bind :$PORT --timeout 0 app:app