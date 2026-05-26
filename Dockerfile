# Use an official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV HOME=/home/user
ENV PATH=/home/user/.local/bin:$PATH

# Set up working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set up a new user 'user' with UID 1000 for Hugging Face Spaces compliance
RUN useradd -m -u 1000 user

# Copy the requirements file first to leverage Docker cache
COPY --chown=user:user requirements.txt /app/

# Switch to the non-root user
USER user

# Install pip dependencies inside the user's home folder context
RUN pip install --no-cache-dir --user -r requirements.txt

# Copy the rest of the application files
COPY --chown=user:user . /app/

# Expose the standard port expected by Hugging Face Spaces
EXPOSE 7860

# Start the Flask application using Gunicorn, binding to port 7860
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app", "--workers", "1", "--timeout", "120"]
