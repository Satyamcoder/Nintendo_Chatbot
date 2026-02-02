FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# CRITICAL: Install compatible httpx version FIRST
RUN pip install --no-cache-dir httpx==0.24.1

# Then install Groq (will use the httpx we just installed)
RUN pip install --no-cache-dir groq==0.4.2

# Install remaining dependencies
RUN pip install --no-cache-dir fastapi==0.109.2 uvicorn[standard]==0.27.1 python-dotenv==1.0.1 pydantic==2.5.0

COPY . .

RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]