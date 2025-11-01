<h1>PROJECT 1: CI/CD Pipeline for Microservices (HIGHEST IMPACT)</h1>
<h4>Time: 2-3 weeks | Difficulty: Intermediate</h4>

<h3>What You'll Build:</h3><br>
A complete CI/CD pipeline that automatically tests, builds, and deploys a simple microservices application.

<h3>Tech Stack:</h3>
<ul>
<li><b>Application:</b> Python Flask microservice (weather API, stock ticker, or todo app)</li>
<li><b>Version Control:</b> GitHub/GitLab</li>
<li><b>CI/CD:</b> Jenkins or GitHub Actions (GitHub Actions is easier to start)</li>
<li><b>Containerization:</b> Docker</li>
<li><b>Orchestration:</b> Docker Compose (start here) or Kubernetes (if ambitious)</li>
<li><b>Testing:</b> pytest for unit tests</li>
<li><b>Monitoring:</b> Prometheus + Grafana (optional but impressive)</li>
</ul>

<h3>Step-by-Step:</h3>
<ol>
<li><b>Week 1: Build the Application</b><br>
<ul>
<li>Create 2-3 microservices (e.g., frontend, API, database)</li>
<li>Write unit tests using pytest</li>
<li>Containerize each service with Docker</li>
<li>Set up docker-compose.yml for local development</li>
</ul>

<li><b>Week 2: Implement CI/CD</b><br>
<ul>
<li>Set up GitHub Actions or Jenkins</li>
<li>Create pipeline stages:</li>
<ul>
<li>Lint code (pylint/flake8)</li>
<li>Run unit tests</li>
<li>Build Docker images</li>
<li>Push to Docker Hub or AWS ECR</li>
<li>Deploy to staging environment</li>
</ul>
<li>Add automated rollback on failure</li>
</ul>

<li><b>Week 3: Add Monitoring & Documentation</b><br>
<ul>
<li>Set up basic monitoring (health checks, logging)</li>
<li>Create comprehensive README with architecture diagram</li>
<li>Add screenshots/videos of pipeline running</li>
<li>Deploy to AWS EC2 or DigitalOcean (free tier)</li>
</ul>

</ol>