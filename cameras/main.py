''' Main file for entering the application '''
from flask import Flask
import manager
import config


app = Flask(__name__)
process = manager.ProcessManager()


@app.route('/camera/on', methods=['GET'])
def turn_camera_on():
    ''' App route for turning camera on '''
    process.run()
    return 'Camera: Turned on'


@app.route('/camera/off', methods=['GET'])
def turn_camera_off():
    ''' App route for turning camera off '''
    process.terminate()
    return 'Camera: Turned off'


if __name__ == '__main__':
    app.run(
        host=config.Server.HOST.value,
        port=config.Server.PORT.value,
        debug=config.Server.DEBUG.value
    )
