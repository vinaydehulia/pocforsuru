# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory contents (curtdpy.py) into the container at /app
COPY curtdpy.py /app/

# Step 4: Install Flask
RUN pip install flask

# Step 5: Expose port 5000 for the Flask app
EXPOSE 5000

# Step 6: Run the Flask app
CMD ["python", "curtdpy.py"]
