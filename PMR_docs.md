Command to start the docker container at 3000
`docker run -p 3000:3000 -v "$(pwd)/pr_agent/settings/.secrets.toml:/app/pr_agent/settings/.secrets.toml" pr-agent:github_app`