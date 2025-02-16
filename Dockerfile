# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    fonts-dejavu \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*
	
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py .

# Copy the DejaVuSans-Bold.ttf font into the container
COPY dejavu-sans-bold.ttf /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf

# Refresh the font cache
RUN fc-cache -f -v

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]