import os

# Folder structure relative to current directory
structure = [
    "usecases/chat-api/app",
    "usecases/chat-api/tests",
    "usecases/rag-qa-system/app",
    "usecases/multi-agent-workflow/app",
    "services/vector-db",
    "services/logging-monitoring/dashboards",
    "services/api-gateway",
    "infra/docker",
    "infra/github-actions",
    "infra/deployment/terraform",
    "docs/architecture-diagrams",
    "docs/blog-drafts",
]

# Files to create with content placeholders (relative to current dir)
files_to_create = {
    "README.md": "# NextGen AI Engineer Playbook\n\nProject Overview...",
    ".gitignore": "*.pyc\n__pycache__/\n.env\n",
    "LICENSE": "MIT License placeholder...",
    "usecases/chat-api/README.md": "# Chat API\n\nDescription of chat API microservice.",
    "usecases/chat-api/app/main.py": "# main.py placeholder\n\nif __name__ == '__main__':\n    print('Hello from chat-api!')\n",
    "usecases/chat-api/requirements.txt": "# requirements.txt placeholder\nfastapi\nuvicorn\nopenai\n",
    "services/vector-db/docker-compose.yml": "# Docker Compose for Vector DB\nversion: '3'\nservices:\n  vector-db:\n    image: vector-db-image-placeholder\n",
    "infra/docker/docker-compose.yml": "# Docker Compose for all services\nversion: '3'\nservices:\n  chat-api:\n    build: ../../usecases/chat-api\n",
    "infra/github-actions/chat-api.yml": "# GitHub Actions workflow placeholder\nname: CI for Chat API\non: [push]\njobs:\n  build:\n    runs-on: ubuntu-latest\n",
    "infra/deployment/render.yaml": "# Render deployment config placeholder\nservices:\n  - type: web\n    name: chat-api\n",
    "docs/system-design-notes.md": "# System Design Notes\n\nImportant notes on architecture...",
    "docs/job-tracker.md": "# Job Tracker\n\nTrack job applications...",
}

# Create directories
for path in structure:
    os.makedirs(path, exist_ok=True)
    print(f"Created folder: {path}")

# Create files with content
for file_path, content in files_to_create.items():
    folder = os.path.dirname(file_path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created file: {file_path}")
