# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY ./requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the entire backend code to the container
COPY . .

# Expose port 3010 for the Flask application
EXPOSE 3010

# Start the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=3010"]
