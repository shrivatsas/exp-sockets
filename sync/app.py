from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print(f'Received message {message}')
    # _send_ to send `message` and `json` special events, _emit_ for named events
    socketio.send(f'echo: {message}')

if __name__ == '__main__':
    socketio.run(app, debug=True)