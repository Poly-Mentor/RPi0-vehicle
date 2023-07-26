import logging
import json
from websocket_server import WebsocketServer #https://github.com/Pithikos/python-websocket-server
from robot import Robot

def new_message(client, server, message):
    log.debug('new message received: %s', message)
    msg = json.loads(message)
    if "lights" in msg:
        if msg["lights"]:
            robot.lights.on()
        else:
            robot.lights.off()
    if "dir" in msg:
        robot.driveDir(msg['dir'])
    else:
         log.error("can't recognize message received over websocket: %s", message)

server = WebsocketServer(host='0.0.0.0', port=13254, loglevel=logging.INFO)
robot = Robot()
log = logging.getLogger('vehicle_log')
server.set_fn_message_received(new_message)
log.info('starting websocket server')
try:
    server.run_forever()
except Exception as e:
      log.error('websocket server exception occured: %s', str(e), exc_info=True)