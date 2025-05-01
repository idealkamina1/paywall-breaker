FROM python:3.11-slim

# Install system dependencies for Playwright browsers
RUN apt-get update && \
    apt-get install -y wget gnupg libnss3 libatk-bridge2.0-0 libgtk-3-0 libxss1 libasound2 libgbm1 libxshmfence1 libxcomposite1 libxrandr2 libu2f-udev libdrm2 libxdamage1 libpango-1.0-0 libpangocairo-1.0-0 libcups2 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN python -m playwright install --with-deps

COPY src/ ./src/
COPY scripts/ ./scripts/
COPY tests/ ./tests/
COPY .gitignore ./
COPY README.md ./

EXPOSE 10000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "10000"]