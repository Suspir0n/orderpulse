# Use the official Python image as a base
FROM python:3.11

# Define the working directory inside the container
WORKDIR /app

# Copy the necessary files to the container (requirements.txt and the app folder)COPY requirements.txt .
COPY ../app ./app
COPY requirements.txt .

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by FastAPI (by default it is port 8000)
EXPOSE 8000

# Command to start FastAPI when the container runs
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
