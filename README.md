# GitHub Actions Workflow: Secrets & Variables

This GitHub Actions workflow demonstrates how to use **secrets** and **variables** at different scopes, including **workflow-level, job-level, environment-level, and repository-level**.

## Categories of Variables & Secrets

- **Environment Variables**: Scoped to a single workflow (e.g., workflow-level, job-level).
- **Configuration Variables**: Shared across multiple workflows (e.g., environment-level, repository-level).

## Usage

To use this workflow, follow these setup steps:

### 1. **Set Up the Environment (`dev`)**
In your GitHub repository settings, configure a **GitHub Actions Environment** named **`dev`**. Within this environment:

- **Add an environment secret:**
  - `FAMILY_NAME`: *(e.g., "liu")*
- **Add an environment variable:**
  - `NAME`: *(e.g., "John")*

These are considered **configuration variables at the environment level**.

### 2. **Set Up Repository-Level Secrets & Variables**
In your GitHub repository settings, configure:

- **A repository secret:**
  - `PHONE_NUMBER`: *(e.g., "12345678")*
- **A repository variable:**
  - `PROJECT_NAME`: *(e.g., "MyProject")*

These are **configuration variables at the repository level**.

## Summary of Secrets & Variables in This Workflow

| Type        | Scope         | Name           | Example Value  |
|------------|--------------|---------------|---------------|
| **Secret**  | Environment  | `FAMILY_NAME`  | `"liu"`       |
| **Secret**  | Repository   | `PHONE_NUMBER` | `"12345678"`  |
| **Variable**| Environment  | `NAME`         | `"John"`      |
| **Variable**| Repository   | `PROJECT_NAME` | `"MyProject"` |

## How It Works

This workflow will:

1. Run on every `push` or when manually triggered (`workflow_dispatch`).
2. Use environment variables at different scopes:
   - Workflow-level (`Workflow_LEVEL_VAR`)
   - Job-level (`JOB_LEVEL_VAR`)
   - Environment-level and repository-level secrets/variables.
3. Print these values for demonstration (excluding sensitive secrets).
4. Use conditional logic to check secret values.

### Example Output

When executed, the workflow prints:
```yaml
Job-level environment variable: myjob
Workflow-level environment variable: myworkflow
Secrets from the dev environment: ***
Variables from the dev environment: John
Repository secrets: ***
Repository variables: MyProject
```

(*Secrets are masked for security reasons.*)

---

This workflow helps you understand how to manage and use **secrets and variables** effectively in **GitHub Actions**.
 
