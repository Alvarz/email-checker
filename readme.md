

#start

Init virtual env (when don't have)

```zsh
python3 -m venv .
```

activate venv

```zsh
source ./bin/activate
```

Freeze requirements.txt

```zsh
pip freeze > requirements.txt
```


install requirements.txt

```zsh
pip install -r requirements.txt
```


Start docker
```cmd
docker run -p 6379:6379 redislabs/redismod:latest
```


To create a gemini api key 

https://aistudio.google.com/app/apikey



available models: 
https://ai.google.dev/gemini-api/docs/models
