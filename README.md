# Table of Contents
- [2-factor authentication](https://github.com/liujikuan/DevOps/tree/2FA)
- [service Container & RedisClient](https://github.com/liujikuan/DevOps/tree/serviceContainerAndRedisClient)


# What I did
GitHub actions workflow triggered by push and workflow_dispatch executes a custom action.
The action initiates a docker container.
The Docker container accepts input and outputs results.


# Note

## some useful Git commands

git remote set-url origin `https://liujikuan:<personal access token>@github.com/liujikuan/DevOps.git`

git log --all --decorate --oneline --graph

## Github actions 

**are categorized into two:**
1. use a container action to run containerized code
2. use a JavaScript action to run javascript code such as Node.js code



**The following command triggers a GitHub Actions workflow for the specified branch using the GitHub API**

curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token `<personal access token>`" \
  https://api.github.com/repos/liujikuan/DevOps/actions/workflows/main.yml/dispatches \
  -d '{"ref":"main"}'



## Jenkins pipeline

### Configure Github webhook to trigger the pipeline

1. Use ngrok as a HTTP proxy
2. create a freestyle project, and set the Git repository in the *Source Code Management* section
3. check the *GitHub hook trigger for GITScm polling* option in Jenkins.
4. create or update a file in the repository

