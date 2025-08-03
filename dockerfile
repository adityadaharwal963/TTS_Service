# 1. base image  the foundation layer , this will pulled from image docker hub
FROM python:3.11-slim

# 2. this will create folder in docker container , set  working directory for any subsequent RUN, CMD, COPY, and ADD commands 
# if this dir doesn't exist docker will create it 
WORKDIR /model_server

COPY requirements.txt .

# Install dependencies without storing the cache 
# By using --no-cache-dir, you prevent this useless cache from being written, which helps keep your final Docker image size smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy file to docker container
COPY . .

EXPOSE 8000
# command to run the application
CMD ["python", "src/server.py"]