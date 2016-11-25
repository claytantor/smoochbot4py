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
SMOOCH_KEY_ID="app_5833aea1f2acf24a002195a1"
SMOOCH_SECRET="DXi9WjDByH4Hh_B1IQuwpVc1"
SMOOCH_APP_TOKEN="32bms7lowsa63v438oamjpyuf"
SMOOCHBOT_NAME="smoochbot"
SMOOCH_WEBOOK_ENDPOINT="https://smoochbot.yourdomain.com/smooch/events"
ROBOT_CONFIG_PATH="/mnt/config/smoochbot.json"
```

## Verifying that You Have Webhooks Configured Correctly For Smooch

```
creating webhook: http://ec2-35-163-72-61.us-west-2.compute.amazonaws.com:8079/smooch/events

{u'webhook': {u'secret': u'84da7soopers3krit6be65c86a553b6c3e7f3a16746051a', u'_id': u'58101ee8891463f000313b61', u'target': u'http://ec2-35-163-72-61.us-west-2.compute.amazonaws.com:8079/smooch/events', u'triggers': [u'message:appUser', u'postback']}}
```


## Configuring The Robot

### Phrases


### Intents
