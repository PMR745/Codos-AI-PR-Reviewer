import sys
import os
from pathlib import Path

# Print current directory
print(f"Current directory: {os.getcwd()}")

# Try to locate the config file
config_paths = [
    Path(".secrets.toml"),
    Path("pr_agent/settings/.secrets.toml"),
    Path("settings/.secrets.toml"),
    Path(os.path.expanduser("~/.pr_agent/.secrets.toml")),
]

for path in config_paths:
    print(f"Checking {path} - exists: {path.exists()}")
    if path.exists():
        print(f"Found config at: {path}")
        with open(path, "r") as f:
            print(f"First 10 lines of file:")
            for i, line in enumerate(f):
                if i < 10:
                    print(f"  {line.strip()}")
                else:
                    break

# Try to import pr_agent's config loading
try:
    sys.path.append(".")
    from pr_agent.settings.config import Config
    config = Config()
    print("\nPR_AGENT CONFIG CONTENT:")
    print(f"GitHub deployment type: {config.get('github.deployment_type')}")
    print(f"GitHub app_id: {config.get('github.app_id')}")
    print(f"GitHub installation_id: {config.get('github.installation_id')}")
except Exception as e:
    print(f"Error loading PR Agent config: {e}")

