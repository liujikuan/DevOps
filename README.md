

## JavaScript Action

This repository contains a sample JavaScript GitHub Action that interacts with a Redis service container which would be destroyed when the job completes.

The workflow consists of two jobs attempting to connect to Redis:

1. **`container-job`**: Runs inside a **Docker container** (`node:20.14.0-alpine3.20`) and communicates with a Redis service container.

2. **`non-container-job`**: Runs directly on the **GitHub-hosted runner** (`ubuntu-latest`) and uses a Redis service container.

   

## Key Differences Summary

| Feature               | `container-job` (Containerized)          | `non-container-job` (Standard Runner)  |
| --------------------- | ---------------------------------------- | -------------------------------------- |
| Execution Environment | Runs inside a container (Node.js)        | Runs directly on Ubuntu runner         |
| Redis Access          | Uses service label (`redis`)             | Uses `127.0.0.1` (localhost)           |
| Network Isolation     | Fully isolated container network         | Can access host services               |
| Port Mapping          | Not needed                               | Required (`ports: 6379:6379`)          |
| Flexibility           | More controlled, but limited host access | Full access to host, but less isolated |

### Files

- `client.js`: This script connects to the Redis service container, sets some keys and fields, and retrieves them.
- `action.yml`: Defines the GitHub Action that runs `client.js`.

### 
