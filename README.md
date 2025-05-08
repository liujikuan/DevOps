# GitHub API Automation Tool

This is a Python-based DevOps utility that interacts with the GitHub REST API to automate common developer tasks such as:

- Creating a new branch from a base branch
- Committing a new file to that branch
- Creating a pull request (PR) from the branch
- (Optional) Triggering GitHub Actions workflows manually

---

## 📌 Features

- 🔧 Fully scriptable via Python and GitHub API
- 📤 Automates pull request creation
- 🚀 Easy to integrate into CI/CD pipelines
- 🔐 Secure configuration using external JSON file (token not hardcoded)

---

## 📂 Project Structure

.
 ├── main.py             # Main script that automates PR creation
 ├── config.json         # Config file (store repo/token info)
 ├── requirements.txt    # Python dependency file
 └── README.md           # This file

---

## 🔧 Prerequisites

- Python 3.10+
- A GitHub [Personal Access Token](https://github.com/settings/tokens) with the following scopes:
  - `repo`
  - `workflow` (if you intend to trigger workflows)

---

## 🛠️ Installation & Usage

1. Clone this repo:
   ```bash
   git clone https://github.com/liujikuan/DevOps.git
   cd DevOps/github-api-automation-tool
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `config.json`:
   ```bash
   {
     "token": "ghp_xxxxxxxxxxxxxxxxxxxxxxx",
     "repo_owner": "liujikuan",
     "repo_name": "DevOps",
     "base_branch": "main"
   }
   
   ```
4. Run the script:
   ```bash
   python main.py
   ```

## ✅ Output Example

- A new branch is created: `feature/auto-pr-test`
- A new file (`auto-created-file.txt`) is committed to that branch
- A pull request is created on GitHub automatically

## 🔐 Security Note

- Do **not** commit `config.json` or any token to version control.
- Use `.gitignore` to exclude it:
```bash
echo config.json >> .gitignore
```

## 🧩 TODO (Next Steps)

-  Add support for triggering GitHub Actions workflows via `repository_dispatch`
-  Add command-line argument support
-  Dockerize this script for easier usage in CI

## 🤝 Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License.
