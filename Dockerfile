FROM python:3.11-alpine

# Create a non-root user for the application
RUN adduser -D -s /bin/bash hbnb

# Define a working directory for the application
WORKDIR /home/hbnb/app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app to the container
COPY app /home/hbnb/app

# Copy data files into the container with ownership set to hbnb user
COPY --chown=hbnb:hbnb data/* /home/hbnb/app/data/

# Set permissions for the data directory to allow read/write by owner and group
RUN chmod -R 755 /home/hbnb/app/data

# Switch to the non-root user for security reasons
USER hbnb

# Define a volume for the data directory to persist data outside the container
VOLUME ["/home/hbnb/app/data"]


# Define working directory for the application
WORKDIR /home/hbnb/app

# Execute the application with gunicorn
CMD ["python", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]