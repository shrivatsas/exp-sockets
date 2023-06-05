# exp-sockets

## SocketIO
    Using Flask-SocketIO - enables websockets when available, downgrades to long-polling otherwise.

    Need to run using either `eventlet` (preferably) or `gevent-websockets`

    gunicorn and eventlet have a bug https://github.com/benoitc/gunicorn/issues/2582
    ```
    gunicorn --worker-class eventlet -w 1 app:app
    ```

    ```
    gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app
    ```

## WebSocket

## RSocket