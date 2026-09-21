FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download Standalone Tailwind CLI (Multi-Arch: x86_64 vs aarch64/arm64)
RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then \
        CLI_ARCH="tailwindcss-linux-arm64"; \
    else \
        CLI_ARCH="tailwindcss-linux-x64"; \
    fi && \
    curl -sLO "https://github.com/tailwindlabs/tailwindcss/releases/latest/download/${CLI_ARCH}" && \
    chmod +x "${CLI_ARCH}" && \
    ./"${CLI_ARCH}" -i static/css/input.css -o static/css/dist/styles.css --minify && \
    rm "${CLI_ARCH}"

# Build static files with safety dummy SECRET_KEY
RUN SECRET_KEY=build-time-dummy-key python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
