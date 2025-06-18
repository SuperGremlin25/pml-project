FROM python:3.10-slim

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY backend .
COPY mcp-tools ./mcp-tools

# Create ops-logs directory
RUN mkdir -p ops-logs

# Make the MCP tools executable
RUN chmod +x mcp-tools/*.py

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
