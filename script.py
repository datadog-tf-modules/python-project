import os
import subprocess

# Configurations
REPO_URL = "https://github.com/datadog-tf-modules/python-project.git"
BRANCH = "main"
COMMIT_MESSAGE = "Auto commit from script.py"

def run_command(cmd):
    """Run a shell command and print output"""
    print(f"$ {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout.strip())
    if result.stderr and "nothing to commit" not in result.stderr:
        print(result.stderr.strip())
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def main():
    # Step 1: Initialize git if not already
    if not os.path.exists(".git"):
        run_command("git init")
        run_command(f"git remote add origin {REPO_URL}")
        run_command(f"git branch -M {BRANCH}")

    # Step 2: Add all changes (including deletions)
    run_command("git add -A")

    # Step 3: Commit (only if there are staged changes)
    code, out, err = run_command(f'git commit -m "{COMMIT_MESSAGE}"')
    if "nothing to commit" in err or "nothing to commit" in out:
        print("✅ No changes to commit. Working directory clean.")
        return

    # Step 4: Push to GitHub
    run_command(f"git push -u origin {BRANCH}")

if __name__ == "__main__":
    main()
