Internal Utility Service – Production-Ready Deployment
Overview
This project transforms a basic Flask application into a production-ready, secure, and automated system using modern DevOps practices.
The system includes:
•	Multi-stage Docker containerization
•	CI/CD pipeline with automated testing and deployment
•	Secure secrets management
•	Reverse proxy with HTTPS
•	Zero-downtime deployment (Blue-Green)
•	Production hardening on AWS EC2
________________________________________
Technical Requirements
To ensure the project functions correctly, the following dependencies are managed within the environment:
•	Core: Flask==2.2.5, 
•	Werkzeug==2.3.7
•	Production Server: gunicorn
•	AWS Integration: boto3
•	Testing & Quality: pytest, flake8
________________________________________

Dockerization & Port Configuration
Multi-stage Build
The Dockerfile uses a multi-stage build to reduce image size, separate environments, and improve security.
•	Application Port: The Flask application is configured to run on Port 5000.
•	Non-root user: Execution is restricted to a dedicated user for security.
•	Base Image: Uses python:3.11-slim for a minimal footprint.
•	Optimization: .dockerignore reduces build context.
•	HEALTHCHECK is configured on the /health endpoint.
________________________________________
CI/CD Pipeline
Pipeline stages:
1.  Check
•	Linting with flake8
•	Testing with pytest
•	Pipeline fails if tests fail
2. Build & Push
•	Builds Docker image
•	Pushes to Docker Hub with latest tag
3. Deployment
•	Automatically deploys to EC2 on push to main
•	Uses SSH via GitHub Actions
•	Runs container with --restart always
________________________________________
Secrets Management
Approach
•	CI secrets → GitHub Secrets
•	Runtime secrets → AWS Secrets Manager
Why?
•	Prevents secrets exposure in:
o	Code
o	Docker images
o	CI logs
Implementation
Application retrieves secrets dynamically using boto3.
________________________________________
 Reverse Proxy (Nginx)
•	Routes traffic to container
•	Acts as entry point for users
•	Enables HTTPS termination
________________________________________
HTTPS (Let’s Encrypt)
•	SSL certificates generated using Certbot
•	HTTP automatically redirects to HTTPS
•	Certificates auto-renewed
________________________________________
Deployment Strategy (Blue-Green)
How it works:
1.	New container starts on alternate port
2.	Health check ensures readiness
3.	Nginx switches traffic
4.	Old container is removed
Result:
•	Zero downtime deployment
•	Instant rollback capability
________________________________________
Health Monitoring
•	Docker HEALTHCHECK endpoint /health
•	Nginx validates backend availability
•	Deployment waits for healthy state before switching
________________________________________
Rollback Strategy
If deployment fails:
•	Switch Nginx back to previous port
•	Restart previous container
________________________________________
Docker Hub
Images are pushed with:
•	latest tag
•	(Optional) version tags
________________________________________
EC2 Setup
•	Docker installed
•	Security groups configured
•	Only necessary ports open
•	Containers auto-restart on crash
________________________________________
Testing
•	Unit tests using pytest
•	Lint checks enforced
•	Manual failure simulations:
o	Container crash
o	Deployment failure
o	Health check failure
________________________________________
When a container fails:

- Docker automatically restarts the container due to the restart policy
- If the container fails health checks, it is not used during deployment
- Nginx continues routing traffic to the healthy container
- During deployment, traffic is only switched after health validation
________________________________________
Conclusion
This project demonstrates:
•	Automation
•	Security
•	Reliability
•	Production-ready deployment practices


