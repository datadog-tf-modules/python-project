import os
import subprocess

REPO_URL = "github.com/datadog-tf-modules/python-project.git"
BRANCH = "main"
COMMIT_MESSAGE = "Auto commit from script.py"

# Read token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
USERNAME = "Pradeep_Reddy"

if not GITHUB_TOKEN:
    raise ValueError("❌ Please set GITHUB_TOKEN environment variable first")

# Build HTTPS URL with token
AUTH_REPO_URL = f"https://{USERNAME}:{GITHUB_TOKEN}@{REPO_URL}"

def run_command(cmd):
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr and "nothing to commit" not in result.stderr:
        print(result.stderr.strip())
    return result.returncode

def main():
    if not os.path.exists(".git"):
        run_command("git init")
        run_command(f"git remote add origin {AUTH_REPO_URL}")
        run_command(f"git branch -M {BRANCH}")
    else:
        run_command(f"git remote set-url origin {AUTH_REPO_URL}")

    run_command("git add -A")
    run_command(f'git commit -m "{COMMIT_MESSAGE}" || echo "No changes to commit"')
    run_command(f"git push -u origin {BRANCH}")

if __name__ == "__main__":
    main()
