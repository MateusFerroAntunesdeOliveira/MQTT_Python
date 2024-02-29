from application.configs.broker_configs import mqtt_broker_configs

topic = mqtt_broker_configs["TOPIC"]

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Connected to broker - Client '{client._client_id.decode('utf-8')}' with code: {rc}")
        client.subscribe(topic)
    else:
        print(f"Connection failed with code: {rc}")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed to topic '{topic}' with mid: {mid} and QoS: {granted_qos}\n")

def on_message(client, userdata, message):
    print(f"\nMessage topic: {message.topic}")
    print(f"Received message: {message.payload.decode('utf-8')}\n")
