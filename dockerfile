# Use an official Python runtime as a parent image
FROM python:alpine

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
RUN pip install pipenv

# Copy the rest of the application code into the container
COPY . /app/

RUN pipenv install

# Expose the port on which your Django app will run (default is 8000)
EXPOSE 8000

# Start the Django development server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
