# youtube_bot
## Selenium Version

### Dependencies
```
pip install selenium, google-auth-oauthlib, google-api-python-client
```
## Webserver Version
### Dependencies
Install ngrok
```
 curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```

Install flask
```
pip install flask
```

Write to the config file in $HOME:/.config/ngrok/ngrok.yml
```
version: "2"
authtoken: [Your Token]
tunnels:
    website:
        proto: http
        schemes:
            - https
        hostname: [Your Doamin Name]
        addr: 5001 
```

Get a domain using ngrok and run the service using daemon
