import requests
import json
import base64

# read the configuration from config.json
with open('config.json') as f:
    config = json.load(f)

TOKEN = config["token"]
OWNER = config["repo_owner"]
REPO = config["repo_name"]
BASE_BRANCH = config["base_branch"]

# Headers for GitHub API
headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}
def trigger_repository_dispatch(event_type, client_payload=None):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches"
    payload = {
        "event_type": event_type,
        "client_payload": client_payload or {}
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f"✅ repository_dispatch event '{event_type}' triggered.")

def get_latest_commit_sha(branch):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/ref/heads/{branch}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["object"]["sha"]

def create_branch(new_branch, from_sha):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/refs"
    payload = {
        "ref": f"refs/heads/{new_branch}",
        "sha": from_sha
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f"✅ Branch '{new_branch}' created.")

def create_file(branch, file_path, content, commit_message):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{file_path}"
    payload = {
        "message": commit_message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch
    }
    response = requests.put(url, headers=headers, json=payload)
    response.raise_for_status()
    print(f"✅ File '{file_path}' committed on branch '{branch}'.")

def create_pull_request(branch, title, body):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls"
    payload = {
        "title": title,
        "head": branch,
        "base": BASE_BRANCH,
        "body": body
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    pr_url = response.json()["html_url"]
    print(f"✅ Pull Request created: {pr_url}")

if __name__ == "__main__":
    new_branch = "feature/auto-pr-test"
    file_path = "auto-created-file.txt"
    content = "This file was created automatically by script."
    commit_message = "Add auto-created file"
    pr_title = "Auto PR: Add a new file"
    pr_body = "This PR was created by Python script using GitHub API."

    latest_sha = get_latest_commit_sha(BASE_BRANCH)
    create_branch(new_branch, latest_sha)
    create_file(new_branch, file_path, content, commit_message)
    create_pull_request(new_branch, pr_title, pr_body)

    # Trigger the repository dispatch event(currently commented out)
#    trigger_repository_dispatch("auto-pr-dispatch", {
#        "triggered_by": "script",
#        "pr_branch": new_branch
#   })
