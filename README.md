# smoochbot4py

Smooch is a very easy to use and install message framework for websites to collect and communicate with visitors. dronze.com thought it was a perfect framework to get our bot talking to people quickly.

Smoochbot4py a fully functional robot you can wire up to your webpage written in python. Smoochbot4py is completely data driven, that is you don't need to program it for it to have conversations with people. That makes it less smart than the other dronze.com robots that are powered by teh artificial intelligence technologies of NLP (natural language processing) and deep learning.

## Running The Docker image
The smoochbot will use the configuration and brain graph you provide.

```
docker run -t -d --name smoochbot -v ${CONFIG_DIR}:/mnt/config -p 8079:8079 claytantor/smoochbot4py:latest
```

## Configuring The Application

```
SMOOCH_KEY_ID="app_5833aea1f2ccf24b002395a1"
SMOOCH_SECRET="DXi9WjDTyH4Hh_A0IQuwpVc1"
SMOOCH_APP_TOKEN="33bms6lowss63v438oamjpyuf"
SMOOCHBOT_NAME="smoochbot"
SMOOCH_WEBOOK_ENDPOINT="https://claydev.dronze.com/smooch/events"
SMOOCH_CLIENT_ENDPOINT="http://localhost:9090/#/"
ROBOT_CONFIG_PATH="/mnt/config/smoochbot.json"
```

## Configuring The Robot

### Phrases


### Intents
