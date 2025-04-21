# Use an official Python runtime as a parent image
ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Use a specific Poetry version
ENV POETRY_VERSION=1.7.1
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_CREATE=false

# Install poetry and make
RUN apt-get update \
    && apt-get install --no-install-recommends -y curl make \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get remove -y curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add poetry to path
ENV PATH="$POETRY_HOME/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the dependency files from the build context root
COPY pyproject.toml poetry.lock* ./

# Install dependencies
# Include dev dependencies to make ruff available
RUN poetry install --no-root

# Copy the rest of the application code (if needed later)
# COPY . .

# Command to run the application (replace with your actual command)
# CMD ["python", "your_app_main_script.py"] 