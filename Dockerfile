FROM python:3.11-alpine

# Create a non-root user for the application
RUN adduser -D -s /bin/bash hbnb

# Log in as root user
USER root

# Define the working directory for the application
WORKDIR /home/hbnb/app

# Copy the configuration files into the container
COPY requirements.txt .
COPY app /home/hbnb/app
COPY data /home/hbnb/app/data 

# Install dependencies of Python
RUN pip install --no-cache-dir -r requirements.txt

#Define the environment variables and expose the port
ENV PORT 8000
EXPOSE 8000

# Define permissions for the data directory
RUN mkdir -p /home/hbnb/app/data \
    && chown -R hbnb:hbnb /home/hbnb/app/data

# Log in as a non-root user
USER hbnb

# Define the volume for the data directory
VOLUME ["/home/hbnb/app/data"]

# Define working directory for running the application
WORKDIR /home/hbnb/app

# Run the application with Gunicorn
CMD ["python", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]