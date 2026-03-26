# -------------------------
# Stage 1: Builder
# -------------------------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

# Install packages into /install (accessible to non-root)
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# -------------------------
# Stage 2: Final Image
# -------------------------
FROM python:3.11-slim

WORKDIR /app

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from builder to /usr/local
COPY --from=builder /install /usr/local

# Copy app code
COPY . .

# Add non-root user
RUN useradd -m appuser
USER appuser

# Ensure Python scripts use unbuffered output
ENV PYTHONUNBUFFERED=1
# Ensure pip-installed packages are in PATH
ENV PATH=/usr/local/bin:$PATH

# Health check
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1

# Expose port
EXPOSE 5000

# Run with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]