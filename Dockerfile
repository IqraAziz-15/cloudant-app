# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install necessary Python packages
RUN pip install --no-cache-dir requests

# Set environment variables for Cloudant credentials
# Replace with your actual values or use Docker secrets for security
ENV ACCOUNT_NAME = "293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix.cloudantnosqldb.appdomain.cloud"
ENV API_KEY = "0Peu2FUOWZpa1C-oR7sKO-F4wvBaU7jcI6n7KJL1vHiS"
ENV BASE_URL = f"https://293e9a3b-b044-4b74-a92a-3b331de2350a-bluemix.cloudantnosqldb.appdomain.cloud"

# Expose the port if necessary (optional)
# EXPOSE 8080

# Run the Python script
CMD ["python3", "cloudantapp.py"]
