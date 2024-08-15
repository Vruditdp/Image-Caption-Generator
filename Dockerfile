# Using the official Python image as the base image
FROM python:3.8-slim

# Setting the working directory
WORKDIR /app

# Copying the requirements file and install dependencies
COPY . /app
# Copying requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copyingthe application code
# COPY . .

# Exposing the port the app runs on
EXPOSE 5000

# Command to run the application
CMD python ./app.py
# CMD ["python", "app.py"]
