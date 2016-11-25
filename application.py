import smooch
import robot
import os
import sys
import json

from flask import Flask, request, g, Response
from werkzeug.local import LocalProxy

app = Flask(__name__)
app.config.from_envvar('FLASK_APPLICATION_SETTINGS')

def get_robot():
    robot_instace = getattr(g, '_robot', None)
    if robot_instace is None:
        botdata = robot.load_robot(app.config["ROBOT_CONFIG_PATH"], app.config['SMOOCHBOT_NAME'])
        robot_instace = g._robot = robot.Robot(botdata)
    return robot_instace

def init_smooch(flask_app):
    jwt = smooch.get_jwt(flask_app.config["SMOOCH_KEY_ID"], flask_app.config['SMOOCH_SECRET'])
    smooch_api_instance = smooch.SmoochV1(jwt=jwt)    

    #test if there are any webhooks for this config
    webhooks_available = smooch_api_instance.list_webhooks()

    #check if the endpoint is in the config
    found = False
    for hook in webhooks_available['webhooks']:
        if hook['target']==flask_app.config["SMOOCH_WEBOOK_ENDPOINT"]:
            found=True

    # tell smooch to start sending events to this place
    if not found:
        print "creating webhook:{0}".format(flask_app.config["SMOOCH_WEBOOK_ENDPOINT"])
        create_response = smooch_api_instance.save_webhook(flask_app.config["SMOOCH_WEBOOK_ENDPOINT"], ["message:appUser", "postback"])
	print create_response

def get_smooch_api():
    smooch_api_instance = getattr(g, '_smooch_api', None)
    if smooch_api_instance is None:

        jwt = smooch.get_jwt(app.config["SMOOCH_KEY_ID"], app.config['SMOOCH_SECRET'])
        smooch_api_instance = g._smooch_api = smooch.SmoochV1(jwt=jwt)

        #test if there are any webhooks for this config
        webhooks_available = smooch_api_instance.list_webhooks()

        #check if the endpoint is in the config
        found = False
        for hook in webhooks_available['webhooks']:
            if hook['target']==app.config["SMOOCH_WEBOOK_ENDPOINT"]:
                found=True

        # tell smooch to start sending events to this place
        if not found:
            smooch_api_instance.save_webhook(app.config["SMOOCH_WEBOOK_ENDPOINT"], ["message:appUser", "postback"])

    return smooch_api_instance

# ========== routes =============
@app.route("/hc")
def hc():
    """
    health check if you need that.
    """
    data = {'message':'succeed'}
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

@app.route('/smooch/events', methods=['POST'])
def smooch_events():
    """
    the firehose of events that the webhooks subscribed to,
    this will send all messages from people who visit your website
    to this endmpoint, the robot then parses those messages and
    does a postback of its response.
    """
    print json.dumps(request.json)

    # get the singletons
    smooch_api = LocalProxy(get_smooch_api)
    robot = LocalProxy(get_robot)

    for message in request.json['messages']:
        response = robot.process_input(message['text'])
        smooch_api.postback_message(response, message['authorId'])

    data = {'message':'succeed'}
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

def main(argv):
    init_smooch(app)
    app.run(host='0.0.0.0', port=int(argv[0]), debug=False)

if __name__ == "__main__":
    main(sys.argv[1:])
