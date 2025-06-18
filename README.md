# PML Fiber Infrastructure Tracker

A modular platform for tracking and managing fiber optic infrastructure deployments using Model Context Protocol (MCP) tools and automation APIs.

## Features

- 🔌 Fiber splice logging and tracking
- 📊 Real-time operation logging
- 🔒 Cloudflare Tunnel support for secure access
- 🛠️ CLI tools for field operations
- 📱 REST API for system integration

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/supergremlin25/pml-project.git
cd pml-project
```

2. Set up the environment:
```bash
cd infra
cp .env.example .env
# Edit .env with your configuration
```

3. Start the services:
```bash
docker compose up -d
```

4. Verify the installation:
```bash
curl http://localhost:8000/health
```

## MCP Tools Usage

### Logging a Fiber Splice

```bash
python mcp-tools/splice_logger.py \
  --crew "Team1" \
  --segment "SEG001" \
  --type "fusion" \
  --notes "Clean splice, no issues"
```

Valid splice types:
- fusion
- mechanical
- preconnectorized

## API Documentation

Once the server is running, visit:
- OpenAPI documentation: http://localhost:8000/docs
- ReDoc alternative: http://localhost:8000/redoc

## Project Structure

```
pml-project/
├── backend/              # FastAPI backend service
│   ├── app/
│   │   ├── core/        # Core functionality
│   │   └── routes/      # API endpoints
│   └── main.py          # Application entry point
├── frontend/            # Future web interface
├── mcp-tools/           # CLI tools
├── infra/               # Infrastructure configs
│   ├── cloudflared/     # Cloudflare tunnel config
│   └── docker-compose.yml
├── scripts/             # Utility scripts
├── docs/               # Documentation
└── ops-logs/           # Operation logs
```

## Development

### Prerequisites

- Docker and Docker Compose
- Python 3.10 or later
- [Cloudflare account](https://dash.cloudflare.com) (for tunnel setup)

### Local Development

1. Create a Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend in development mode:
```bash
cd backend
uvicorn main:app --reload
```

## Built By
- SuperGremlin25
- Jonathan McKee

## License

This project is licensed under the MIT License - see the LICENSE file for details.
