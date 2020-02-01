## Create react frontend, create default lambda, create s3 bucket website

```sh
mkdir uf-tech-talk
cd uf-tech-talk
npx create-react-app .
npm run build
serverless create --template aws-python
serverless plugin install -n serverless-s3-sync
# Some, small modifications to serverless.yml, see file
sls deploy
```

## Add database (dynamodb) and make the lambda read from it

Demo

## Make frontend hit api gateway

Demo

## Resources/Credit

https://github.com/facebook/create-react-app  
https://github.com/k1LoW/serverless-s3-sync  
https://www.serverlessops.io/blog/static-websites-on-aws-s3-with-serverless-framework
