Command to start the docker container at 3000
`docker run -p 3000:3000 -v "$(pwd)/pr_agent/settings/.secrets.toml:/app/pr_agent/settings/.secrets.toml" pr-agent:github_app`

# Start server command
`uvicorn pr_agent.servers.github_app:app --host 0.0.0.0 --port 3000`

# Smee connection command
`npx smee-client --url https://smee.io/you_smee_link --target http://localhost:3000/api/v1/github_webhooks`