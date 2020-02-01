# Base image
FROM arm32v7/python:3.6-stretch

# Meta for Docker Hub
LABEL author="matthewgleich@gmail.com"

# Install Depencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copying over files
COPY /rpiStatus /rpiStatus
WORKDIR /rpiStatus

# Running program
CMD ["python3", "main.py"]