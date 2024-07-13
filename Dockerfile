# Official FastAPI Image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements file to the container
COPY ./requirements.txt /app/requirements.txt

# Install the requirements
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entire project to the container
COPY . /app

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
