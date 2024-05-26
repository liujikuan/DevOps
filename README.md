# DevOps
practise DevOps practice for job interview

** Github actions 

*** use a container action to run containerized code



** commands

git remote set-url origin https://liujikuan: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@github.com/liujikuan/DevOps.git

git log --all --decorate --oneline --graph

curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token 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" \
  https://api.github.com/repos/liujikuan/DevOps/actions/workflows/main.yml/dispatches \
  -d '{"ref":"main"}'



** Jenkins pipeline

*** configure Github webhook to trigger the pipeline

1. Use ngrok as a HTTP proxy
2. check the GitHub hook trigger for GITScm polling option in Jenkins.
