FROM python:3.11-slim-bookworm
RUN apt-get update && apt-get install -y git
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

CMD ["uv", "run", "petals-bootstrap", "--identity_path", "p2p.id"]