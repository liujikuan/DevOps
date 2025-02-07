

## JavaScript Action

This repository contains a sample JavaScript GitHub Action that interacts with a Redis service container which would be destroyed when the job completes.

### Files

- `client.js`: This script connects to the Redis service container, sets some keys and fields, and retrieves them.
- `action.yml`: Defines the GitHub Action that runs `client.js`.

### Usage

To use this action in your workflow, I reference it in my `.github/workflows/redis.yml` file.
