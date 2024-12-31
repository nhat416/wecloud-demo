# Build stage
FROM python:3.12-slim AS build-stage

# Environment variables
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install necessary tools
RUN apt-get update && apt-get install -y curl

# Create and activate virtual environment
RUN python -m venv $VIRTUAL_ENV

# Upgrade pip
RUN pip install --upgrade pip

# Install `uv` using `pip`
RUN pip install uv

# Copy requirements.txt and install dependencies using `uv`
COPY requirements.txt ./
RUN uv pip install -r requirements.txt

# Final stage
FROM python:3.12-slim AS final

# Environment variables
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copy the virtual environment from the build stage
COPY --from=build-stage $VIRTUAL_ENV $VIRTUAL_ENV

# Create a directory for the app
WORKDIR /app

# Copy the FastAPI app code
COPY . /app

# Expose the port uvicorn will run on
EXPOSE 8000

# Command to run the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]