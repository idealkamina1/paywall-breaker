FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/
COPY scripts/ ./scripts/
COPY tests/ ./tests/
COPY .gitignore ./
COPY README.md ./

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "src/app.py"]