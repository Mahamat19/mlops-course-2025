# Part 1: Base image and Python
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Install dependencies separately (layer caching)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY app/ .

# Switch to non-root
USER appuser

# Expose API port
EXPOSE 8000

# Start FastAPI (CMD = default args)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]