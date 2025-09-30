# Lab: Containerizing an ML API with Docker & Docker Compose

## Overview

In this lab, you will containerize a FastAPI ML app and learn essential Docker concepts for MLOps.  
We’ll focus on how to:  

- Write good Dockerfiles (layers, cache, non-root, .dockerignore).  
- Configure containers with env vars and `.env` files.  
- Mount trained models dynamically (no rebuilds needed).  
- Manage secrets safely (don’t bake into images).  
- Use Docker Compose for reproducible multi-service setups.  
- (Optional) Optimize images with multi-stage builds and wheels.  

---

## Part 1 — Dockerfile Best Practices

### Theory

- **Base images:** slim vs full (trade-off size vs compatibility).  
- **Layers & caching:** each Dockerfile instruction creates a layer. Order matters.  
- **`.dockerignore`:** prevents unnecessary files from being copied (saves build time & size).  
- **Non-root users:** containers should not run as root in production.  

### Task

1. Create a `Dockerfile` for the FastAPI app. Set the working directory. Copy all the needed files. Install requirements, switch to a non-root user and run the container.
2. Use `.dockerignore` to exclude `.git`, `__pycache__/`, `.venv/`.  
3. Expose port `8000`.  
4. Run the container and access the app.  

### Solution

**Dockerfile:**

```dockerfile
# Part 1: Base image and Python
FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Install dependencies separately (layer caching)
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY app/ .

# Switch to non-root
USER appuser

# Expose API port
EXPOSE 8000

# Start FastAPI (CMD = default args)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**.dockerignore:**

```
__pycache__/
*.pyc
.venv/
.git/
```

**Build & Run:**

```bash
docker build -t mlapi:latest .
docker run -p 8000:8000 mlapi:latest
```

Run curl requests to test the endpoints:

```bash
curl -X POST localhost:8000/predict/logistic_model -H "Content-Type: application/json" \
  -d '{"sepal_length":1.1,"sepal_width":3.1,"petal_length":2.1,"petal_width":4.1}'
curl -X POST localhost:8000/predict_secure/rf_model \
  -H "X-API-Key: dev-12345" -H "Content-Type: application/json" \
  -d '{"sepal_length":1.2,"sepal_width":2.2,"petal_length":3.3,"petal_width":4.4}'
```

### Notes

- We copy requirements first for better caching.  
- The `.dockerignore` reduces build context size ignoring irrelevant files.
- Running as non-root improves security.  

---

## Part 2 — Configuration with Env Vars & `.env` Files

### Theory

- Configuration should not be hardcoded.  
- `.env` files standardize config across environments.  

### Task

1. Extract secrets from original image.
2. Modify the build and run to attach the `.env` files _externally_.

### Solution

- Extract secrets with:

```bash
docker cp busy_lederberg:/app/.env ./stolen.env
```

- Add `app/.env` to `.dockerignore`.

- Run:

```bash
docker build -t mlapi_noenv:latest .
docker run --env-file app/.env -p 8000:8000 mlapi_noenv:latest
```

---

## Part 3 — Model Mounting with Volumes

### Theory

- Don’t bake models into images → rebuilding every update is slow.  
- Use volumes (bind mounts) to dynamically inject models.  

### Task

1. Add `/models` to `Dockerfile`.  
2. Add `/models` to `.dockerignore`.  
3. Run docker while mounting a volume (use `-v`).  

### Solution

```bash
docker run --env-file app/.env -p 8000:8000  -v ./app/models:/models mlapi_nomodel
```

### Notes

- Container sees the file at runtime (like a symlink to your host).

```bash
docker run -v <host-path>:<container-path>[:opts]
```

- Now if you drop a new `model.pkl` into `./app/models`, the container uses it without rebuild.

---

## Part 4 — Docker Compose Basics

### Theory

- Compose = declarative, reproducible multi-service setup.  
- Easier than long `docker run` commands.  

### Task

1. Write a minimal `docker-compose.yml` for the API.  
2. Configure env vars, model mount, and secret mount.  
3. Run with `docker compose up`.  

### Solution

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    env_file: ./app/.env
    volumes:
      - ./app/models:/models
```

Run:

```bash
docker compose up --build
```

---

## (BONUS) Part 5 — Secrets Management (don’t bake into images)

### Theory

- Baking secrets into images = security risk (leaks if image is pushed).  
- Instead: mount secrets or pass them at runtime.  
- .env is meant for non-sensitive config: ports, model paths, log level.
- Secrets should have stricter handling (separate files, secret stores, limited access).

### Task

1. Extract api key from running container.
2. Create a secret file for the secret.
3. Define the secret in `compose.yaml`.  
4. Modify app to read the secret at runtime.  

### Solution

- Check for secrets in env file.

```bash
docker inspect <container_id>
```

- Update `compose.yaml`

```yaml
services:
  api-container:
    build: .
    image: mlapi_nosecret:latest
    ports:
      - "8000:8000"
    env_file: ./app/.env2
    volumes:
      - ./app/models:/models:ro
    secrets:
      - source: api_key
        target: api_key

secrets:
  api_key:
    file: ./secrets/api_key.txt
```

- In `auth.py` load `API_KEY` from newly added secret

```python
def load_secret(name: str, default=None):
    # allow local dev via dotenv/env
    val = os.getenv(name)
    if val:
        return val
    # prod: mounted file at /run/secrets/<lowercased name>
    p = Path(f"/run/secrets/{name.lower()}")
    if p.exists():
        print(p.read_text().strip())
        return p.read_text().strip()
    print("nista")
    print(name.lower())
    return default


API_KEY = load_secret("API_KEY")
```

- Secret can still be "leaked":

```bash
docker compose exec api sh -c 'cat /run/secrets/api_key'
```

### Notes

- `docker inspect` leakage is worse
  - Secrets live in Docker’s control plane state.
  - Anyone with read-only access to Docker’s API/daemon can dump them without touching the container.
  - They may be logged in CI/CD pipelines (inspect is often used for debugging).
  - They persist until you remove the container.

- `docker exec` leakage is acceptable (to a point)
  - Anyone who can exec is basically root on the host already.
  - Reading secrets inside the container is expected — the app needs them to run.
  - Once the container is gone, the secret is gone with it (if using tmpfs / proper secrets).

---

## Wrap-Up — Key MLOps Lessons

- **Dockerfile:** reproducible envs, caching, non-root, `.dockerignore`.  
- **Env vars & .env:** config = externalized.  
- **Volumes:** models/data stay outside the image.  
- **Compose:** reproducible dev/prod setups.
