# Flask Mongo Template
This Flask template is designed for Gitpod and is based on CodeInstitute's template. It comes with a `.gitignore` file, two helper scripts and an `app.py` with most of the `imports` defined.

## requirements.txt

The requirements.txt include dependencies for:

1. Flask
2. pymongo
3. pytest
4. load-dotenv
5. flask-login

To install, run:
```
  pip3 install -r requirements.txt
```

## Helper script: start-mongo.sh
If you wish to use the local instance of Mongo client, simply follow the steps below:

1. Create a new directory `data/db` in the Explorer panel
2. Enable execution permission for the file `start-mongo.sh` by typing the following in the terminal:
```
  chmod 775 start-mongo.sh
 ```
 
From now on, you can run the local instance of Mongo by typing:

```
  ./start-mongo.sh
```

## Helper script: generate Flask keys
If you wish to use sessions in Flask, you must give the app a secret key. You can generate one with the `generate-key` script:
``` 
  python3 generate-key.py
```
Copy and paste the string between the quotes and set it as the `SECRET_KEY` in the `.env` file
 
