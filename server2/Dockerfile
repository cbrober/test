# Use Python 3.9 base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the server2.py code into the container
COPY server2.py /app/

# Install required dependencies
RUN pip install flask

# Expose port 5001 for Flask server
EXPOSE 5001

# Run the server2.py when the container starts
CMD ["python3", "server2.py"]