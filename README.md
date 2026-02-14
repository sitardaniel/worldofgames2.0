# World of Games 2.0

A Python-based gaming platform with Flask web server, featuring DevOps best practices including CI/CD, Kubernetes deployment, monitoring, and security hardening.

## Features

- **3 Interactive Games**: Memory Game, Guess Game, Currency Roulette
- **Score Tracking**: Persistent score storage with web interface
- **Health Endpoints**: `/health`, `/ready` for Kubernetes probes
- **Prometheus Metrics**: `/metrics` endpoint for monitoring
- **Structured Logging**: JSON-formatted logs for aggregation

## Tech Stack

- Python 3.11
- Flask + Gunicorn
- Docker (multi-stage build)
- Kubernetes
- Prometheus metrics
- Jenkins CI/CD

## Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/worldofgames2.0.git
cd worldofgames2.0

# Set up environment
cp .env.example .env
# Edit .env and add your CURRENCY_API_KEY

# Install dependencies
pip install -r requirements.txt

# Run the game
python MainGame.py

# Run the score server
python MainScores.py
```

### Docker

```bash
# Build and run
CURRENCY_API_KEY=your_key docker-compose up --build

# Access the score server
open http://localhost:5000
```

### Kubernetes

```bash
# Create secret (edit with your API key first)
kubectl apply -f k8s/secret.yaml

# Deploy application
kubectl apply -f k8s/

# Check status
kubectl get pods -l app=worldofgames
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `/` | Score display page |
| `/health` | Liveness probe |
| `/ready` | Readiness probe |
| `/metrics` | Prometheus metrics |

## CI/CD Pipeline

The Jenkins pipeline includes:

1. **Checkout** - Clone repository
2. **Install Dependencies** - pip install
3. **Code Quality** (parallel):
   - Linting (flake8)
   - Security scan (bandit)
4. **Test** - pytest with coverage
5. **Build** - Docker image
6. **E2E Tests** - Selenium tests
7. **Push** - Docker Hub (main branch only)
8. **Deploy** - Kubernetes (main branch only)

## Project Structure

```
worldofgames2.0/
├── MainGame.py          # CLI entry point
├── MainScores.py        # Flask web server
├── MemoryGame.py        # Memory game logic
├── GuessGame.py         # Guess game logic
├── CurrencyRouletteGame.py  # Currency game logic
├── Score.py             # Score management
├── Utils.py             # Utilities
├── Dockerfile           # Multi-stage Docker build
├── docker-compose.yml   # Docker Compose config
├── Jenkinsfile          # CI/CD pipeline
├── requirements.txt     # Python dependencies
├── k8s/                 # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── secret.yaml
│   ├── pvc.yaml
│   └── ingress.yaml
└── tests/               # Unit tests
    ├── test_api.py
    ├── test_games.py
    └── test_score.py
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `CURRENCY_API_KEY` | API key for freecurrencyapi.com | Yes |

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=. --cov-report=html

# Run linting
flake8 --max-line-length=120 .

# Run security scan
bandit -r . -x ./venv,./tests
```

## Monitoring

The application exposes Prometheus metrics at `/metrics`:

- `http_requests_total` - Total HTTP requests by method, endpoint, status
- `http_request_duration_seconds` - Request latency histogram

## Security Features

- Environment-based secrets (no hardcoded credentials)
- Non-root Docker user
- API key via HTTP header (not URL)
- Input validation on all user inputs
- Generic error messages (no stack traces exposed)

## License

MIT
