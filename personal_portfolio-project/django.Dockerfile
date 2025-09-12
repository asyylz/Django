FROM python:3.13.1

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the Django dev server (hot reload works with mounted volumes)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
