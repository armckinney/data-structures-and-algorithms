---
description: Rebuild devcontainer for the current project
---

// turbo-all
1. Stop the dev container and remove it
```bash
docker compose -f .devcontainer/docker-compose.yaml down --volumes --rmi all
```

2. Rebuild the devcontainer image (optional but recommended for a full rebuild)
```bash
docker compose -f .devcontainer/docker-compose.yaml build --no-cache
```

3. Start the container in detached mode
```bash
docker compose -f .devcontainer/docker-compose.yaml up -d
```

4. Run the Antigravity command to reopen in container
> **Action Required**: Open the Command Palette (`Cmd+Shift+P`) and run **"Remote-Containers: Reopen Folder in Container"** (or click the "Reopen in Container" button in the UI).