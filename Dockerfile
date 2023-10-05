# Use the official Python 3.9 image as a parent image
FROM python:3.11

# Update package lists
RUN apt-get update

# Remove any previously installed conflicting packages (optional)
RUN apt-get remove --purge python3-pkg-resources python3-setuptools

# Install necessary dependencies
RUN apt-get install -y \
    git \
    python3-dev \
    build-essential \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose the port that the Flask app listens on
EXPOSE 8502

# Create a directory for your application
RUN mkdir /image

# Copy your application files into the container
COPY ./app.py /image/
COPY ./requirements.txt /image/


# Set the working directory to /llama2
WORKDIR /image


# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Start the Flask app when the container launches
CMD ["python", "app.py"]
