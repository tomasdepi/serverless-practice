# Serverless 

## Install Dependencies

- Install [Node](https://nodejs.org/en/download/package-manager/)
- Install serverless framework: 
  ```
  npm install serverless -g
  ``` 
- Configure credentials: (also setting .aws/credentials will work)
  ```
  serverless config credentials -p aws -k aws_key --secret aws_secret serverless-admin
  ```

## Usuful Command
|   | Command |
|---|---|
| Deploy stack | sls deploy -v |
| Invoke single function | sls invoke -f hello -l |
| Deploy just a function | sls deploy function -f hello |
| Output function logs | sls logs -f hello |
