# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /home/fti-pdaspute/Desktop/api_test/fast_api_auth

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]