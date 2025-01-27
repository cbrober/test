# Use Python 3.9 base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the server1.py code into the container
COPY server1.py /app/

# Install required dependencies
RUN pip install flask requests

# Expose port 5000 for Flask server
EXPOSE 5000

# Run the server1.py when the container starts
CMD ["python3", "server1.py"]