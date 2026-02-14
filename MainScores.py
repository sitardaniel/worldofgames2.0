import os
import logging
import json
from datetime import datetime
from flask import Flask, Response, request
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from Utils import SCORES_FILE_NAME

# Structured JSON logging
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_obj)

# Configure logging
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logging.basicConfig(level=logging.INFO, handlers=[handler])
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status']
)
REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['method', 'endpoint']
)

@app.before_request
def before_request():
    request.start_time = datetime.now()

@app.after_request
def after_request(response):
    latency = (datetime.now() - request.start_time).total_seconds()
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.path,
        status=response.status_code
    ).inc()
    REQUEST_LATENCY.labels(
        method=request.method,
        endpoint=request.path
    ).observe(latency)
    logger.info(f"{request.method} {request.path} {response.status_code} {latency:.3f}s")
    return response

@app.route("/")
def score_server():
    try:
        with open(SCORES_FILE_NAME, "r") as f:
            score = int(f.readline().strip())
        return f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    except Exception:
        logger.exception("Failed to retrieve score")
        return """
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">Error: Unable to retrieve score</div></h1>
        </body>
        </html>
        """, 500

@app.route("/health")
def health():
    """Liveness probe - is the app running?"""
    return {"status": "healthy"}, 200

@app.route("/ready")
def ready():
    """Readiness probe - is the app ready to serve traffic?"""
    try:
        # Check if we can read the scores file (or create it)
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, "r") as f:
                f.read()
        return {"status": "ready"}, 200
    except Exception:
        logger.exception("Readiness check failed")
        return {"status": "not ready"}, 503

@app.route("/metrics")
def metrics():
    """Prometheus metrics endpoint"""
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    logger.info("Starting WorldofGames Score Server")
    app.run(host='0.0.0.0', port=5000)
