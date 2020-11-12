import base64
import json
import requests
import uuid
import websocket

from google.protobuf.json_format import Parse
import Devialet.CallMeMaybe.CallMeMaybe_pb2 as maybe


def on_message(ws, message):
    print(f"received message: {message}")

def on_error(ws, error):
    print(f"received error: {error}")

def on_close(ws):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")

    id = uuid.uuid4().hex
    id_bytes = id.encode('ascii')
    id_base64 = base64.b64encode(id_bytes)
    tracking_id = id_base64.decode('ascii')

    json_string = {
        "type": "Request",
        "subType" : "Open",
        "tracking": {
        "id": tracking_id
        },
        "target": {
            "serviceId": 1,
        },
        "body": None
    }

    print(f"Sending message: {json_string}")

    # Convert the json payload to protobuf and serialize as string
    json_payload = json.dumps(json_string)
    proto_payload = Parse(json_payload, maybe.BaseRequest())

    ws.send(proto_payload.SerializeToString())

if __name__ == "__main__":

    # url = "192.168.1.10:46135"
    url = "192.168.1.11:34639"

    websocket.enableTrace(True)

    ws = websocket.WebSocketApp("ws://192.168.1.10:46135",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)

    ws.on_open = on_open
    ws.run_forever()

    '''
    --- request header ---
    GET / HTTP/1.1
    Upgrade: websocket
    Host: 192.168.1.10:46135
    Origin: http://192.168.1.10:46135
    Sec-WebSocket-Key: lh4hS5gXA0Am+my4m0GpRw==
    Sec-WebSocket-Version: 13
    Connection: upgrade
    -----------------------
    --- response header ---
    HTTP/1.1 101 Switching Protocols
    Upgrade: websocket
    Connection: Upgrade
    Sec-WebSocket-Accept: HUox4JoxZa+VsOLUoK+1wsyTbBU=
    Access-Control-Allow-Credentials: false
    Access-Control-Allow-Methods: GET
    Access-Control-Allow-Headers: content-type
    Access-Control-Allow-Origin: http://192.168.1.10:46135
    Date: Thu, 12 Nov 2020 08:32:40 GMT
    -----------------------
    '''