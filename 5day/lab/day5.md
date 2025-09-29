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

### Notes

- We copy requirements first for better caching.  
- The `.dockerignore` reduces build context size ignoring irrelevant files.
- Running as non-root improves security.  


## Part 2 — Configuration with Env Vars & `.env` Files

### Theory

- Configuration should not be hardcoded.  
- `.env` files standardize config across environments.  

### Task

1. Extract secrets from original image. This is to demo the vulnerability.
2. Modify the build and run to attach the `.env` files _externally_.


## Part 3 — Model Mounting with Volumes

### Theory

- Don’t bake models into images → rebuilding every update is slow.  
- Use volumes (bind mounts) to dynamically inject models.  

### Task

1. Add `/models` to `Dockerfile`.  
2. Add `/models` to `.dockerignore`.  
3. Run docker while mounting a volume (use `-v`).  


### Notes

- Container sees the file at runtime (like a symlink to your host).

```bash
docker run -v <host-path>:<container-path>[:opts]
```

- Now if you drop a new `model.pkl` into `./app/models`, the container uses it without rebuild.


## Part 4 — Docker Compose Basics

### Theory

- Compose = declarative, reproducible multi-service setup.  
- Easier than long `docker run` commands.  

### Task

1. Write a minimal `docker-compose.yml` for the API.  
2. Configure env vars, model mount, and secret mount.  
3. Run with `docker compose up`.  



## (BONUS) Part 5 — Secrets Management (don’t bake into images)

### Theory

- Baking secrets into images = security risk (leaks if image is pushed).  
- Instead: mount secrets or pass them at runtime.  
- .env is meant for non-sensitive config: ports, model paths, log level.
- Secrets should have stricter handling (separate files, secret stores, limited access).

### Task

1. Extract api key from running container. This is to demo the vulnerability.
2. Create a secret file for the secret.
3. Define the secret in `compose.yaml`.  
4. Modify app to read the secret at runtime or update the entrypoint to export the secret key.  


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
