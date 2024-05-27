# DevOps
*practise DevOps practice for job interview*

## Github actions 

### use a container action to run containerized code

commands:

git remote set-url origin https://liujikuan:<personal access token>@github.com/liujikuan/DevOps.git

git log --all --decorate --oneline --graph

curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token <personal access token>" \
  https://api.github.com/repos/liujikuan/DevOps/actions/workflows/main.yml/dispatches \
  -d '{"ref":"main"}'



** Jenkins pipeline

*** Configure Github webhook to trigger the pipeline

1. Use ngrok as a HTTP proxy
2. create a freestyle project, and set the Git repository in the *Source Code Management* section
3. check the *GitHub hook trigger for GITScm polling* option in Jenkins.
4. create or update a file in the repository
5. 
